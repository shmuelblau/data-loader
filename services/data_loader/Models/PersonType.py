from pydantic import BaseModel, Field


class prediction_request(BaseModel):
    id : int 
    first_name : str
    last_name : str