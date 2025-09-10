from enum import Enum

class ResponseSignal(str, Enum):
    FILE_VALIDATED_SUCCESS = "File validated successfully"
    INVALID_FILE_TYPE = "Invalid file type"
    FILE_SIZE_EXCEEDS_LIMIT = "File size exceeds limit"
    FILE_UPLOAD_SUCCESS = "File uploaded successfully"
    FILE_UPLOAD_FAILED = "File upload failed"
    FILE_PROCESSING_FAILED = "File processing failed"
    FILE_PROCESSED_SUCCESS = "File processed successfully"