FROM python:3.10-alpine

RUN pip install --upgrade pip

RUN mkdir -p /home/app
WORKDIR /home/app

COPY . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

ENV VIRTUAL_ENV=/home/app/.venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py collectstatic

EXPOSE 8000
