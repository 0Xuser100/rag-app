from .BaseController import BaseController
from .ProjectContorller import ProjectContorller
from fastapi import UploadFile
from models import ResponseSignals
import re
import os
class DataController(BaseController):
    def __init__(self):
        super().__init__()## super refers to the parent class BaseController
        self.size_scale = 1024 * 1024 # 1 MB
    
    def validate_uploaded_file(self,file:UploadFile):
        # check file extension
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False,ResponseSignals.FILE_TYPE_NOT_ALLOWED.value
        
        # check file size
        if file.size > self.app_settings.FILE_MAX_SIZE*self.size_scale: #file.size is in bytes and FILE_MAX_SIZE is in MB so we need to convert MB to bytes
            # 1 MB = 1024 * 1024 bytes
            return False,ResponseSignals.FILE_SIZE_TOO_LARGE.value
        
        return True,ResponseSignals.FILE_VALIDATION_SUCCESS.value 
    
    def generate_unique_filepath(self,original_filename:str,project_id:int):
        # Generate a unique filename using the project ID and the original filename 
        random_key = self.generate_random_string()
        project_path=ProjectContorller().get_project_path(project_id=project_id)
        cleaned_filename = self.get_cleaned_filename(original_filename=original_filename)
        new_file_path=os.path.join(
            project_path,
            random_key+"_"+cleaned_filename
        )
        # Check if the file already exists
        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()
            new_file_path = os.path.join(
                project_path,
                random_key+"_"+cleaned_filename
            )

        # Return the new file path
        return new_file_path,random_key+"_"+cleaned_filename
    def get_cleaned_filename(self,original_filename:str):
# Remove any special characters from the filename except for alphanumeric characters, underscores, and periods
        # and replace spaces with underscores
        cleaned_filename = re.sub(r'[^\w.]', '_', original_filename.strip())
#        # Remove leading and trailing underscores
        cleaned_filename=cleaned_filename.replace(" ","_")

        return cleaned_filename