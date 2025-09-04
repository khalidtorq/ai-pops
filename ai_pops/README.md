# 🤖 AI Pops - Intelligent Developer-Ticket Matching System

AI Pops is a modern, AI-powered application that intelligently matches developers to tickets using OpenAI's advanced language models. It combines a powerful CrewAI backend with a sleek Next.js frontend to deliver smart resource allocation and team assignment management.

## 🚀 Features

### 🎯 **AI-Powered Matching**
- **Smart Allocation**: Uses OpenAI to analyze developer skills, experience, and ticket requirements for optimal matching
- **Dynamic Reasoning**: Provides detailed explanations for each assignment decision
- **Match Scoring**: Confidence scores from 0-100 for each assignment

### 🔄 **AI Content Generation**
- **Developer Profiles**: Generate realistic developer profiles with diverse skills and backgrounds
- **Ticket Creation**: Create realistic work tickets across various domains (frontend, backend, DevOps, etc.)
- **Dynamic Content**: All content is AI-generated, no hardcoded values

### 🖥️ **Modern Web Interface**
- **Real-time Updates**: Live API connection status and error handling
- **Interactive Dashboard**: View teams, tickets, and assignments in organized tabs
- **Manual Override**: Manual assignment capability alongside AI recommendations

### 🛠️ **Powerful Backend**
- **FastAPI Server**: High-performance async API with automatic documentation
- **CrewAI Integration**: Multi-agent AI system for complex task orchestration
- **OpenAI Integration**: Latest GPT models for intelligent analysis

## 📋 Prerequisites

- **Python**: 3.10 or higher (< 3.14)
- **Node.js**: 18.0 or higher
- **OpenAI API Key**: Required for AI functionality

## 🔧 Installation & Setup

### 1. **Environment Setup**

Create a `.env` file in the root directory:

```bash
# Copy the example file
cp .env.example .env

# Edit with your OpenAI API key
OPENAI_API_KEY=your_openai_api_key_here
```

### 2. **Backend Setup**

```bash
# Install UV (if not already installed)
pip install uv

# Install Python dependencies
cd ai_pops
uv sync

# Or alternatively using crewai
crewai install
```

### 3. **Frontend Setup**

```bash
# Navigate to frontend directory
cd frontend

# Install Node.js dependencies
npm install

# Or using yarn
yarn install
```

## 🚀 Running the Application

### **Option 1: Full Stack Development**

**Terminal 1 - Backend Server:**
```bash
cd ai_pops
python start_server.py
```

**Terminal 2 - Frontend Development:**
```bash
cd frontend
npm run dev
```

### **Option 2: Production Mode**

**Backend:**
```bash
cd ai_pops
uvicorn ai_pops.api.server:app --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
cd frontend
npm run build
npm start
```

### 🌐 **Access Points**

- **Frontend Application**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **API Health Check**: http://localhost:8000

## 🏗️ Architecture Overview

```
AI Pops Application
├── Frontend (Next.js + React)
│   ├── Modern UI with Tailwind CSS
│   ├── Real-time API integration
│   └── Interactive assignment management
│
├── Backend API (FastAPI)
│   ├── RESTful API endpoints
│   ├── OpenAI service integration
│   └── Async request handling
│
├── AI Services (OpenAI)
│   ├── Developer-ticket matching
│   ├── Content generation
│   └── Intelligent reasoning
│
└── CrewAI Integration
    ├── Multi-agent orchestration
    ├── Research and reporting agents
    └── Extensible task framework
```

## 📚 API Endpoints

### **Core Endpoints**

- `GET /` - Health check
- `POST /api/match` - Match developers to tickets using AI
- `POST /api/generate-developers?count=N` - Generate N AI developer profiles
- `POST /api/generate-tickets?count=N` - Generate N AI tickets

### **Example Usage**

```python
import requests

# Match developers to tickets
response = requests.post('http://localhost:8000/api/match', json={
    'developers': [...],  # List of developer objects
    'tickets': [...]      # List of ticket objects
})

assignments = response.json()
```

## 🔨 Development

### **Project Structure**

```
ai_pops/
├── src/ai_pops/              # Backend source code
│   ├── api/                  # FastAPI application
│   │   ├── server.py         # Main server file
│   │   └── models.py         # Pydantic models
│   ├── services/             # Business logic
│   │   └── matching_service.py  # OpenAI integration
│   ├── crew.py               # CrewAI configuration
│   └── main.py               # CLI entry points
├── frontend/                 # Next.js frontend
│   ├── app/                  # App router pages
│   ├── components/           # React components
│   ├── utils/                # Utility functions
│   ├── data/                 # Initial data
│   └── types/                # TypeScript definitions
└── start_server.py           # Development server script
```

### **Adding New Features**

1. **Backend**: Add new endpoints in `api/server.py`
2. **AI Services**: Extend `services/matching_service.py`
3. **Frontend**: Create components in `components/`
4. **Types**: Update TypeScript types in `types/`

## 🧪 CrewAI Integration

The application includes a full CrewAI setup for advanced AI agent orchestration:

```bash
# Run the research crew
crewai run

# Train the crew
crewai train

# Test crew performance
crewai test
```

**Available Agents:**
- **Researcher**: Gathers cutting-edge information
- **Reporting Analyst**: Creates detailed analysis reports

## 🔧 Configuration

### **Environment Variables**

**Backend (.env):**
```bash
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4o-mini
API_HOST=0.0.0.0
API_PORT=8000
FRONTEND_URL=http://localhost:3000
```

**Frontend (.env.local):**
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### **Customization**

- **Agent Configuration**: `src/ai_pops/config/agents.yaml`
- **Task Definitions**: `src/ai_pops/config/tasks.yaml`
- **UI Components**: `frontend/components/`
- **API Models**: `src/ai_pops/api/models.py`

## 🚨 Troubleshooting

### **Common Issues**

1. **API Connection Failed**
   - Verify backend server is running on port 8000
   - Check OPENAI_API_KEY is set correctly
   - Ensure no firewall blocking localhost:8000

2. **OpenAI API Errors**
   - Verify API key is valid and has credits
   - Check rate limits if getting 429 errors
   - Ensure gpt-4o-mini model access

3. **Frontend Build Issues**
   - Run `npm install` to ensure all dependencies
   - Check Node.js version compatibility
   - Clear `.next` cache if needed

### **Debug Mode**

Enable verbose logging:
```bash
# Backend
uvicorn ai_pops.api.server:app --log-level debug

# Frontend  
npm run dev -- --debug
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For support, questions, or feedback:
- **CrewAI Documentation**: [docs.crewai.com](https://docs.crewai.com)
- **OpenAI API Docs**: [platform.openai.com](https://platform.openai.com/docs)
- **Next.js Documentation**: [nextjs.org/docs](https://nextjs.org/docs)

---

**Built with ❤️ using CrewAI, OpenAI, FastAPI, and Next.js**
