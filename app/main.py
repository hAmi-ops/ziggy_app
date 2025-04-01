from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Ziggy - AI Social Media Assistant",
    description="An AI-powered assistant for managing and optimizing your social media presence",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

class SocialMediaPost(BaseModel):
    platform: str
    content: str
    scheduled_time: Optional[str] = None

class PostResponse(BaseModel):
    post_id: str
    platform: str
    content: str
    status: str

class HashtagResponse(BaseModel):
    hashtags: List[str]
    explanation: str

class CommentRequest(BaseModel):
    comment: str
    tone: str
    platform: str = "general"

class CommentResponse(BaseModel):
    response: str
    explanation: str

@app.get("/")
async def root():
    return {"message": "Welcome to Ziggy - Your AI Social Media Assistant"}

@app.post("/api/generate-post", response_model=PostResponse)
async def generate_post(platform: str, topic: str):
    try:
        # Generate content using OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are Ziggy, an expert social media assistant for {platform}."},
                {"role": "user", "content": f"Create an engaging post about {topic} for {platform}"}
            ]
        )
        
        generated_content = response.choices[0].message.content
        
        return PostResponse(
            post_id="temp_id",  # In production, generate a proper ID
            platform=platform,
            content=generated_content,
            status="generated"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/generate-hashtags", response_model=HashtagResponse)
async def generate_hashtags(topic: str, platform: str = "instagram"):
    try:
        # Generate hashtags using OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are Ziggy's Hashtag Wizard, an expert at finding relevant and trending hashtags for {platform}."},
                {"role": "user", "content": f"Generate 10 relevant and trending hashtags for the topic: {topic}. Include a brief explanation of why these hashtags are relevant."}
            ]
        )
        
        # Parse the response to separate hashtags and explanation
        content = response.choices[0].message.content
        hashtags = [tag.strip() for tag in content.split('\n') if tag.strip().startswith('#')]
        explanation = content.split('\n')[-1] if not content.split('\n')[-1].startswith('#') else ""
        
        return HashtagResponse(
            hashtags=hashtags,
            explanation=explanation
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/generate-comment-response", response_model=CommentResponse)
async def generate_comment_response(request: CommentRequest):
    try:
        # Generate comment response using OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are Ziggy's Comment Assistant, an expert at crafting {request.tone} responses for {request.platform}."},
                {"role": "user", "content": f"Generate a {request.tone} response to this comment: '{request.comment}'. Include a brief explanation of why this response is appropriate."}
            ]
        )
        
        # Parse the response to separate the response and explanation
        content = response.choices[0].message.content
        response_lines = content.split('\n')
        generated_response = response_lines[0]
        explanation = response_lines[-1] if len(response_lines) > 1 else ""
        
        return CommentResponse(
            response=generated_response,
            explanation=explanation
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/schedule-post", response_model=PostResponse)
async def schedule_post(post: SocialMediaPost):
    # TODO: Implement post scheduling logic
    return PostResponse(
        post_id="temp_id",
        platform=post.platform,
        content=post.content,
        status="scheduled"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 