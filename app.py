from flask import Flask, render_template, abort, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm, form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)

bootstrap = Bootstrap5(app)

projects_data = [
    {
        "id": 1,
        "title": "Portfolio Site",
        "description": "This current website built with Flask.",
        "tech": "Python, HTML, CSS, Jinja2",
        "github_link": "https://github.com/",
        "image": "https://picsum.photos/id/1/600/400",
        "tags": ["Python", "Flask", "Web"]
    },
    {
        "id": 2,
        "title": "Weather App",
        "description": "Fetches live weather data from an API.",
        "tech": "JavaScript, React, OpenWeatherMap API",
        "github_link": "https://github.com/",
        "image": "https://picsum.photos/id/10/600/400",
        "tags": ["JavaScript", "API", "React"]
    },
    {
        "id": 3,
        "title": "Tour Israel",
        "description": "Israel travel guide.",
        "tech": "JavaScript, React, OpenWeatherMap API",
        "github_link": "https://github.com/",
        "image": "https://picsum.photos/200/300?grayscale",
        "tags": ["Travel", "UI/UX"]
    },
    {
        "id": 4,
        "title": "Menorah",
        "description": "Menorah with different characteristics.",
        "tech": "JavaScript, React, OpenWeatherMap API",
        "github_link": "https://github.com/",
        "image": "https://picsum.photos/id/237/200/300",
        "tags": ["React", "Art"]
    }
]

@app.route('/')
def home():  # put application's code here
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=projects_data)
@app.route('/project/<int:project_id>')
def project(project_id):
    for project in projects_data:
        if project["id"] == project_id:
            return render_template('project_detail.html', project=project)

    return abort(404)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm(request.form)
    if form.validate_on_submit():
        user_name= form.name.data
        user_email= form.email.data
        user_message= form.message.data
        return redirect(url_for('contact_submission', user_name=user_name, user_email=user_email))
    return render_template('contact.html', form=form)

@app.route('/contact_submission/<user_name>/<user_email>')
def contact_submission(user_name, user_email):
    return render_template('contact_submission.html',  user_name=user_name, user_email=user_email)


if __name__ == '__main__':
    app.run(debug=True)
