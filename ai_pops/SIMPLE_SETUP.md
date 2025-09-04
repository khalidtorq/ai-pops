# 🚀 Simple Setup - Get Running in 2 Minutes

## Step 1: Set up OpenAI API Key

Create a `.env` file in the `ai_pops` directory:

```bash
# Create .env file
echo "OPENAI_API_KEY=your_actual_api_key_here" > .env
```

## Step 2: Install Dependencies

```bash
# Simple pip install
pip install fastapi uvicorn openai python-dotenv pydantic requests
```

## Step 3: Start the Server

```bash
# Start the simple server
python run_server.py
```

You should see:
```
🚀 Starting AI Pops Simple Server...
📍 Server: http://localhost:8000
📖 API docs: http://localhost:8000/docs
🔑 OpenAI API Key: ✅ Found
```

## Step 4: Test the API

```bash
# Test all endpoints
python test_api.py
```

## Step 5: Start Frontend (Optional)

```bash
cd frontend
npm install
npm run dev
```

## 🌐 URLs

- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs  
- **Frontend**: http://localhost:3000

## 🔧 API Endpoints

- `GET /` - Health check
- `POST /api/match` - Match developers to tickets
- `POST /api/generate-developers?count=N` - Generate N developers
- `POST /api/generate-tickets?count=N` - Generate N tickets

## 🧪 Test with curl

```bash
# Health check
curl http://localhost:8000/

# Generate developers
curl -X POST http://localhost:8000/api/generate-developers?count=3

# Generate tickets  
curl -X POST http://localhost:8000/api/generate-tickets?count=3
```

That's it! Simple and working! 🎉