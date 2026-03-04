# Start the service in development mode (Windows PowerShell)
# Usage: .\dev_start.ps1

$Env:ENV = "dev"
python .\run.py
