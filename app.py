from bottle import route, run, template, request, redirect
import os

@route('/')
def hello():
    return template('index')

@route('/upload', method='GET')
def upload():
    return template('upload')

@route('/upload', method='POST')
def do_upload():
    uploader = request.forms.get('name')
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png','.jpg','.jpeg'):
        return 'File extension not allowed.'

    save_path = 'media/uploads/' + uploader + '_' + name + ext
    upload.save(save_path) # appends upload.filename automatically
    return """
    <p>上传成功！</p>
    <a href="/">返回主页</a>
    """

run(host='0.0.0.0', port=8001, debug=True)

