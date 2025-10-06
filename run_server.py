#!/usr/bin/env python3
"""
Flask application runner for Coffee Shop API
"""
import os
import sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.api import app

if __name__ == '__main__':
    # Set environment variables
    os.environ['FLASK_APP'] = 'api.py'
    os.environ['FLASK_ENV'] = 'development'
    
    print("Starting Coffee Shop API server...")
    print("Server will be available at: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)