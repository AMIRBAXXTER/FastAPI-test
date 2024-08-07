FROM python:3.11.4-alpine

WORKDIR /code

COPY . /code

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "code.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
