steps to run
python -m venv .venv
source .venv/bin/activate

superuser for minimud
markar
werty678

\\wsl.localhost\Ubuntu\home\mark\home\muddev\evennia-minimud\server

# Delete the current combat script, freeing up related variables
- py here.scripts.get('combat').delete()
>>> here.scripts.get('combat').delete()
(1, {'scripts.CombatScript': 1})