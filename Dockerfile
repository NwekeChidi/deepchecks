FROM python:3.12-alpine
WORKDIR /src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5001
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]