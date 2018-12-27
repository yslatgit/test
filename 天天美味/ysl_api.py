from flask import make_response
from flask import abort
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    # print (name)
    if name == 'no':
        return render_template('user.html')
    elif name == 'ysl':
        return render_template('user.html',user=name)

@app.errorhandler(404)
def page_not_find(e):
    return render_template('404.html'),404
    # if id == 2:
    #     abort(400)
    # else:
    #     return '<h1>%d</h1>'%id

     # response = make_response('<h1>This document carries a cookie!</h1>')
     # response.set_cookie('answer', '42')
     # return response

if __name__ == '__main__':
    # print()
    app.run(port=1234,debug=True)




























# students=[]
#
# @app.route('/')
# def welcome():
#     return 'Welcome to ysl api!'
#
# @app.route('/student/', methods=['POST'])
# def add_student():
#     print(request.json.get("id"))
#     student = {
#         'id' : request.form.get('id'),
#         'name' : request.form.get('name')
#     }
#     # student = {
#     #     'id' : request.json['id'],
#     #     'name' : request.json['name'],
#     #     'age' : request.json.get('age', ""),
#     #     'birthplace' : request.json.get('birthplace', ""),
#     #     'grade' : request.json['grade']
#     # }
#     students.append(student)
#     return "success"
# @app.route('/look/',methods=['GET'])
# def look_student():
#     for i in students:
#         print(str(i))
#     return str(i)


