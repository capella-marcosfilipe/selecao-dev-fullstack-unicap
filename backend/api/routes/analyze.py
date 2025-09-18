import uuid
import logging
from fastapi import APIRouter, HTTPException
from schemas.analysis import AnalysisRequest, AnalysisResponse
from services.registry import task_registry

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post('/analyze', response_model=AnalysisResponse, tags=["Analysis"])
def analyze(request: AnalysisRequest):
    """
    Receives an analysis request, delegates to the appropriate service, and returns the structured result.
    """
    logger.info(f"Received request for task: {request.task}.")
    
    # 1st - Retrieve the appropriate service based on the task type
    specialist_service = task_registry.get(request.task)
    
    if not specialist_service:
        raise HTTPException(status_code=400, detail=f"Task '{request.task}' is not supported or could not be found.")
    
    # 2nd - Calls the specialist service to process the request
    try:
        service_response = specialist_service.execute(request)
        
        # 3rd - Prepares the AnalysisResponse
        response = AnalysisResponse(
            id=uuid.uuid4(),
            task=request.task,
            **service_response
        )
        # Log the response
        logger.info(f"Analysis Response: {response}")

        return response
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise HTTPException(status_code=500, detail="An internal error occurred.")
