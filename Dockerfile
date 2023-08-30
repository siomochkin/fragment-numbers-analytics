FROM python:3.8

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/

RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

COPY . /app/

CMD ["python", "main.py"]