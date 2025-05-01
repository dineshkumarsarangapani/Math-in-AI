#!/bin/bash

# Check if virtual environment already exists
if [ -d "venv" ]; then
    echo "Virtual environment already exists."
    echo "To activate it, run: source venv/bin/activate"
else
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created."
    echo "Activating virtual environment..."
    source venv/bin/activate
    echo "Installing dependencies..."
    pip install -r requirement.txt
    echo "Setup complete!"
    echo "To activate the environment next time, run: source venv/bin/activate"
fi 