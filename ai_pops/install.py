#!/usr/bin/env python3
"""
AI Pops Installation Script - Windows Friendly
This script helps install AI Pops with Windows compatibility fixes.
"""

import os
import sys
import subprocess
import platform

def run_command(cmd, description):
    """Run a command and handle errors gracefully."""
    print(f"\n🔧 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version < (3, 10) or version >= (3, 14):
        print(f"❌ Python {version.major}.{version.minor} is not supported")
        print("Please install Python 3.10, 3.11, 3.12, or 3.13")
        return False
    else:
        print(f"✅ Python {version.major}.{version.minor} is compatible")
        return True

def check_openai_key():
    """Check if OpenAI API key is set."""
    if os.getenv("OPENAI_API_KEY"):
        print("✅ OPENAI_API_KEY found in environment")
        return True
    else:
        print("⚠️  OPENAI_API_KEY not found")
        print("Please set your OpenAI API key:")
        print("1. Create a .env file in this directory")
        print("2. Add: OPENAI_API_KEY=your_api_key_here")
        return False

def main():
    """Main installation process."""
    print("🤖 AI Pops Installation Script")
    print("===============================")
    
    # Check system compatibility
    print(f"🖥️  Platform: {platform.system()} {platform.release()}")
    
    if not check_python_version():
        return False
    
    # Try different installation methods
    print("\n📦 Installing dependencies...")
    
    # Method 1: Try uv sync (fastest)
    if run_command("uv sync", "Installing with uv"):
        print("✅ Installation successful with uv!")
    else:
        print("⚠️  uv sync failed, trying pip...")
        
        # Method 2: Try pip install
        pip_packages = [
            "crewai>=0.152.0,<1.0.0",
            "fastapi>=0.104.0",
            "uvicorn[standard]>=0.24.0", 
            "openai>=1.12.0",
            "python-dotenv>=1.0.0",
            "pydantic>=2.5.0",
            "python-multipart>=0.0.6",
            "requests>=2.31.0"
        ]
        
        for package in pip_packages:
            if not run_command(f"pip install {package}", f"Installing {package}"):
                print(f"❌ Failed to install {package}")
                print("\n🔧 If you see compilation errors, try:")
                print("1. Install Microsoft Visual C++ Build Tools")
                print("2. Or use conda: conda install -c conda-forge chromadb")
                return False
        
        print("✅ Installation successful with pip!")
    
    # Check environment
    check_openai_key()
    
    print("\n🎉 Installation Complete!")
    print("\n🚀 Next Steps:")
    print("1. Set your OPENAI_API_KEY in .env file")
    print("2. Start backend: python start_server.py")
    print("3. Start frontend: cd frontend && npm install && npm run dev")
    print("4. Open http://localhost:3000")
    
    return True

if __name__ == "__main__":
    main()