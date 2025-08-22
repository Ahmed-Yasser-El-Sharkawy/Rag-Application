from .BaseController import BaseController
from .ProjectController import ProjectController
from fastapi import UploadFile
from models import ResponseSignal
import re
import os

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576  # 1 MB
    def validate_uploader_file(self,file: UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False,ResponseSignal.INVALID_FILE_TYPE
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False,ResponseSignal.FILE_SIZE_EXCEEDS_LIMIT
        return True ,ResponseSignal.FILE_VALIDATED_SUCCESS

    def Generate_unique_Filepath(self, orgin_file: str,project_id:str):
        random_key= self.generate_random_string()
        project_path=ProjectController().get_project_path(project_id=project_id)
        cleaned_file_name = self.get_clean_filename(original_filename=orgin_file)

        new_file_path=os.path.join(project_path,random_key + "_" +  cleaned_file_name)
        
        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()
            new_file_path = os.path.join(
                project_path, 
                random_key + "_" + cleaned_file_name
                )

        return new_file_path, random_key + "_" + cleaned_file_name

    def get_clean_filename(self, original_filename: str) -> str:
        """Generate a clean filename by removing unwanted characters."""
        # Remove special characters and keep only alphanumeric characters and dots
        cleaned_file_name = re.sub(r'\W+', '', original_filename.strip())
        #
        cleaned_file_name = cleaned_file_name.replace(' ', '_')
        return cleaned_file_name