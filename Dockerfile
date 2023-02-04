FROM python:3.9-slim

ENV VIRTUAL_ENV=/opt/venv

WORKDIR /opt/intelas

COPY requirements.txt .

RUN python3 -m venv $VIRTUAL_ENV
RUN $VIRTUAL_ENV/bin/pip3 install -r requirements.txt

ENV PATH=$VIRTUAL_ENV/bin:$PATH

COPY . .

CMD ["python3", "manage.py", "runserver", "0:8000"]
