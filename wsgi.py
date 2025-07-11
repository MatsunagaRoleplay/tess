#!/usr/bin/env python3
"""
WSGI configuration for web hosting compatibility
This file allows the Flask app to run on any WSGI-compatible web hosting service
"""

import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import the Flask application
from app import app

# Standard WSGI application callable
application = app

if __name__ == "__main__":
    # For development
    app.run(host='0.0.0.0', port=5000, debug=True)