from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal
import os

class ProjectController(BaseController):
    def __init__(self):
        super().__init__()

    def get_project_path(self, project_id: str) -> str:
        
        project_path = os.path.join(
            self.Files_directory, 
            project_id
            )
        
        os.makedirs(project_path, exist_ok=True)
        
        return project_path