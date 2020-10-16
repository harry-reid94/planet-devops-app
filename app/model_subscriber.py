from flask import Flask
from wtforms import Form, BooleanField, StringField, validators
from wtforms.fields.html5 import EmailField
from wtforms.widgets import TextArea
from wtforms.validators import InputRequired, Length, Email
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testDB.db'
db = SQLAlchemy(app)

class SubscriberForm(Form):

    style={'class': 'form-control subscribe-input', 'placeholder': 'Enter your email'}

    email = EmailField('email', validators=[InputRequired(), Length(1, 64), Email()], render_kw=style)

