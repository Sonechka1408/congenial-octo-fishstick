#!/usr/bin/env python3
"""
Test script for Webmaster API endpoints
"""

import requests
import json
import time

BASE_URL = "http://localhost:5000"

def test_health():
    """Test health endpoint"""
    print("🔄 Testing health endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health check passed: {data['status']}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False

def test_form_submission():
    """Test form submission endpoint"""
    print("🔄 Testing form submission...")
    
    test_data = {
        "name": "Test User",
        "email": "test@example.com",
        "phone": "+1234567890",
        "form_type": "price_calculator",
        "message": "This is a test submission"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/submit-form",
            json=test_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print("✅ Form submission successful")
                return True
            else:
                print(f"❌ Form submission failed: {data.get('error', 'Unknown error')}")
                return False
        else:
            print(f"❌ Form submission failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Form submission error: {e}")
        return False

def test_users_endpoint():
    """Test users endpoint"""
    print("🔄 Testing users endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/users")
        if response.status_code == 200:
            data = response.json()
            users = data.get('users', [])
            print(f"✅ Users endpoint successful: {len(users)} users found")
            return True
        else:
            print(f"❌ Users endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Users endpoint error: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Webmaster API endpoints...")
    print("=" * 50)
    
    # Wait a moment for server to start
    print("⏳ Waiting for server to be ready...")
    time.sleep(2)
    
    tests = [
        ("Health Check", test_health),
        ("Form Submission", test_form_submission),
        ("Users Endpoint", test_users_endpoint)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📋 Running {test_name}...")
        if test_func():
            passed += 1
        print("-" * 30)
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("❌ Some tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())
