from flask import Flask, render_template, request, redirect, url_for
from model_subscriber import SubscriberForm
from model_writer import WriterForm
from model_tutorial import TutorialForm, TutorialModel
from flask_sqlalchemy import SQLAlchemy
from IPython.display import display, HTML
from datetime import date
import json



app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testDB.db'
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    form = SubscriberForm(request.form)
    if request.method == 'POST':
        print("OK")
        subscriber = form.email.data 
        print(subscriber)
        file_object = open('subscribers.txt', 'a')
        file_object.write(subscriber + '\n')
        form.email.data = ""
        return redirect('/success')
    return render_template('home.html', form=form)

@app.route('/success', methods=['GET', 'POST'])
def success():
    form = SubscriberForm(request.form)
    if request.method == 'POST':
        print("OK")
        subscriber = form.email.data 
        print(subscriber)
        file_object = open('subscribers.txt', 'a')
        file_object.write(subscriber + '\n')
        form.email.data = ""
    return render_template('success.html', form=form)

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
        tutorial.wide_img = form.wide_img.data
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

@app.route('/tutorial-edit/<tag>', methods=['GET', 'POST'])
def tutorial_edit(tag):
    form = TutorialForm(request.form)
    tutorial = TutorialModel.query.filter_by(tag=tag).first()
    title = tutorial.title
    tag = tutorial.tag
    content = tutorial.content
    success = False

    if request.method == 'POST':

        if 'delete_button' in request.form:
            print("gets here")

            try:
                db.session.query(TutorialModel).filter_by(tag=tag).delete()
                db.session.commit()
                success=True
                return redirect('/tutorials')
            except Exception as e:
                print(e)
                #log your exception in the way you want -> log to file, log as error with default logging, send by email. It's upon you
                db.session.rollback()
                db.session.flush() # for resetting non-commited .add()

        elif form.validate:
            tutorial.tag = form.tag.data
            tutorial.title = form.title.data
            print(form.title.data)
            tutorial.content = form.content.data
            
            try:
                db.session.commit()
                success=True
                return redirect('/tutorials')
            except Exception as e:
                print(e)
                #log your exception in the way you want -> log to file, log as error with default logging, send by email. It's upon you
                db.session.rollback()
                db.session.flush() # for resetting non-commited .add()

        print(success)
            
    return render_template('tutorial-edit.html', form = form, title = title, tag = tag, content = content)


@app.route('/blog/', methods=['GET', 'POST'])
def blog():
    return render_template('blog.html')

@app.route('/devops/', methods=['GET', 'POST'])
def devops():
    return render_template('devops.html')

@app.route('/writeforus/', methods=['GET', 'POST'])
def writeforus():
    form = WriterForm(request.form)
    if request.method == 'POST':
        data = {}
        data['writer'] = []
        data['writer'].append({
            'name': form.name.data,
            'email': form.email.data,
            'city': form.city.data,
            'phone': form.phone.data,
            'details': form.details.data
        })
        with open('writers.json', 'w') as outfile:
            json.dump(data, outfile)

        return redirect('/')

    return render_template('writeforus.html', form=form)

app.run(host='0.0.0.0', port='5000')

#ssl_context='adhoc'