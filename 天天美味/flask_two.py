from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<int:id>')
def two(id=0):
    if id == 0:
        return 'ID=0'
    else:
        return '%d'%id

if __name__ == '__main__':
    app.run(port=1234,debug=True)