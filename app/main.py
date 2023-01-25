import firebase_admin
from fastapi import FastAPI, status, Request
from firebase_admin import credentials, firestore
from .routers import users, shows
from fastapi.middleware.cors import CORSMiddleware


cred = credentials.Certificate("firebase_credentials.json")
admin = firebase_admin.initialize_app(cred)
db = firestore.client()

app = FastAPI()

origins = [
    "http://localhost:4200",
    "https://netflix-portal-4f825.web.app",
    "https://netflix-portal-4f825.firebaseapp.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.state.db = db

app.include_router(users.router)
app.include_router(shows.router, )

@app.get("/", status_code=status.HTTP_200_OK)
async def ping(request: Request):
    return f'Netflix Portal Backend | Deployed on {request.url}'