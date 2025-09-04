"""Simple FastAPI server for AI Pops."""

import os
import json
from typing import List, Dict, Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="AI Pops API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client
openai_client = None
if os.getenv("OPENAI_API_KEY"):
    openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Simple models
class Developer(BaseModel):
    name: str
    skills: List[str]
    experience_years: int
    profile_summary: str

class Ticket(BaseModel):
    id: str
    title: str
    description: str

class Assignment(BaseModel):
    ticketId: str
    developerName: str
    reason: str
    matchScore: float

class MatchRequest(BaseModel):
    developers: List[Developer]
    tickets: List[Ticket]

@app.get("/")
def root():
    """Health check."""
    return {
        "message": "AI Pops API is running", 
        "openai_configured": openai_client is not None
    }

@app.post("/api/match")
def match_developers_to_tickets(request: MatchRequest):
    """Match developers to tickets."""
    if not openai_client:
        raise HTTPException(status_code=500, detail="OpenAI API key not configured")
    
    try:
        # Simple matching prompt
        prompt = f"""
        Match these developers to tickets. Return JSON array only:
        
        DEVELOPERS: {json.dumps([d.model_dump() for d in request.developers])}
        TICKETS: {json.dumps([t.model_dump() for t in request.tickets])}
        
        Return format:
        [
            {{
                "ticketId": "ticket_id",
                "developerName": "Developer Name",
                "reason": "Why this match makes sense",
                "matchScore": 85.5
            }}
        ]
        """
        
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=2000
        )
        
        result_text = response.choices[0].message.content
        # Clean up the response to extract JSON
        if "```json" in result_text:
            result_text = result_text.split("```json")[1].split("```")[0]
        elif "```" in result_text:
            result_text = result_text.split("```")[1].split("```")[0]
        
        assignments = json.loads(result_text.strip())
        return assignments
        
    except Exception as e:
        # Fallback: simple rule-based matching
        assignments = []
        for i, ticket in enumerate(request.tickets[:len(request.developers)]):
            dev = request.developers[i]
            assignments.append({
                "ticketId": ticket.id,
                "developerName": dev.name,
                "reason": f"Matched based on {dev.experience_years} years experience",
                "matchScore": 75.0
            })
        return assignments

@app.post("/api/generate-developers")
def generate_developers(count: int = 10):
    """Generate developer profiles."""
    if not openai_client:
        # Fallback data
        return [
            {
                "name": f"Developer {i+1}",
                "skills": ["Python", "React", "JavaScript"],
                "experience_years": 3 + (i % 8),
                "profile_summary": f"Software developer with {3 + (i % 8)} years experience"
            }
            for i in range(count)
        ]
    
    try:
        prompt = f"""
        Generate {count} realistic software developer profiles. Return JSON array only:
        [
            {{
                "name": "Full Name",
                "skills": ["skill1", "skill2", "skill3"],
                "experience_years": 5,
                "profile_summary": "Brief summary"
            }}
        ]
        """
        
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            max_tokens=2000
        )
        
        result_text = response.choices[0].message.content
        if "```json" in result_text:
            result_text = result_text.split("```json")[1].split("```")[0]
        elif "```" in result_text:
            result_text = result_text.split("```")[1].split("```")[0]
        
        return json.loads(result_text.strip())
        
    except Exception as e:
        # Fallback
        return [{"name": f"Dev {i}", "skills": ["Python"], "experience_years": 3, "profile_summary": "Developer"} for i in range(count)]

@app.post("/api/generate-tickets")
def generate_tickets(count: int = 10):
    """Generate tickets."""
    if not openai_client:
        # Fallback data
        return [
            {
                "id": f"TASK-{i+1:03d}",
                "title": f"Sample Task {i+1}",
                "description": f"This is a sample development task number {i+1}"
            }
            for i in range(count)
        ]
    
    try:
        prompt = f"""
        Generate {count} realistic software development tickets. Return JSON array only:
        [
            {{
                "id": "TASK-001",
                "title": "Task title",
                "description": "Detailed description"
            }}
        ]
        """
        
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=2000
        )
        
        result_text = response.choices[0].message.content
        if "```json" in result_text:
            result_text = result_text.split("```json")[1].split("```")[0]
        elif "```" in result_text:
            result_text = result_text.split("```")[1].split("```")[0]
        
        return json.loads(result_text.strip())
        
    except Exception as e:
        # Fallback
        return [{"id": f"T{i}", "title": f"Task {i}", "description": "Sample task"} for i in range(count)]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)