# Run -> uvicorn api.main:app --reload
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importing routes
from api.routes import healthz, analyze


# -- Constants --
API_PREFIX = "/api/v1"

# Initializing FastAPI application
app = FastAPI(
    title="FASA/UNICAP - Full-Stack + AI"
)

# --- CORS configuration ---
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --- End of CORS configuration ---

# --- Routes ---
app.include_router(healthz.router, prefix=API_PREFIX)
app.include_router(analyze.router, prefix=API_PREFIX)
