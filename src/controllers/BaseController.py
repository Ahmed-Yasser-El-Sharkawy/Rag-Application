from helpers.config import get_settings, settings
import os
import random
import string

class BaseController:
    def __init__(self):
        self.app_settings = get_settings()
        self.Base_directory = os.path.dirname(os.path.dirname(__file__))
        self.Files_directory = os.path.join(self.Base_directory, "assets/Files")

    def generate_random_string(self, length:int=12):
        """Generate a random string of fixed length."""
        letters = string.ascii_lowercase + string.digits
        return ''.join(random.choices(letters, k=length))
