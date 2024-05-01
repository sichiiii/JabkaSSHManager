FROM python:3.12

WORKDIR /ssh_micro_service

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "ws_connection_app:app", "--host", "0.0.0.0", "--port", "8001"]