import json
import bottle
from bottle import route, run, request, abort
# from pymongo import Connection
 
# connection = Connection('localhost', 27017)
# db = connection.mydatabase
 
@route('/gnip/:stream', method='POST')
def post_rules(stream):
    if stream == 'prod_darpa':
        pass
    elif stream == 'dev_darpa':
        pass
    else:
        abort(404, 'That stream does not exist')
    data = request.body.readline()
    if not data:
        abort(400, 'No data received')
    try:
        rules = json.loads(data)
    except ValueError:
        abort(400, 'Invalid JSON received')

    msg = 'it worked!', rules
    return rules
     
@route('/gnip/:stream', method='GET')
def get_rules(stream):
    if stream == 'prod_darpa':
        pass
    elif stream == 'dev_darpa':
        pass
    else:
        abort(404, 'That stream does not exist')
    rules = {
            "rules": [
                {"tag": "House", "value": "Highgarden"},
                {"tag": "Tyrell", "value": "Mace"},
                {"tag": "Tyrell", "value": "Margery"},
                ]
            }

    return rules
 
run(host='localhost', port=8080)