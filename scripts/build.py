"""Build the NFL home-field-advantage dataset and analysis outputs.

Sources (downloaded to ~/nfl/raw):
  - FiveThirtyEight nfl-elo-game: every game 1920-2020 (used for 1920-1998)
  - nflverse games.csv: every game 1999-2026 with stadium, roof, surface, temp, wind, ESPN ids
  - spreadspoke_scores.csv (NFLweather-derived): stadium + weather 1966-2025
  - TidyTuesday 2020-02-04 attendance.csv: weekly attendance 2000-2019
"""
import json, sys, math
import numpy as np, pandas as pd
import statsmodels.formula.api as smf
sys.path.insert(0, "/root/nfl/scripts")
import meta

RAW = "/root/nfl/raw/"
OUT = "/root/nfl/out/"
import os; os.makedirs(OUT, exist_ok=True)

# ------------------------------------------------------------------ games
e = pd.read_csv(RAW + "nfl-elo-game_nfl_games.csv")
e = e[e.season <= 1998].copy()
code538 = {"WSH": "WAS", "OAK": "LV"}
e["home"] = e.team1.replace(code538); e["away"] = e.team2.replace(code538)
e["date"] = pd.to_datetime(e.date)
old = pd.DataFrame(dict(season=e.season, date=e.date, home=e.home, away=e.away, hs=e.score1, as_=e.score2,
                        neutral=e.neutral.astype(int), playoff=(e.playoff.notna() & (e.playoff.astype(str) != "0")).astype(int)))
old["src"] = "538"; old["espn"] = None; old["stadium_id"] = None; old["roof_nv"] = None; old["surf_nv"] = None
old["temp_nv"] = np.nan; old["wind_nv"] = np.nan; old["spread"] = np.nan; old["div"] = np.nan; old["week"] = np.nan

n = pd.read_csv(RAW + "nfldata_games.csv")
n = n[n.home_score.notna()].copy()
nvmap = {"OAK": "LV", "SD": "LAC", "STL": "LAR", "LA": "LAR"}
new = pd.DataFrame(dict(season=n.season, date=pd.to_datetime(n.gameday), home=n.home_team.replace(nvmap),
                        away=n.away_team.replace(nvmap), hs=n.home_score, as_=n.away_score,
                        neutral=(n.location == "Neutral").astype(int), playoff=(n.game_type != "REG").astype(int)))
new["src"] = "nflverse"; new["espn"] = n.espn.astype("Int64").astype(str).replace("<NA>", None).values
new["stadium_id"] = n.stadium_id.values; new["stadium_nv"] = n.stadium.values
new["roof_nv"] = n.roof.values; new["surf_nv"] = n.surface.str.strip().values
new["temp_nv"] = n.temp.values; new["wind_nv"] = n.wind.values
new["spread"] = n.spread_line.values  # positive = home favoured by that many points
new["div"] = n.div_game.values; new["week"] = n.week.values
g = pd.concat([old, new], ignore_index=True)
g = g.sort_values(["date", "home"]).reset_index(drop=True)
g["margin"] = g.hs - g.as_
g["hwin"] = np.where(g.margin > 0, 1.0, np.where(g.margin < 0, 0.0, 0.5))

# league
def league(r):
    s = r.season
    if 1946 <= s <= 1949 and r.home in meta.AAFC_TEAMS and r.away in meta.AAFC_TEAMS: return "AAFC"
    if 1960 <= s <= 1969 and r.home in meta.AFL_TEAMS and r.away in meta.AFL_TEAMS and not r.playoff: return "AFL"
    if 1960 <= s <= 1969 and r.home in meta.AFL_TEAMS and r.away in meta.AFL_TEAMS: return "AFL"
    if s <= 1921: return "APFA"
    return "NFL"
g["league"] = g.apply(league, axis=1)

# ------------------------------------------------------------------ spreadspoke venue/weather join
s = pd.read_csv(RAW + "spreadspoke_scores.csv")
name2fr = {}
for nm in pd.concat([s.team_home, s.team_away]).unique():
    w = nm.split()[-1]
    m = {"Cardinals": "ARI", "Falcons": "ATL", "Ravens": "BAL", "Bills": "BUF", "Panthers": "CAR", "Bears": "CHI",
         "Bengals": "CIN", "Browns": "CLE", "Cowboys": "DAL", "Broncos": "DEN", "Lions": "DET", "Packers": "GB",
         "Texans": "HOU", "Jaguars": "JAX", "Chiefs": "KC", "Raiders": "LV", "Chargers": "LAC", "Rams": "LAR",
         "Dolphins": "MIA", "Vikings": "MIN", "Patriots": "NE", "Saints": "NO", "Giants": "NYG", "Jets": "NYJ",
         "Eagles": "PHI", "Steelers": "PIT", "49ers": "SF", "Seahawks": "SEA", "Buccaneers": "TB", "Titans": "TEN",
         "Redskins": "WAS", "Commanders": "WAS", "Team": "WAS"}.get(w)
    if w == "Oilers": m = "TEN"
    if w == "Colts": m = "IND"
    name2fr[nm] = m
