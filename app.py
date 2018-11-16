from bottle import route, run, template

@route('/')
def hello():
    return template('index')

run(host='0.0.0.0', port=8001, debug=True)
