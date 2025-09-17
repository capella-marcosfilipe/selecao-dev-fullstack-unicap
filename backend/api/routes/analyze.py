import datetime
import uuid
from fastapi import APIRouter
from schemas.analysis import AnalysisRequest, AnalysisResponse


router = APIRouter()

@router.post('/analyze', response_model=AnalysisResponse, tags=["Analysis"])
def analyze_text(request: AnalysisRequest):
    """
    Endpoint that analyzes the provided text and returns a summary and sentiment.
    """
    # Mock response
    response = AnalysisResponse(
        id=uuid.uuid4(),
        task=request.task,
        engine="mock-engine",
        result=[
            {"text": "Marcos Filipe", "label": "PER"},
            {"text": "Brasil", "label": "LOC"},
            {"text": "UNICAP", "label": "ORG"}
        ],
        elapsed_ms=123,
    )
    
    return response
