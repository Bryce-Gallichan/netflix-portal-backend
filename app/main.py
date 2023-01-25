import firebase_admin
from fastapi import FastAPI, status, Request
from firebase_admin import credentials, firestore
from .routers import users, shows

cred = credentials.Certificate("firebase_credentials.json")
admin = firebase_admin.initialize_app(cred)
db = firestore.client()

app = FastAPI()
app.state.db = db

app.include_router(users.router)
app.include_router(shows.router, )

@app.get("/", status_code=status.HTTP_200_OK)
async def ping(request: Request):
    return f'Netflix Portal Backend | Deployed on {request.url}'