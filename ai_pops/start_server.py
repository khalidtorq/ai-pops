#!/usr/bin/env python3
"""Startup script for the AI Pops backend server."""

import uvicorn
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add the src directory to Python path
current_dir = Path(__file__).parent
src_dir = current_dir / "src"
if src_dir.exists():
    sys.path.insert(0, str(src_dir))

# Load environment variables
load_dotenv()

def main():
    """Start the FastAPI server."""
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", "8000"))
    
    print(f"🚀 Starting AI Pops backend server...")
    print(f"📍 Server will be available at: http://{host}:{port}")
    print(f"📖 API docs will be available at: http://{host}:{port}/docs")
    print(f"🔑 OpenAI API Key: {'✅ Found' if os.getenv('OPENAI_API_KEY') else '❌ Missing'}")
    print()
    
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Warning: OPENAI_API_KEY environment variable is not set!")
        print("   Please set it in your .env file or environment.")
        print()
    
    uvicorn.run(
        "ai_pops.api.server:app",
        host=host,
        port=port,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main()