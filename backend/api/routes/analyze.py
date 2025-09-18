import time
import uuid
import logging
from fastapi import APIRouter, Depends, HTTPException
from schemas.analysis import AnalysisRequest, AnalysisResponse
from services.nlp_service import get_nlp_service, NlpService 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post('/analyze', response_model=AnalysisResponse, tags=["Analysis"])
def analyze_text(request: AnalysisRequest, nlp_service: NlpService = Depends(get_nlp_service)):
    """
    Endpoint that analyzes the provided text and returns a summary and sentiment.
    """
    if not request.input_text:
        raise HTTPException(status_code=400, detail="input_text cannot be empty for NER task.")
    
    start_time = time.monotonic()
    
    # Calls the NLP service to analyze entities
    entities = nlp_service.analyze_entities(request.input_text)
    
    end_time = time.monotonic()
    elapsed_ms = int((end_time - start_time) * 1000)

    response = AnalysisResponse(
        id=uuid.uuid4(),
        task=request.task,
        engine="local:pt_core_news_sm",
        result=entities,
        elapsed_ms=elapsed_ms,
    )

    # Log the response
    logging.info(f"Analysis Response: {response}")

    return response
