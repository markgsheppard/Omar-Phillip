# Does Home Field Still Matter?

An interactive explorer of NFL home-field advantage covering every game from 1920 through October 2026.

**Short answer:** yes, but less than it used to. Home teams have won 57.6% of 18,208 non-neutral games and outscore visitors by about 2.6 points after adjusting for team strength. The edge sat near 2.8 points from 1970 to 2009, has averaged about 2.0 since 2021, and nearly disappeared (+0.1) in 2020 when most stadiums were empty.

## Publish on GitHub Pages

1. Create a repository and upload everything in this folder (keep `index.html` at the root).
2. Settings → Pages → Source: *Deploy from a branch*, branch `main`, folder `/ (root)`.
3. The site appears at `https://<your-user>.github.io/<repo>/`.

`index.html` is self-contained (data embedded), so it also works opened straight from disk.

## Contents

- `index.html` — the dashboard
- `data/nfl_games_home_field.csv` — one row per game with venue, surface, roof, stadium type, MLB tenancy, weather, attendance (2000–2019), strength ratings and adjusted margin
- `data/results.json` — season, decade, franchise and venue summaries plus regression output
- `scripts/` — `build.py` (data assembly and analysis), `meta.py` (hand-compiled franchise and stadium history), `build_site.py`

## Sources

| Data | Link | Used for |
|---|---|---|
| FiveThirtyEight `nfl-elo-game` | https://github.com/fivethirtyeight/nfl-elo-game (file: https://github.com/fivethirtyeight/nfl-elo-game/blob/master/data/nfl_games.csv) | Every game 1920–1998 |
| nflverse `nfldata` schedules | https://github.com/nflverse/nfldata (file: https://github.com/nflverse/nfldata/blob/master/data/games.csv) | Every game 1999–2026; ESPN IDs, stadium, roof, surface, temperature, wind, spread |
| NFL scores and betting data ("spreadspoke"), Kaggle | https://www.kaggle.com/datasets/tobycrabtree/nfl-scores-and-betting-data (copy from https://github.com/lillyjob/nfl-spread-dashboard) | Stadium and kickoff weather 1966–2025 |
| TidyTuesday 2020-02-04 NFL attendance | https://github.com/rfordatascience/tidytuesday/tree/master/data/2020/2020-02-04 | Weekly attendance 2000–2019 |
| ESPN | https://www.espn.com/nfl/ | Game pages linked for 1999+ |
| Wikipedia stadium pages | https://en.wikipedia.org/wiki/Tulane_Stadium · https://en.wikipedia.org/wiki/FirstBank_Stadium · https://en.wikipedia.org/wiki/Robert_F._Kennedy_Memorial_Stadium | Surface-history checks |

Copies of the downloaded source files are in `data/raw/`. Team badges use official team colors only; no logos are reproduced.
