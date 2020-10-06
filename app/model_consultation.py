from flask import Flask
from wtforms import Form, BooleanField, StringField, validators
from wtforms.widgets import TextArea
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testDB.db'
db = SQLAlchemy(app)

class ConsultationModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True)
    email = db.Column(db.String(100), index=True, unique=True)
    company = db.Column(db.String(100), index=True, unique=True)
    phone = db.Column(db.String(100), index=True, unique=True)
    city = db.Column(db.String(100), index=True, unique=True)
    postcode = db.Column(db.String(100), index=True, unique=True)
    details = db.Column(db.String(1000), index=True, unique=True)

class ConsultationForm(Form):
    name = StringField('Name', [validators.required(), validators.length(max=100)])
    email = StringField('email', [validators.required(), validators.length(max=100)])
    company = StringField('company')
    phone = StringField('phone')
    city = StringField('city')
    postcode = StringField('postcode')
    details = StringField('Name', [validators.required(), validators.length(max=1000)])
    '''
    title    = StringField(u'Title', [validators.required(), validators.length(max=100)])
    subtitle = StringField('SubTitle', widget = TextArea())
    content1-title = StringField('content1-title')
    content1-
    '''


