
FROM python:3.12.2-slim

RUN pip install pipenv

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock ./

RUN pipenv install --deploy --ignore-pipfile

COPY . .

CMD ["pipenv", "run", "python", "main.py"]