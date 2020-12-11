FROM python

WORKDIR /TILT/
COPY /app .

RUN pip install -r requirements.txt

ENTRYPOINT python app.py