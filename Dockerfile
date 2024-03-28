FROM python:3

WORKDIR /drf_lessons_app

COPY requirements.txt .

RUN pip install -r requirements.txt


COPY . .

CMD ["python", "manage.py", "runserver"]