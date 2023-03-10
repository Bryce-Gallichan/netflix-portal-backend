# netflix-portal-backend

Back-end code for Netflix Portal full-stack application

## Requirements
- Python 3.7+
- FastAPI
- Uvicorn (for running the application)

## Installation
To install the required packages, run the following command:
```
pip install -r requirements.txt
```

To install run the application locally, run the following command:
```
uvicorn app.main:app --reload --port 8080
```

## Connecting to Firebase
This project uses Firebase Auth to authenticate requests. Follow the [setup guide](https://firebase.google.com/docs/auth) to configure your Firebase project and place the firebase.json credentials in the project root directory

## Contact
For any questions or issues, please contact the developer at gallichan.bryce@gmail.com.
