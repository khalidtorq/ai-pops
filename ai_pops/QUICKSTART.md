# 🚀 Quick Start Guide

Get AI Pops running in under 5 minutes!

## ⚡ Prerequisites

- Python 3.10+ installed
- Node.js 18+ installed  
- OpenAI API key

## 🔧 Setup (Windows-Friendly)

### Option 1: Automated Installation (Recommended)

```bash
# Navigate to the project
cd ai_pops

# Run the installation script
python install.py

# Follow the prompts and troubleshooting suggestions
```

### Option 2: Manual Installation

```bash
# 1. Setup environment
cp .env.example .env
# Edit .env and add: OPENAI_API_KEY=your_api_key_here

# 2. Install backend dependencies (choose one)
# Option A: With uv (faster)
pip install uv
uv sync

# Option B: With pip (if uv fails)
pip install crewai fastapi uvicorn openai python-dotenv pydantic python-multipart requests

# 3. Install frontend dependencies
cd frontend
npm install
cd ..
```

### Option 3: If Build Errors Occur

If you see "Microsoft Visual C++ 14.0 required" errors:

**Solution A - Install Build Tools:**
1. Download **Build Tools for Visual Studio 2022** from:
   https://visualstudio.microsoft.com/downloads/
2. Install with "C++ build tools" selected
3. Restart terminal and try again

**Solution B - Use Conda:**
```bash
conda create -n ai_pops python=3.12
conda activate ai_pops
conda install -c conda-forge chromadb
pip install crewai fastapi uvicorn openai python-dotenv pydantic
```

## 🚀 Start the Application

### Backend (Choose one method):

**Method 1 - Development Setup (Recommended):**
```bash
# Install package in development mode first
python setup_dev.py

# Then start server
python start_server.py
```

**Method 2 - Direct Run (If Method 1 fails):**
```bash
python run_server.py
```

**Method 3 - Manual (Alternative):**
```bash
# From the ai_pops directory
set PYTHONPATH=src
uvicorn ai_pops.api.server:app --reload
```

### Frontend:
```bash
# Terminal 2
cd frontend
npm install
npm run dev
```

## 🌐 Access

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 🎮 Usage

1. **Open** http://localhost:3000
2. **Check** API connection status (green dot = connected)
3. **Click** "Smart AI Allocation" to see AI matching in action
4. **Try** "Generate AI Developers" and "Generate AI Tickets" for fresh content
5. **Explore** the different tabs to see assignments, developers, and tickets

## 🔧 Troubleshooting

**API Not Connected?**
- Ensure backend is running on port 8000
- Check your OpenAI API key in `.env`
- Verify no firewall blocking localhost

**Need Help?**
- Check the full README.md for detailed instructions
- Verify environment variables are set correctly
- Ensure all dependencies are installed

---

**That's it! You're now running AI-powered developer matching! 🎉**