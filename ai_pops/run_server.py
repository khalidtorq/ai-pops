#!/usr/bin/env python3
"""Simple server startup script."""

import os
import sys
import subprocess
from pathlib import Path
from dotenv import load_dotenv

def main():
    """Start the FastAPI server."""
    
    # Get the directory of this script
    script_dir = Path(__file__).parent
    src_dir = script_dir / "src"
    
    # Load environment variables
    load_dotenv(script_dir / ".env")
    
    print("🚀 Starting AI Pops Simple Server...")
    print(f"📍 Server: http://localhost:8000")
    print(f"📖 API docs: http://localhost:8000/docs")
    print(f"🔑 OpenAI API Key: {'✅ Found' if os.getenv('OPENAI_API_KEY') else '❌ Missing'}")
    print()
    
    # Add src to Python path
    if src_dir.exists():
        sys.path.insert(0, str(src_dir))
    
    try:
        # Direct import and run
        from ai_pops.api.server import app
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
    except ImportError:
        # Fallback: use subprocess with PYTHONPATH
        env = os.environ.copy()
        env["PYTHONPATH"] = str(src_dir)
        
        cmd = [
            sys.executable, "-m", "uvicorn",
            "ai_pops.api.server:app",
            "--host", "0.0.0.0",
            "--port", "8000"
        ]
        
        subprocess.run(cmd, env=env, cwd=script_dir)
    except KeyboardInterrupt:
        print("\n👋 Server stopped")

if __name__ == "__main__":
    main()