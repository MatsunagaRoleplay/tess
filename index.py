#!/usr/bin/env python3
"""
Alternative entry point for hosting platforms that expect index.py
This file ensures compatibility with various hosting providers
"""

import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import the Flask application
from app import app

# For CGI hosting
if __name__ == "__main__":
    print("Content-Type: text/html\n")
    from wsgiref.handlers import CGIHandler
    CGIHandler().run(app)
else:
    # For WSGI hosting
    application = app