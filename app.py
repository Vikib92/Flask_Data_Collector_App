from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from send_email import send_email

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/height_collector'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email_name']
        height = request.form['height']
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            dob = Data(email, height)
            db.session.add(dob)
            db.session.commit()
            avg_hgt = db.session.query(func.avg(Data.height_)).scalar()
            avg_hgt = round(avg_hgt, 1)
            cnt = db.session.query(Data.height_).count()
            send_email(email, height, avg_hgt, cnt)
            return render_template('success.html')
    return render_template('index.html', text='This email address is already available')

if __name__=='__main__':
    app.debug = True
    app.run()