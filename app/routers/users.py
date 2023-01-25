from fastapi import APIRouter, Depends, HTTPException, status
from ..dependencies import has_access

router = APIRouter(
    prefix='/user',
    tags=['user'],
    responses={404: {'description': 'Not found'}}
)

@router.get("", status_code=status.HTTP_200_OK)
async def get_user(user: dict = Depends(has_access)):
    return user