#!/bin/bash
# Simple script to run the Flask server

export FLASK_APP=main.py
export FLASK_ENV=development
export PYTHONPATH=$PYTHONPATH:$(pwd)

python main.py