s["home"] = s.team_home.map(name2fr); s["away"] = s.team_away.map(name2fr)
s["date"] = pd.to_datetime(s.schedule_date, format="mixed")
s = s.rename(columns=dict(weather_temperature="temp_ss", weather_wind_mph="wind_ss", weather_humidity="hum_ss",
                          weather_detail="detail_ss", stadium="stadium_ss"))
s = s[["date", "home", "away", "stadium_ss", "temp_ss", "wind_ss", "hum_ss", "detail_ss"]]
# join on home+away within +-2 days
g["gid"] = np.arange(len(g))
cand = g[["gid", "date", "home", "away"]].merge(s, on=["home", "away"], suffixes=("", "_s"))
cand = cand[(cand.date - cand.date_s).abs() <= pd.Timedelta(days=2)]
cand = cand.sort_values("gid").drop_duplicates("gid")
g = g.merge(cand.drop(columns=["date", "home", "away", "date_s"]), on="gid", how="left")
print("spreadspoke matched 1966-1998:", g[(g.season.between(1966, 1998))].stadium_ss.notna().mean().round(4))

# ------------------------------------------------------------------ venue attributes
def venue_id(r):
    if r.src == "nflverse":
        if r.stadium_id == "BUF00" and r.season >= 2026: return "NEWHIGHMARK"
        return meta.NFLVERSE_MAP.get(r.stadium_id, "INTL")
    if isinstance(r.stadium_ss, str):
        return meta.SPREADSPOKE_MAP.get(r.stadium_ss, "INTL" if r.neutral else None)
    return None
meta.venue("NEWHIGHMARK", "Highmark Stadium (2026)", "Orchard Park, NY", "FB", "outdoors", 62000, meta.G())
g["venue"] = g.apply(venue_id, axis=1)
g.loc[g.neutral == 1, "venue"] = g.loc[g.neutral == 1, "venue"].where(
    g.loc[g.neutral == 1, "venue"].isin(meta.V) & (g.loc[g.neutral == 1, "src"] == "nflverse"), "INTL")

def surface(r):
    if r.src == "nflverse" and isinstance(r.surf_nv, str) and r.surf_nv:
        return "Natural grass" if r.surf_nv in ("grass", "dessograss") else "Artificial turf"
    if r.venue and r.venue in meta.V:
        sf = meta.surface_for(r.venue, r.season)
        if sf: return "Artificial turf" if sf == "artificial" else "Natural grass"
    if r.season < 1966: return "Natural grass"   # first NFL artificial turf: 1968 Astrodome
    return None
g["surface"] = g.apply(surface, axis=1)

def roof(r):
    if r.src == "nflverse" and isinstance(r.roof_nv, str):
        return {"outdoors": "Open air", "dome": "Dome", "closed": "Retractable (closed)", "open": "Retractable (open)"}[r.roof_nv]
    if r.season < 1966: return "Open air"
    if r.venue in meta.V:
        rf = meta.V[r.venue]["roof"]
        return {"outdoors": "Open air", "dome": "Dome", "partial": "Open air", "retractable": "Retractable (closed)"}[rf]
    return None
g["roof"] = g.apply(roof, axis=1)
g["indoor"] = g.roof.isin(["Dome", "Retractable (closed)"]).astype(float).where(g.roof.notna())
g["shape"] = g.venue.map(lambda v: meta.V[v]["shape"] if v in meta.V else "")
g.loc[g.neutral == 1, "shape"] = g.loc[g.neutral == 1, "shape"].replace("", "INTL")
g["venue_name"] = g.venue.map(lambda v: meta.V[v]["name"] if v in meta.V else None)
g.loc[(g.src == "nflverse") & (g.neutral == 1), "venue_name"] = g.loc[(g.src == "nflverse") & (g.neutral == 1), "stadium_nv"]

