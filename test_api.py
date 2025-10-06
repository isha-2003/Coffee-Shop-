#!/usr/bin/env python3
"""
Simple test script for Coffee Shop API
"""
import requests
import json

BASE_URL = 'http://localhost:5000'

def test_public_endpoint():
    """Test the public drinks endpoint"""
    try:
        response = requests.get(f'{BASE_URL}/drinks')
        print(f"GET /drinks - Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error testing public endpoint: {e}")
        return False

def test_root_endpoint():
    """Test the root endpoint"""
    try:
        response = requests.get(f'{BASE_URL}/')
        print(f"GET / - Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error testing root endpoint: {e}")
        return False

def test_protected_endpoint_without_auth():
    """Test protected endpoint without authentication"""
    try:
        response = requests.get(f'{BASE_URL}/drinks-detail')
        print(f"GET /drinks-detail (no auth) - Status: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 401
    except Exception as e:
        print(f"Error testing protected endpoint: {e}")
        return False

if __name__ == '__main__':
    print("Testing Coffee Shop API...")
    print("=" * 50)
    
    print("\n1. Testing root endpoint:")
    test_root_endpoint()
    
    print("\n2. Testing public drinks endpoint:")
    test_public_endpoint()
    
    print("\n3. Testing protected endpoint without auth:")
    test_protected_endpoint_without_auth()
    
    print("\n" + "=" * 50)
    print("Test completed. Make sure to run 'flask run --reload' in the src directory first!")