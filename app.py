import app
from flask import Flask, render_template, abort
from flask_bootstrap import Bootstrap, Bootstrap5
from flask import Flask
from flask_wtf import FlaskForm, form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email



bootstrap = Bootstrap5(app)
app = Flask(__name__)
projects_data = [
    {
        "id": 1,
        "title": "Portfolio Site",
        "description": "This current website built with Flask.",
        "tech": "Python, HTML, CSS, Jinja2",
        "github_link": "[https://github.com/](https://github.com/)...",
        "image_url": "https://picsum.photos/id/1/600/400"  # Example stock photo
    },
    {
        "id": 2,
        "title": "Weather App",
        "description": "Fetches live weather data from an API.",
        "tech": "JavaScript, React, OpenWeatherMap API",
        "github_link": "[https://github.com/](https://github.com/)...",
        "image_url": "https://picsum.photos/id/10/600/400"
    },
    {
        "id": 3,
        "title": "Tour Israel",
        "description": "Israel travel guide",
        "tech": "JavaScript, React, OpenWeatherMap API",
        "github_link": "[https://github.com/](https://github.com/)...",
        "image_url": "https://picsum.photos/200/300?grayscale"
    },
{
        "id": 4,
        "title": "Menorah",
        "description": "Menorah with different characteristics",
        "tech": "JavaScript, React, OpenWeatherMap API",
        "github_link": "[https://github.com/](https://github.com/)...",
        "image_url": "https://picsum.photos/id/237/200/300"
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


if __name__ == '__main__':
    app.run()
