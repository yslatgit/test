from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from webform import NameForm
from flask import session,redirect,url_for,flash
from hello import User,Role
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = 'YSL'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1/test?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        print(user)
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index_3.html',form=form,name=session.get('name'),known=session.get('known',False))

if __name__ == '__main__':
    app.run(port=1324,debug=True)