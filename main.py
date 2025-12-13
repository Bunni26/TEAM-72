"""FastAPI application entry point."""
import structlog
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.config import settings
from app.models.database import init_db
from app.api.chat import router as chat_router
from app.api.audit import router as audit_router
from app.api.ticket import router as ticket_router

# Configure structured logging
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.stdlib.BoundLogger,
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler."""
    # Startup
    logger.info("application_starting", app_name=settings.APP_NAME)
    
    # Initialize database
    await init_db()
    logger.info("database_initialized")
    
    # Initialize Sentry if configured
    if settings.SENTRY_DSN:
        import sentry_sdk
        sentry_sdk.init(
            dsn=settings.SENTRY_DSN,
            traces_sample_rate=0.1,
        )
        logger.info("sentry_initialized")
    
    yield
    
    # Shutdown
    logger.info("application_shutting_down")


# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="""
    AI-Powered Customer Support Automation System
    
    Features:
    - RAG-based knowledge retrieval
    - Intent classification and action detection
    - Ticket creation and escalation
    - Audit logging for all interactions
    - Conversation memory management
    """,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Handle uncaught exceptions."""
    logger.error(
        "unhandled_exception",
        error=str(exc),
        path=request.url.path,
        method=request.method
    )
    
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "detail": str(exc) if settings.DEBUG else "An unexpected error occurred"
        }
    )


# Include routers
app.include_router(chat_router, tags=["Chat"])
app.include_router(audit_router, tags=["Audit"])
app.include_router(ticket_router, tags=["Tickets"])


# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint for container orchestration."""
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION
    }


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "health": "/health",
        "endpoints": {
            "chat": "POST /api/v1/chat",
            "webhook": "POST /webhook/message",
            "audit": "GET /api/v1/audit",
            "ticket": "POST /api/v1/ticket"
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )
