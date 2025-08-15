from .BaseController import BaseController
from fastapi import UploadFile

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576  # 1 MB
    def validate_uploader_file(self,file: UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False,"Invalid file type"
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False,"File size exceeds limit"
        return True ,"success"
