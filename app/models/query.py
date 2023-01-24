from pydantic import BaseModel

class Query(BaseModel):
    start_title: str = ''
    search_parms: str = ''
    type: str = 'Movie'