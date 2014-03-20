import os

import bottle
from bottle import route
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['dev-trashspotter']

@route('/wakeup', method='GET')
def get_wakeup():
  return 'f'

bottle.run(server='gevent', port=os.environ.get('PORT', 5000))
