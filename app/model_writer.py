from flask import Flask
from wtforms import Form, BooleanField, StringField, validators
from wtforms.fields.html5 import EmailField
from wtforms.widgets import TextArea
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import InputRequired, Length, Email

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testDB.db'
db = SQLAlchemy(app)

class WriterForm(Form):
    name={'class': 'form-control', 'placeholder': 'Name'}
    email={'class': 'form-control', 'placeholder': 'Email'}
    phone={'class': 'form-control', 'placeholder': 'Phone Number'}
    city={'class': 'form-control', 'placeholder': 'City'}
    postcode={'class': 'form-control', 'placeholder': 'Postcode'}
    details={'class': 'form-control', 'placeholder': 'Details'}

    name = StringField('Name', [ validators.length(max=100)], render_kw=name)
    email = EmailField('email', [validators.required(), Length(1, 64), Email()], render_kw=email)
    phone = StringField('phone', [validators.length(max=100)], render_kw=phone)
    city = StringField('city', [validators.length(max=100)], render_kw=city)
    postcode = StringField('postcode', [validators.length(max=100)], render_kw=postcode)
    details = StringField('Name', [validators.required(), validators.length(max=1000)], widget = TextArea(), render_kw=details)



