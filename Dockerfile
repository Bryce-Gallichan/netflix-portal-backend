FROM tiangolo/uvicorn-gunicorn:python3.9
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
