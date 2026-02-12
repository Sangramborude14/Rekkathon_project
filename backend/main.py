"""
GenomeGuard API - Main FastAPI application
"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create app
app = FastAPI(
    title="GenomeGuard API",
    version="1.0.0",
    description="AI-Powered Genetic Disease Predictor",
    docs_url="/docs",
    openapi_url="/openapi.json"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import routers
try:
    from backend.api.auth import router as auth_router
    from backend.api.analysis import router as analysis_router
    
    # Include routers
    app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
    app.include_router(analysis_router, prefix="/analysis", tags=["Analysis"])
    logger.info("✅ Successfully loaded API routers")
except ImportError as e:
    logger.warning(f"⚠️  Could not load API routers: {e}")
    logger.info("Using default routes...")

# Default routes
@app.get("/")
async def root():
    return {
        "message": "GenomeGuard API",
        "status": "running",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": str(__import__('datetime').datetime.now())
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("API_PORT", 8000))
    host = os.getenv("API_HOST", "0.0.0.0")
    
    logger.info(f"🚀 Starting GenomeGuard API on {host}:{port}")
    uvicorn.run(
        "backend.main:app",
        host=host,
        port=port,
        reload=os.getenv("API_RELOAD", "true").lower() == "true"
    )
