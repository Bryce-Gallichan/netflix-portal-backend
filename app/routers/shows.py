from fastapi import APIRouter, Depends, HTTPException, Request, status

from app.models.query import Query
from ..dependencies import has_access

router = APIRouter(
    prefix='/show',
    tags=['show'],
    responses={404: {'description': 'Not found'}}
)

@router.post("/", status_code=status.HTTP_200_OK)
async def get_all_shows(query: Query, request: Request, user: dict = Depends(has_access)):
    db = request.app.state.db

    # Default limit
    limit = 3
    # Start title
    start_title = query.start_title
    # Search paramaters
    search_parms = query.search_parms
    # Type (Movie or TV Show)
    type = query.type

    show_ref = db.collection('show').where('title', '>=', search_parms.lower()).where('type', '==', type).order_by('title').start_at({'title': start_title}).limit(limit)
    docs = show_ref.stream()
    shows = []
    for doc in docs:
        shows.append(doc.to_dict())
    return shows

@router.get('/{show_id}', status_code=status.HTTP_200_OK)
async def get_show_by_id(show_id: str, request: Request, user: dict = Depends(has_access)):
    db = request.app.state.db

    show_ref = db.collection('show').document(show_id)
    show_doc = show_ref.get()

    if not show_doc.exists:
        raise HTTPException(status_code=404, detail='Show not found')
    
    return show_doc.to_dict()

@router.post('/{show_id}', status_code=status.HTTP_201_CREATED)
async def add_show_to_favorites(show_id: str, request: Request, user: dict = Depends(has_access)):
    uid = user['uid']
    db = request.app.state.db

    show_doc = await get_show_by_id(show_id, request)
    show_doc['id'] = show_id

    fav_ref = db.collection('user').document(uid).collection('favorite').document(show_id)
    fav_ref.set(show_doc)

    return show_doc

@router.delete('/{show_id}', status_code=status.HTTP_200_OK)
async def remove_show_from_favorites(show_id: str, request: Request, user: dict = Depends(has_access)):
    uid = user['uid']
    db = request.app.state.db

    fav_ref = db.collection('user').document(uid).collection('favorite').document(show_id)
    fav_ref.delete()

    return

    



    