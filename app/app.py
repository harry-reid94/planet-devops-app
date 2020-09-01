from flask import Flask, render_template, request, redirect, url_for
from model_tutorial import TutorialForm, TutorialModel
from flask_sqlalchemy import SQLAlchemy
from IPython.display import display, HTML
from datetime import date



app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testDB.db'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/tutorials/')
def tutorials():
    tutorial = TutorialModel.query.all()
    #print(type(tutorial))
    #print(type(tutorial[0]))
    return render_template('tutorials.html', tutorial=tutorial)

@app.route('/tutorial-template/<tag>', methods=['GET', 'POST'])
def tutorial_template(tag):
    #tutorial = TutorialModel.query.all()
    tutorial = TutorialModel.query.filter_by(tag=tag).first()
    content = HTML(tutorial.content)
    return render_template('tutorial-template.html', tutorial=tutorial, content=content)

@app.route('/tutorial-create/', methods=['GET', 'POST'])
def tutorial_create():
    form = TutorialForm(request.form)
    if form.validate and request.method == 'POST':
        tutorial = TutorialModel()
        tutorial.tag = form.tag.data
        tutorial.title = form.title.data
        tutorial.content = form.content.data
        tutorial.python = form.python.data
        tutorial.linux = form.linux.data
        tutorial.ansible = form.ansible.data
        tutorial.docker = form.docker.data
        tutorial.kubernetes = form.kubernetes.data
        tutorial.rancher = form.rancher.data
        tutorial.aws = form.aws.data
        tutorial.github = form.github.data
        tutorial.created_date = date.today()
        print(tutorial.created_date)

        db.session.add(tutorial)

        success=False
        
        try:
            db.session.commit()
            success=True
            return redirect(url_for('tutorials'))
        except Exception as e:
            print(e)
            #log your exception in the way you want -> log to file, log as error with default logging, send by email. It's upon you
            db.session.rollback()
            db.session.flush() # for resetting non-commited .add()
        
        print(success)

        form.tag.data = ""
            
    return render_template('tutorial-create.html', form = form)

@app.route('/consultation/')
def consultation():
    return render_template('consultation.html')

app.run()