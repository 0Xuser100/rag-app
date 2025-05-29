from .BaseController import BaseController
from .ProjectContorller import ProjectContorller
import os
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyMuPDFLoader
class ProcessController(BaseController):
    def __init__(self,project_id:str):
        super().__init__() 
        self.project_id=project_id
        self.project_path=ProjectContorller().get_project_path(project_id=project_id)
        

    def get_file_extension(self,file_id:str):
        return os.path.splitext(file_id)[-1]
    