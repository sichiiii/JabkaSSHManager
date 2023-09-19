FROM python:3.12

WORKDIR /ssh_manager

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install tzdata -y
ENV TZ="Europe/Moscow"

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
RUN pip3 install pandas --no-build-isolation

COPY . .
WORKDIR /
ENTRYPOINT ["python3.11", "/ssh_manager/manage.py", "runserver", "0.0.0.0:8000"]