def mlb(r):
    v = meta.V.get(r.venue)
    if not v or not v["mlb"]: return 0, 0
    team, a, b = v["mlb"]
    if not (a <= r.season <= b): return 0, 0
    inseason = int(r.date.month < 10 or (r.date.month == 10 and r.date.day <= 3))
    return 1, inseason
mm = g.apply(mlb, axis=1, result_type="expand"); g["mlb_shared"] = mm[0]; g["mlb_inseason"] = mm[1]

# weather: prefer nflverse 1999+, else spreadspoke; indoor games -> no outdoor weather
g["temp"] = g.temp_nv.where(g.temp_nv.notna(), g.temp_ss)
g["wind"] = g.wind_nv.where(g.wind_nv.notna(), g.wind_ss)
g.loc[g.indoor == 1, ["temp", "wind"]] = np.nan
d = g.detail_ss.fillna("").str.lower()
g["precip"] = np.where(d.str.contains("snow"), "Snow", np.where(d.str.contains("rain"), "Rain", np.where(g.temp.notna(), "None reported", None)))
g.loc[g.indoor == 1, "precip"] = None

# attendance 2000-2019 (TidyTuesday): home team's weekly attendance in a home game
att = pd.read_csv(RAW + "tt_attendance.csv")
att["fr"] = (att.team + " " + att.team_name).map(lambda x: name2fr.get(x) or {
    "Los Angeles Rams": "LAR", "St. Louis Rams": "LAR", "Washington Redskins": "WAS", "San Diego Chargers": "LAC",
    "Los Angeles Chargers": "LAC", "Oakland Raiders": "LV", "Houston Texans": "HOU", "Tennessee Titans": "TEN"}.get(x))
att = att[att.weekly_attendance.notna()][["year", "week", "fr", "weekly_attendance"]]
g = g.merge(att.rename(columns={"year": "season", "fr": "home", "weekly_attendance": "attendance"}),
            on=["season", "week", "home"], how="left")
g.loc[(g.playoff == 1) | (g.neutral == 1), "attendance"] = np.nan
cap = g.venue.map(lambda v: meta.V[v]["cap"] if v in meta.V else None)
g["fill"] = (g.attendance / cap).clip(upper=1.15)
print("attendance coverage 2000-2019 REG home:", g[(g.season.between(2000, 2019)) & (g.playoff == 0) & (g.neutral == 0)].attendance.notna().mean().round(3))

# ------------------------------------------------------------------ team strength (per-season ridge Massey with HFA)
g["r_home"] = np.nan; g["r_away"] = np.nan; g["hfa_season"] = np.nan
ratings = []
for season, gs in g.groupby("season"):
    teams = sorted(set(gs.home) | set(gs.away)); ix = {t: i for i, t in enumerate(teams)}
    k = len(teams); m = len(gs)
    X = np.zeros((m, k + 1)); y = gs.margin.values.astype(float)
    for j, (h, a, nt) in enumerate(zip(gs.home, gs.away, gs.neutral)):
        X[j, ix[h]] = 1; X[j, ix[a]] = -1; X[j, k] = 0 if nt else 1
    lam = 2.0  # light ridge shrinkage on team ratings (not on HFA)
    R = np.hstack([np.sqrt(lam) * np.eye(k), np.zeros((k, 1))])
    beta = np.linalg.lstsq(np.vstack([X, R]), np.concatenate([y, np.zeros(k)]), rcond=None)[0]
    g.loc[gs.index, "r_home"] = [beta[ix[t]] for t in gs.home]
    g.loc[gs.index, "r_away"] = [beta[ix[t]] for t in gs.away]
    g.loc[gs.index, "hfa_season"] = beta[k]
    for t in teams: ratings.append(dict(season=season, team=t, rating=round(beta[ix[t]], 2)))
g["strength_diff"] = g.r_home - g.r_away
g["adj"] = g.margin - g.strength_diff   # strength-adjusted home margin (for neutral games ~ 0 expected)

# ------------------------------------------------------------------ team climate (visitor from dome/warm city)
hg = g[g.neutral == 0]
clim = hg.groupby(["season", "home"]).apply(lambda x: pd.Series(dict(
    indoor_share=x.indoor.mean(), late_temp=x[x.date.dt.month.isin([11, 12, 1])].temp.median())), include_groups=False).reset_index()
