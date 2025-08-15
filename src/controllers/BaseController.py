from helpers.config import get_settings, settings
import os

class BaseController:
    def __init__(self):
        self.app_settings = get_settings()
        self.Base_directory = os.path.dirname(os.path.dirname(__file__))
        self.Files_directory = os.path.join(self.Base_directory, "assets/Files")
        