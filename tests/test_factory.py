import pytest
from flask import json
from python_math_api import create_app

def test_config():
  assert not create_app().testing
  assert create_app({'TESTING': True}).testing

@pytest.mark.parametrize(('a', 'b', 'result'), (
  (2, 2, 4),
  (10, 10, 20),
  (-5, -5, -10),
  (3, -3, 0),
))
def test_sum_ok(client, a, b, result):
  response = client.post(
    '/api/v1/sum',
    data=json.dumps({'a': a, 'b': b}),
    content_type='application/json',
  )

  assert response.status_code == 200
  assert response.is_json

  body = response.get_json()
  assert body['result'] == result

@pytest.mark.parametrize(('data', 'content_type', 'message'), (
  (None, None, 'Request body must be JSON'),
  (json.dumps({'a': 2, 'b': 2}), None, 'Request body must be JSON'),
  (json.dumps({'b': 2}), 'application/json', 'Request body must contain key "a"'),
  (json.dumps({'a': 2}), 'application/json', 'Request body must contain key "b"'),
  (json.dumps({'a': "foo", 'b': 2}), 'application/json', 'Request body value of key "a" must be an integer'),
  (json.dumps({'a': True, 'b': 2}), 'application/json', 'Request body value of key "a" must be an integer'),
  (json.dumps({'a': 1.1, 'b': 2}), 'application/json', 'Request body value of key "a" must be an integer'),
  (json.dumps({'a': 2, 'b': "foo"}), 'application/json', 'Request body value of key "b" must be an integer'),
  (json.dumps({'a': 2, 'b': True}), 'application/json', 'Request body value of key "b" must be an integer'),
  (json.dumps({'a': 2, 'b': 1.1}), 'application/json', 'Request body value of key "b" must be an integer'),
))
def test_sum_bad_request(client, data, content_type, message):
  response = client.post(
    '/api/v1/sum',
    data=data,
    content_type=content_type,
  )

  assert response.status_code == 400
  assert message in response.data