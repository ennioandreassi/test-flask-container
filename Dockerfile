FROM python:3.8-slim

WORKDIR /app

copy app.py /app

RUN pip install flask requests flask-cors

COPY . .

EXPOSE 5000

ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
