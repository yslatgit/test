from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from webform import NameForm
from flask import session,redirect,url_for,flash
app = Flask(__name__)

app.config['SECRET_KEY'] = 'YSL'

bootstrap = Bootstrap(app)
#flash提示
@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return  render_template('index_2.html',form=form,name=session.get('name'))
#重定向
# @app.route('/',methods=['GET','POST'])
# def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         session['name'] = form.name.data
#         return redirect(url_for('index'))
#     return render_template('index_2.html',form=form,name=session.get('name'))
#展示表单
# def index():
#     name = None
#     form = NameForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         form.name.data = ''
#     return render_template('index_2.html',form=form,name=name)
@app.route('/name')
def name():
    return '<h1>%s</h1>'%session.get('name')
if __name__ == '__main__':
    app.run(port=1234,debug=True)