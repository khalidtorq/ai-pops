#!/usr/bin/env python3
"""Test script to verify the API is working."""

import requests
import json
import time

def test_api():
    """Test all API endpoints."""
    base_url = "http://localhost:8000"
    
    print("🧪 Testing AI Pops API...")
    
    # Test 1: Health check
    print("\n1. Testing health check...")
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            print("✅ Health check passed")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return
    except Exception as e:
        print(f"❌ Cannot connect to server: {e}")
        print("   Make sure the server is running: python run_server.py")
        return
    
    # Test 2: Generate developers
    print("\n2. Testing developer generation...")
    try:
        response = requests.post(f"{base_url}/api/generate-developers?count=3")
        if response.status_code == 200:
            developers = response.json()
            print(f"✅ Generated {len(developers)} developers")
            print(f"   Sample: {developers[0]['name']}")
        else:
            print(f"❌ Developer generation failed: {response.status_code}")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Developer generation error: {e}")
    
    # Test 3: Generate tickets
    print("\n3. Testing ticket generation...")
    try:
        response = requests.post(f"{base_url}/api/generate-tickets?count=3")
        if response.status_code == 200:
            tickets = response.json()
            print(f"✅ Generated {len(tickets)} tickets")
            print(f"   Sample: {tickets[0]['title']}")
        else:
            print(f"❌ Ticket generation failed: {response.status_code}")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Ticket generation error: {e}")
    
    # Test 4: Matching
    print("\n4. Testing developer-ticket matching...")
    try:
        # Sample data for testing
        test_data = {
            "developers": [
                {
                    "name": "Alice Smith",
                    "skills": ["Python", "React", "JavaScript"],
                    "experience_years": 5,
                    "profile_summary": "Full-stack developer"
                },
                {
                    "name": "Bob Johnson", 
                    "skills": ["Java", "Spring", "MySQL"],
                    "experience_years": 3,
                    "profile_summary": "Backend developer"
                }
            ],
            "tickets": [
                {
                    "id": "T001",
                    "title": "Frontend React component",
                    "description": "Build a React component for user dashboard"
                },
                {
                    "id": "T002",
                    "title": "Backend API endpoint",
                    "description": "Create REST API for user management"
                }
            ]
        }
        
        response = requests.post(
            f"{base_url}/api/match",
            json=test_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            assignments = response.json()
            print(f"✅ Generated {len(assignments)} assignments")
            for assignment in assignments:
                print(f"   {assignment['ticketId']} → {assignment['developerName']}")
        else:
            print(f"❌ Matching failed: {response.status_code}")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Matching error: {e}")
    
    print("\n🎉 API testing complete!")
    print("   You can now open http://localhost:3000 for the frontend")

if __name__ == "__main__":
    test_api()