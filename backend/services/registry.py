from services.ner_service import ner_service_instance
from schemas.analysis import TaskType

"""
A registry mapping task types to their corresponding service instances.
"""
task_registry = {
    TaskType.NER: ner_service_instance
    # Add more task-service mappings as needed
}