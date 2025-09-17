from datetime import datetime
import uuid
from pydantic import BaseModel, Field
from typing import Dict, List, Optional
from enum import Enum


class TaskType(str, Enum):
    """
    Enumeration representing the different AI tasks to be performed.
    """
    SENT = "sentiment"
    NER = "ner" # Named Entity Recognition    
    OCR = "ocr" # Optical Character Recognition
    CAP = "caption"
    CUS = "custom"


class AnalysisRequest(BaseModel):
    """
    Model representing the user requests for analysis.
    """
    task: TaskType = TaskType.NER # Default task is NER
    input_text: Optional[str]
    use_external: bool = False # Default is False. To be implemented.
    options: Dict = { "lang": "pt "}


class AnalysisResponse(BaseModel):
    """
    Model representing the user responses for analysis.
    """
    id: uuid.UUID
    task: TaskType
    engine: str
    result: List[Dict]
    elapsed_ms: int
    received_at: datetime = Field(default_factory=datetime.now)
    