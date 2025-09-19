import uuid
from datetime import datetime
from enum import Enum
from typing import Dict, Optional

from pydantic import BaseModel, Field


class TaskType(str, Enum):
    """
    Enumeration representing the different AI tasks to be performed.
    """
    SENT = "sentiment"
    NER = "ner" # NER service is available in this project
    OCR = "ocr"
    CAP = "caption"
    CUS = "custom"


class AnalysisRequest(BaseModel):
    """
    Model representing the user requests for analysis.
    """
    task: TaskType = TaskType.NER # Default task is NER because by now it's the only one available.
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
    result: Dict
    elapsed_ms: int
    received_at: datetime = Field(default_factory=datetime.now)
    