FROM python:3.8

ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /var/moto_practice
ADD ./ /var/moto_practice

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
RUN poetry config virtualenvs.create false && poetry install
