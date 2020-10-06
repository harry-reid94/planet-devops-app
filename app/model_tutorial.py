from flask import Flask
from wtforms import Form, BooleanField, StringField
from wtforms.widgets import TextArea
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testDB.db'
db = SQLAlchemy(app)

class TutorialModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(20), index=True, unique=True)
    title = db.Column(db.String(100), index=True, unique=True)
    content = db.Column(db.String(2000), index=True, unique=True)
    python = db.Column(db.Integer)
    linux = db.Column(db.Integer)
    ansible = db.Column(db.Integer)
    docker = db.Column(db.Integer)
    kubernetes = db.Column(db.Integer)
    rancher = db.Column(db.Integer)
    jenkins = db.Column(db.Integer)
    aws = db.Column(db.Integer)
    github = db.Column(db.Integer)
    created_date = db.Column(db.Date)
    wide_img = db.Column(db.Integer)

class TutorialForm(Form):
    tag = StringField('Tag')
    title = StringField('Title')
    content = StringField('Content', widget = TextArea())
    python = BooleanField('Python?')
    linux = BooleanField('Linux?')
    ansible = BooleanField('ansible?')
    docker = BooleanField('docker?')
    kubernetes = BooleanField('kubernetes?')
    rancher = BooleanField('rancher?')
    jenkins = BooleanField('jenkins?')
    aws = BooleanField('aws?')
    github = BooleanField('github?')
    wide_img = BooleanField('wide img?')
    '''
    title    = StringField(u'Title', [validators.required(), validators.length(max=100)])
    subtitle = StringField('SubTitle', widget = TextArea())
    content1-title = StringField('content1-title')
    content1-
    '''


