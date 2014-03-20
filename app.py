
import bottle
from bottle import route
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['dev-trashspotter']

@route('/wakeup', method='GET')
def get_wakeup():
  return 'f'

bottle.run(host='localhost', port=8080, debug=True)
