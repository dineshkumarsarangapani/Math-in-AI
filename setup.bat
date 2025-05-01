@echo off

REM Check if virtual environment already exists
if exist venv (
    echo Virtual environment already exists.
    echo To activate it, run: venv\Scripts\activate
) else (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created.
    echo Activating virtual environment...
    call venv\Scripts\activate
    echo Installing dependencies...
    pip install -r requirement.txt
    echo Setup complete!
    echo To activate the environment next time, run: venv\Scripts\activate
) 