from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    print('请求方式为------->', request.method)
    args = request.args.get("username") or "args没有参数"
    print('args参数是------->', args)
    form = request.form.get('name') or 'form 没有参数'
    print('form参数是------->', form)
    return jsonify(args=args, form=form)


if __name__ == '__main__':
    app.run(debug=True,port=12306)
