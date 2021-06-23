FROM python:3

WORKDIR /app

COPY main.py /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "/app/main.py"]