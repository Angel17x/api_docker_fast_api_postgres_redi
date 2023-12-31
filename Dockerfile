FROM python:3.9

RUN mkdir -p /home/app

WORKDIR /home/app

COPY ./requirements.txt /home/app/requirements.txt
COPY *.sql /docker-entrypoint-initdb.d/

RUN pip install --no-cache-dir --upgrade -r /home/app/requirements.txt

EXPOSE 3000

CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port", "3000"]