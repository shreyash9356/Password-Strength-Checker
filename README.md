# Password Strength Checker (Flask web)

## Quick start

1) Create/activate a virtual environment (recommended).

```bash
python -m venv .venv
# Windows PowerShell
. .venv\\Scripts\\Activate.ps1
```

2) Install dependencies:

```bash
pip install -r requirements.txt
```

3) Run the app:

```bash
python app.py
```

4) Open in your browser:

- http://127.0.0.1:5000/

## API

- POST `/check`
  - JSON: `{ "password": "..." }`
  - Response: `{ "strength": "Weak|Medium|Strong|Weak (Too short)" }`

The browser UI uses this endpoint via `fetch()`.

