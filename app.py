
import bottle
from bottle import route

@route('/wakeup', method='GET')
def get_wakeup():
  return 'f'

bottle.run(host='localhost', port=8080, debug=True)
