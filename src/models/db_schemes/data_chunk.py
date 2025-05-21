from pydantic import BaseModel, Field,validator
from typing import Optional
from bson.objectid import ObjectId

class DataChunk(BaseModel):
    _id: Optional[ObjectId] 
    chunk_text: str = Field(..., min_length=1)
    chunk_metadata: dict 
    chunk_order: int = Field(..., gt=0)## this is to ensure that the chunk order is a positive integer
    chunk_project_id: ObjectId ## this is to ensure that the chunk project id is a string
    class Config:
        arbitrary_types_allowed = True