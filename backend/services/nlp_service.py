import spacy

SPACY_PT_SM_MODEL = "pt_core_news_sm"

class NlpService:
    """
    A service class to handle Natural Language Processing (NLP) tasks.
    """
    def __init__(self):
        """
        Initialize the NLP service by loading the spaCy model.
        """
        print("Loading spaCy model...")
        self.nlp = spacy.load(SPACY_PT_SM_MODEL)
        print("spaCy model loaded successfully.")
    
    def analyze_entities(self, text: str) -> list[dict]:
        """
        Analyzes the input text to find named entities.
        """        
        doc = self.nlp(text)
        entities = [{ "text": ent.text, "label": ent.label_ } for ent in doc.ents]
        
        return entities

# Singleton instance of NlpService
nlp_service_instance = NlpService()

def get_nlp_service() -> NlpService:
    """
    Dependency injection function to get the singleton instance of NlpService.
    """
    return nlp_service_instance
