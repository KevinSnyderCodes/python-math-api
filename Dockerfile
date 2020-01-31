FROM python:2.7.17

RUN pip install flask waitress

COPY . .

CMD waitress-serve --call 'python_math_api:create_app'