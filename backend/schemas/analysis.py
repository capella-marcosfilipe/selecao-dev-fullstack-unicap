from datetime import datetime
import uuid
from pydantic import BaseModel, Field
from typing import Dict, Optional
from enum import Enum

"""
Enumeration representing the different AI tasks to be performed.
"""
class TaskType(str, Enum):
    SENT = "sentiment"
    NER = "ner" # Named Entity Recognition    
    OCR = "ocr" # Optical Character Recognition
    CAP = "caption"
    CUS = "custom"

"""
Model representing the user requests for analysis.
"""
class AnalysisRequest(BaseModel):
    task: TaskType = TaskType.NER # Default task is NER
    input_text: Optional[str]
    use_external: bool = False # Default is False. To be implemented.
    options: Dict = { "lang": "pt "}

"""
Model representing the user responses for analysis.
"""
class AnalysisResponse(BaseModel):
    id: uuid.UUID
    task: TaskType
    engine: str
    result: Dict
    elapsed_ms: int
    received_at: datetime = Field(default_factory=datetime.now)
    