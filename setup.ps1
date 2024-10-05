if (Test-Path .venv){
    Remove-Item -Recurse .venv
}
python -m venv .venv
.venv\Scripts\Activate
python -m pip install -r requirements.txt