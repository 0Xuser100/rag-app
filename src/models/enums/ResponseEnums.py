from enum import Enum

class ResponseSignals(Enum):
    FILE_VALIDATION_SUCCESS = "File validation success"
    FILE_TYPE_NOT_ALLOWED = "File type not allowed"
    FILE_SIZE_TOO_LARGE = "File size too large"
    
    FILE_UPLOAD_SUCCESS = "File is Successfully  uploaded"
    FILE_UPLOAD_FAILED = "File upload failed"
