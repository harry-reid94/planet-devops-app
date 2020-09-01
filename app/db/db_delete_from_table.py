import sqlite3
from model_tutorial import TutorialModel
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testDB.db'
db = SQLAlchemy(app)

conn = sqlite3.connect('testDB.db')


#db.session.query(SignoffModel).delete()

db.session.query(TutorialModel).delete()


db.session.commit()