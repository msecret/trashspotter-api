import os

import bottle
from bottle import route
import json
import pymongo
from pymongo import MongoClient

from decorators import enable_cors

client = MongoClient('localhost', 27017)
db = client['dev-trashspotter']

@route('/awake', method='GET')
def get_awake():
  return 'f'

@route('/garbage-can', method='POST')
@enable_cors
def post_garbage_can():
  bottle.response.content_type = 'application/json'
  return json.dumps({'success': True})

@route('litter', method='POST')
@enable_cors
def post_litter():
  return json.dumps({'success': True})


bottle.run(server='gevent', port=os.environ.get('PORT', 5000))