clim["warm_or_dome"] = ((clim.indoor_share >= 0.5) | (clim.late_temp >= 55)).astype(int)
clim.loc[clim.indoor_share.isna(), "warm_or_dome"] = np.nan
g = g.merge(clim[["season", "home", "warm_or_dome"]].rename(columns={"home": "away", "warm_or_dome": "away_warm"}), on=["season", "away"], how="left")
g = g.merge(clim[["season", "home", "warm_or_dome"]].rename(columns={"warm_or_dome": "home_warm"}), on=["season", "home"], how="left")

# names
nm = g.apply(lambda r: meta.team_name(r.home, r.season)[0], axis=1); g["home_name"] = nm
g["away_name"] = g.apply(lambda r: meta.team_name(r.away, r.season)[0], axis=1)
g["covid2020"] = ((g.season == 2020) & (g.playoff == 0)).astype(int)

g.to_csv(OUT + "games_full.csv", index=False)

# ------------------------------------------------------------------ analysis
H = g[(g.neutral == 0)].copy()
res = {}
def summ(x):
    nn = len(x); wp = x.hwin.mean()
    return dict(n=int(nn), win=round(wp, 4), win_se=round(math.sqrt(wp * (1 - wp) / nn), 4) if nn else None,
                margin=round(x.margin.mean(), 3), adj=round(x.adj.mean(), 3), adj_se=round(x.adj.std() / math.sqrt(nn), 3) if nn > 1 else None)
res["overall"] = summ(H)
res["overall_modern"] = summ(H[H.season >= 1970])
res["neutral"] = summ(g[g.neutral == 1])

from scipy import stats
bt = stats.binomtest(int((H.hwin == 1).sum()), int((H.hwin != 0.5).sum()), 0.5, alternative="greater")
res["binom_p"] = float(bt.pvalue)

# per-season
per = []
for s_, x in H.groupby("season"):
    d_ = summ(x); d_["season"] = int(s_); d_["hfa_massey"] = round(float(x.hfa_season.iloc[0]), 3)
    per.append(d_)
res["by_season"] = per

