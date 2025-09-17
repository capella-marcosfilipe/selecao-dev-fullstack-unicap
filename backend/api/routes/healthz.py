from fastapi import APIRouter


router = APIRouter()

@router.get('/healthz', tags=["Health"])
def get_healthz():
    """
    Endpoint that checks if the API is running.
    Returns status OK.
    """
    return {"status": "ok"}