#!/usr/bin/env python3
"""
Passenger WSGI configuration for shared hosting (cPanel, Namecheap, etc.)
This file is specifically for hosting providers that use Passenger
"""

import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import the Flask application
from app import app

# Passenger requires the application to be named 'application'
application = app

if __name__ == "__main__":
    # For development
    app.run(host='0.0.0.0', port=5000, debug=False)