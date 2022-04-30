FROM python:3.8.13-bullseye

CMD ["flask", "run"]

ENV APP_ROOT=/opt/app APP_USER=app PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

WORKDIR $APP_ROOT

RUN useradd -d $APP_ROOT -r $APP_USER

RUN pip install --no-cache-dir flask flask-cors

COPY . $APP_ROOT
