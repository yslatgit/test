from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/',methods=['POST',])
def index():
    user_agent = request.headers.get('User-Agent')
    return '<b>User-Agent:%s</b>'%user_agent

@app.route('/user/<int:id>')
def user(id):
    return '<h1>%d</h1>'%id

@app.route('/path/<string:path>')
def path_p(path):
    print(path)
    return '<h1>%s</h1>'%path

if __name__ == '__main__':
    print(app.url_map)
    app.run(port=12345,debug=True)