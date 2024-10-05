#!/bin/bash
echo "Deleting the old virtual environment..."
if [ -d ".venv" ]; then
    rm -rf .venv
fi
echo "Creating the new virtual environment..."
python3 -m venv .venv
source .venv/bin/activate
echo "Installing packages..."
python3 -m pip install -r requirements.txt
