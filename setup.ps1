Write-Output("Deleting the old virtual environment...") | Out-Default
if (Test-Path .venv){
    Remove-Item -Recurse .venv
}
Write-Output("Creating the new virtual environment...") | Out-Default
python -m venv .venv
.venv\Scripts\Activate
Write-Output("Installing packages...") | Out-Default
python -m pip install -r requirements.txt