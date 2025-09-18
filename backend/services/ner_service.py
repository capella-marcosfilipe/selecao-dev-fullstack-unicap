import time
import logging
from fastapi import HTTPException
import spacy
from schemas.analysis import AnalysisRequest

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SPACY_PT_SM_MODEL = "pt_core_news_sm"

class NerService:
    """
    A service class to handle NER tasks.
    """
    def __init__(self):
        """
        Initialize the NLP service by loading the spaCy model.
        """
        print("Loading spaCy model...")
        self.nlp = spacy.load(SPACY_PT_SM_MODEL)
        print("spaCy model loaded successfully.")
    
    def execute(self, request: AnalysisRequest) -> list[dict]:
        """
        Executes the NER analysis on the request's input text.
        """
        if not request.input_text:
            raise ValueError("input_text cannot be empty for the NER task.")
        
        try:
            logger.info(f"Received Analysis Request: {request}")
            
            start_time = time.monotonic()
            
            entities = self.analyze_entities(request.input_text)
            
            end_time = time.monotonic()
            elapsed_ms = int((end_time - start_time) * 1000)
            
            response = { 
                        "engine": SPACY_PT_SM_MODEL, 
                        "result": {"entities": entities}, 
                        "elapsed_ms": elapsed_ms 
                        }
        except Exception as e:
            print(f"Error during NER analysis: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")
        
        # Log the response
        logger.info(f"Analysis Response: {response}")
        
        return response            
    
    def analyze_entities(self, text: str) -> list[dict]:
        """
        Executes the NER analysis on the request's input text.
        """        
        doc = self.nlp(text)
        entities = [{ "text": ent.text, "label": ent.label_ } for ent in doc.ents]
        
        return entities

# Singleton instance of NlpService
ner_service_instance = NerService()
