#!/usr/bin/env python3
"""Setup script for development installation."""

import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return False

def main():
    """Install the package in development mode."""
    print("🚀 Setting up AI Pops for development...")
    
    # Check if we're in the right directory
    if not Path("pyproject.toml").exists():
        print("❌ pyproject.toml not found. Please run this from the ai_pops directory.")
        return False
    
    # Install in development mode
    print("\n📦 Installing package in development mode...")
    
    # Try different installation methods
    methods = [
        ("pip install -e .", "Installing with pip in editable mode"),
        ("python -m pip install -e .", "Installing with python -m pip in editable mode"),
    ]
    
    for cmd, desc in methods:
        if run_command(cmd, desc):
            print("✅ Development installation successful!")
            print("\n🎉 You can now run:")
            print("python start_server.py")
            print("OR")
            print("uvicorn ai_pops.api.server:app --reload")
            return True
    
    print("❌ Development installation failed")
    print("🔧 Try running manually:")
    print("python run_server.py")
    return False

if __name__ == "__main__":
    main()