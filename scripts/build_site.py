import json, shutil, os
t = open("/root/nfl/site/template.html").read()
res = open("/root/nfl/out/results.json").read().replace("</", "<\\/")
gam = open("/root/nfl/out/games.json").read().replace("</", "<\\/")
page = t.replace("__RESULTS__", res).replace("__GAMES__", gam)
open("/root/nfl/site/nfl-home-field.html", "w").write(page)
gh = "/root/nfl/gh-pages"; os.makedirs(gh + "/data", exist_ok=True); os.makedirs(gh + "/scripts", exist_ok=True)
head = '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<style>:root{padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n</head>\n<body>\n'
open(gh + "/index.html", "w").write(head + page + "\n</body>\n</html>\n")
shutil.copy("/root/nfl/out/games_full.csv", gh + "/data/nfl_games_home_field.csv")
shutil.copy("/root/nfl/out/results.json", gh + "/data/results.json")
for f in ["meta.py", "build.py", "build_site.py"]: shutil.copy("/root/nfl/scripts/" + f, gh + "/scripts/" + f)
open(gh + "/.nojekyll", "w").write("")
print(len(page)/1e6, "MB")
