#!/usr/bin/env python3
"""
WSGI configuration for Apache mod_wsgi
This file allows deployment on traditional Apache hosting
"""

import os
import sys

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import the Flask application
from app import app as application

if __name__ == "__main__":
    # For development
    application.run(host='0.0.0.0', port=5000, debug=False)