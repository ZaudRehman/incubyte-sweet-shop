from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.middleware.trustedhost import TrustedHostMiddleware
import uvicorn

from app.api import auth, sweets, inventory

from dotenv import load_dotenv
load_dotenv()  # This loads variables from .env into environment


app = FastAPI(
    title="Sweet Shop Management System API",
    description="API backend for Sweet Shop Management System",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS origins (restrict in production as needed)
origins = [
    "http://localhost",
    "http://localhost:3000",  # React frontend default dev server
    # Add your production frontend domain here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# (Optional) Trusted Hosts middleware to restrict allowed host headers (enhances security)
# Disabled for testing
# app.add_middleware(
#     TrustedHostMiddleware,
#     allowed_hosts=["localhost", "127.0.0.1", "[::1]", "yourdomain.com"]  # Change accordingly
# )

# Exception handler example (customize as needed)
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"}
    )

# Include API routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(sweets.router, prefix="/api/sweets", tags=["Sweets"])
app.include_router(inventory.router, prefix="/api/sweets", tags=["Inventory"])

# Root health check endpoint
@app.get("/", tags=["Health"])
async def root():
    return {"message": "Sweet Shop Management System API is running"}

# Optional startup event
@app.on_event("startup")
async def on_startup():
    # Initialize connections, logging, caches, etc.
    pass

# Optional shutdown event
@app.on_event("shutdown")
async def on_shutdown():
    # Cleanup resources, connections, etc.
    pass

if __name__ == "__main__":
    # For local development with auto reload
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
