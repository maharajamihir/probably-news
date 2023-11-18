FROM public.ecr.aws/docker/library/python:3.11-slim

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app.py app.py
COPY helper.py helper.py

EXPOSE 80

ENTRYPOINT [ "streamlit", "run", "app.py", \
    "--server.enableCORS", "true", \
             "--server.port", "80", \
             "--browser.serverPort", "80"]