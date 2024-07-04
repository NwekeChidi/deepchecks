FROM python:3.12-alpine
# FROM nginx:latest

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 3002
CMD ["flask", "--app", "app", "run", "--host=0.0.0.0", "--port=3002", "--debug"]