import os

from flask import Flask, request, jsonify

def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY='dev',
  )

  if test_config is None:
    app.config.from_pyfile('config.py', silent=True)
  else:
    app.config.from_mapping(test_config)
  
  @app.route('/api/v1/sum', methods=['POST'])
  def sum():
    if not request.is_json:
      return 'Request body must be JSON', 400
    
    body = request.get_json()
    for key in ['a', 'b']:
      if key not in body:
        return 'Request body must contain key "{}"'.format(key), 400
      if type(body[key]) not in [int, long]:
        return 'Request body value of key "{}" must be an integer'.format(key), 400
    
    return jsonify(
      result=(body['a'] + body['b']),
    )
  
  return app