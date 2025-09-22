## Django Practice #2 + Git Basics (Windows/PowerShell)

### Quick start
- **Activate venv** (from repo root `C:\Users\alan\Desktop\djangorlal`):
```powershell
./venv/Scripts/Activate.ps1
```
- **Run the project** (the Django project root is `practice\myapp`):
```powershell
cd practice/myapp
python manage.py migrate
python manage.py runserver
```
- Open: `http://127.0.0.1:8000/`

### Project layout
- **Repo root**: `C:\Users\alan\Desktop\djangorlal`
- **Virtual env**: `venv/`
- **Django project root**: `practice\myapp`
- **Settings file**: `practice\myapp\myapp\settings.py`
- **SQLite DB**: `practice\myapp\db.sqlite3`

### Common Django commands
```powershell
# From repo root
./venv/Scripts/Activate.ps1
cd practice/myapp

# Migrations
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run development server
python manage.py runserver              # 127.0.0.1:8000
# python manage.py runserver 0.0.0.0:8000  # LAN (update ALLOWED_HOSTS)

# Create a new app
python manage.py startapp <app_name>

# Open Django shell
python manage.py shell
```

### Git basics (PowerShell)
```powershell
# One-time setup (inside repo)
git init -b main
git config user.name "Your Name"
git config user.email "you@example.com"

# See status and changes
git status | cat
git diff | cat

# Stage and commit
git add -A
git commit -m "Your message"

# Branching
git switch -c feature/my-change
git switch main
git merge feature/my-change

# Remote
git remote add origin https://github.com/<you>/<repo>.git
git push -u origin main
git pull --rebase origin main

# Undo helpers
git restore --staged <path>   # unstage
git restore <path>            # discard local file changes
git revert <commit>           # new commit that reverts
git reset --hard HEAD~1       # hard reset (careful)
git stash -u && git stash pop # quick stash
```

### Useful tips
- **Execution policy**: if activation is blocked, run PowerShell as Admin once:
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned -Force
```
- **Allowed hosts**: edit `ALLOWED_HOSTS` in `practice\myapp\myapp\settings.py` when serving on LAN/other hosts.
- **.gitignore essentials** (already typical for Python/Django):
```gitignore
venv/
__pycache__/
*.pyc
db.sqlite3
.env
```

### Troubleshooting
- Port in use: change port with `python manage.py runserver 8001`.
- Wrong Python: ensure venv is active (`(venv)` prompt) before running commands.