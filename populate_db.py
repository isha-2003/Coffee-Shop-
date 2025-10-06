#!/usr/bin/env python3
"""
Script to populate the database with sample drinks
"""
import os
import sys
import json

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.database.models import Drink, setup_db, db_drop_and_create_all
from flask import Flask

def create_sample_drinks():
    """Create sample drinks in the database"""
    
    # Sample drink recipes
    drinks_data = [
        {
            'title': 'Espresso',
            'recipe': [
                {
                    'name': 'Coffee',
                    'color': '#8B4513',
                    'parts': 1
                }
            ]
        },
        {
            'title': 'Cappuccino',
            'recipe': [
                {
                    'name': 'Coffee',
                    'color': '#8B4513',
                    'parts': 1
                },
                {
                    'name': 'Steamed Milk',
                    'color': '#FFFFFF',
                    'parts': 2
                }
            ]
        },
        {
            'title': 'Latte',
            'recipe': [
                {
                    'name': 'Coffee',
                    'color': '#8B4513',
                    'parts': 1
                },
                {
                    'name': 'Steamed Milk',
                    'color': '#FFFFFF',
                    'parts': 3
                }
            ]
        }
    ]
    
    # Create drinks
    for drink_data in drinks_data:
        drink = Drink(
            title=drink_data['title'],
            recipe=json.dumps(drink_data['recipe'])
        )
        drink.insert()
        print(f"Created drink: {drink_data['title']}")

if __name__ == '__main__':
    # Create Flask app and setup database
    app = Flask(__name__)
    setup_db(app)
    
    with app.app_context():
        print("Populating database with sample drinks...")
        create_sample_drinks()
        print("Database populated successfully!")