# decade
H["decade"] = (H.season // 10 * 10)
H["yr10"] = (H.season - 2000) / 10
H["covid2020"] = H.covid2020
res["by_decade"] = [dict(decade=int(k), **summ(x)) for k, x in H.groupby("decade")]

# trend regressions (adjusted margin), cluster by season
def ols(formula, data, label, cov="cluster"):
    mod = smf.ols(formula, data=data); rows = mod.data.row_labels
    m = mod.fit(cov_type="cluster", cov_kwds={"groups": data.loc[rows, "season"].values}) if cov == "cluster" else mod.fit(cov_type="HC1")
    out = dict(label=label, n=int(m.nobs), r2=round(m.rsquared, 4), terms=[])
    for t in m.params.index:
        out["terms"].append(dict(term=t, b=round(m.params[t], 3), se=round(m.bse[t], 3), p=float(m.pvalues[t])))
    return out

M = H[H.season >= 1966].copy()
M["yr10"] = (M.season - 2000) / 10
M["artificial"] = (M.surface == "Artificial turf").astype(float).where(M.surface.notna())
M["dome"] = M.indoor
M["cold"] = ((M.temp <= 32)).astype(float).where(M.temp.notna() | (M.indoor == 1), np.nan)
M.loc[M.indoor == 1, "cold"] = 0
M["windy"] = (M.wind >= 15).astype(float); M.loc[M.wind.isna(), "windy"] = 0
M["snow"] = (M.precip == "Snow").astype(float); M["rain"] = (M.precip == "Rain").astype(float)
M["cold_x_warmvisitor"] = M.cold * (M.away_warm == 1)
M["mlb_cfg"] = M.mlb_inseason.astype(float)
M["pl"] = M.playoff.astype(float)
M["shape_c"] = M["shape"].replace("", "Unknown")

models = []
models.append(ols("margin ~ 1", H, "Raw home margin (all seasons, no controls)"))
models.append(ols("margin ~ 1 + strength_diff", H, "Home margin controlling for team strength"))
models.append(ols("adj ~ yr10", H, "Trend in strength-adjusted HFA (per decade, centred 2000)"))
models.append(ols("adj ~ covid2020", H[H.season >= 2010], "2020 empty-stadium season vs 2010-2026 (robust SE)", cov="HC1"))
Mc = M.dropna(subset=["artificial", "dome"])
models.append(ols("adj ~ artificial + dome + mlb_cfg + cold + windy + snow + rain + cold_x_warmvisitor + pl + yr10 + C(shape_c, Treatment('FB'))", Mc,
                  "Venue & weather model, 1966-2026"))
A_ = H[H.attendance.notna()].copy(); A_["att10k"] = A_.attendance / 10000; A_["yr10"] = (A_.season - 2000) / 10
models.append(ols("adj ~ att10k + yr10", A_, "Attendance (per 10,000 fans), 2000-2019"))
Dd = H[H["div"].notna()].copy(); Dd["yr10"] = (Dd.season - 2000) / 10
Dd = Dd.rename(columns={"div": "divgame"}); models.append(ols("adj ~ divgame + yr10", Dd, "Divisional games, 1999-2026"))
Sp = H[H.spread.notna()].copy()
models.append(ols("margin ~ spread", Sp, "Vegas: margin on closing spread, 1999-2026"))
res["models"] = models
res["spread_mean"] = round(float(Sp[Sp.playoff == 0].spread.mean()), 3)
res["spread_by_season"] = [dict(season=int(k), spread=round(float(v), 3)) for k, v in Sp[Sp.playoff == 0].groupby("season").spread.mean().items()]

# franchise home/away records
fr_rows = []
for fr in meta.FRANCHISES:
    hx = H[H.home == fr]; ax = H[H.away == fr]
    if len(hx) == 0: continue
    fr_rows.append(dict(fr=fr, name=meta.FRANCHISES[fr][-1][2], first=int(min(hx.season.min(), ax.season.min())),
                        home_n=len(hx), home_win=round(hx.hwin.mean(), 4), away_n=len(ax), away_win=round(1 - ax.hwin.mean(), 4),
                        home_adj=round(hx.adj.mean(), 2), away_adj=round(-ax.adj.mean(), 2),
                        history=[dict(a=a, b=min(b, 2026), name=nm_, city=c) for a, b, nm_, c in meta.FRANCHISES[fr]]))
res["franchises"] = fr_rows

# venue records
vrows = []
for v, x in H[H.venue.notna() & (H.venue != "INTL")].groupby("venue"):
    vv = meta.V[v]
    tenants = sorted(set(meta.team_name(h, s_)[0] for h, s_ in zip(x.home, x.season)))
    vrows.append(dict(id=v, name=vv["name"], city=vv["city"], shape=meta.SHAPE_LABEL[vv["shape"]], roof=vv["roof"], cap=vv["cap"],
                      surface="; ".join(f"{a if a > 1900 else ''}-{b if b < 2099 else ''} {s_}" if len(vv["surface"]) > 1 else s_ for a, b, s_ in vv["surface"]),
                      mlb=f"{vv['mlb'][0]} ({vv['mlb'][1]}-{vv['mlb'][2] if vv['mlb'][2] < 2099 else 'now'})" if vv["mlb"] else "",
                      note=vv["note"], first=int(x.season.min()), last=int(x.season.max()), n=len(x),
                      win=round(x.hwin.mean(), 4), adj=round(x.adj.mean(), 2), tenants=tenants))
res["venues"] = sorted(vrows, key=lambda r: r["first"])
res["ratings_n"] = len(ratings)
res["built"] = "2026-10-27"
res["last_game"] = str(g.date.max().date())
json.dump(res, open(OUT + "results.json", "w"), default=float)

# compact game table for the browser
cols = ["season", "date", "week", "home", "away", "home_name", "away_name", "hs", "as_", "neutral", "playoff", "league",
        "venue_name", "shape", "surface", "roof", "mlb_shared", "mlb_inseason", "temp", "wind", "precip", "attendance",
        "spread", "div", "strength_diff", "adj", "away_warm", "espn"]
c = g[cols].copy()
c["date"] = c.date.dt.strftime("%Y-%m-%d")
for k in ["temp", "wind", "attendance", "spread", "week", "div", "away_warm"]:
    c[k] = c[k].astype(float).round(0)
c["strength_diff"] = c.strength_diff.round(1); c["adj"] = c.adj.round(1)
c = c.astype(object).where(c.notna(), None)
json.dump(dict(cols=cols, rows=c.values.tolist()), open(OUT + "games.json", "w"), separators=(",", ":"), default=str)
print(json.dumps({k: res[k] for k in ["overall", "overall_modern", "neutral", "binom_p", "last_game"]}, indent=1))
for m_ in models:
    print("\n" + m_["label"], m_["n"])
    for t in m_["terms"]: print(f"  {t['term']:<45} {t['b']:>8} ({t['se']})  p={t['p']:.3g}")
