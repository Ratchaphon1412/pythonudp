FROM python:3

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python -

COPY . /app
WORKDIR /app

# Install dependencies
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Run the application

CMD ["python3", "receiver.py"]
