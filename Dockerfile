FROM python:3.12

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

RUN pip install "django-phonenumber-field[phonenumbers]"

COPY . .

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
