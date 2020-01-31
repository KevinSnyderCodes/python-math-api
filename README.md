# python-math-api

An API for doing simple math. Written in Python 2.7 using [Flask](https://github.com/pallets/flask).

## Run

With docker-compose:

```sh
docker-compose up
```

Locally (make sure Python 2.7 and Flask are installed):

```sh
FLASK_APP=python-math-api FLASK_ENV=development flask run
```

Unit tests (make sure pytest is installed):

```sh
python -m pytest
```

Unit tests with coverage (make sure coverage is installed):

```sh
coverage run -m pytest
coverage report
```

## Usage

Make requests to get the sum of two integers:

```sh
# Positive
curl -X POST \
  -H "Content-Type: application/json" \
  localhost:8080/api/v1/sum \
  -d '{"a": 2, "b": 2}'
# {"result":4}

# Negative
curl -X POST \
  -H "Content-Type: application/json" \
  localhost:8080/api/v1/sum \
  -d '{"a": -5, "b": -5}'
# {"result":-10}

# A mix of both
curl -X POST \
  -H "Content-Type: application/json" \
  localhost:8080/api/v1/sum \
  -d '{"a": 3, "b": -3}'
# {"result":0}
```
