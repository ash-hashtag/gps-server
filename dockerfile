FROM python:3.8-slim-buster

WORKDIR /app


RUN pip3 install navpy websockets asyncio

COPY . .

EXPOSE 8080

CMD [ "python3", "server.py" ]