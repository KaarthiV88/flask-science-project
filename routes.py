from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # flash('Login requested for user {}, remember_me={}'.format(
       #     form.username.data, form.remember_me.data))
        return redirect(url_for('project'))
    return render_template('login.html',  title='Sign In', form=form)

@app.route('/project')
def project():
    projects = [
        {
            'name': 'B&V Volcano',
            'cost': '$ 8.75',
            'completion': '72%',
            'image': 'volcano.jpg'
        },
        {
            'name': 'Solar Powered Car',
            'cost': '$ 20.50',
            'completion': '28%',
            'image': 'solar-car.jpg'

        },
        {
            'name': 'Juice Powered Battery',
            'cost': '$ 18.55',
            'completion': '97%',
            'image': 'juice-battery.jpg'
        },
        {
            'name': 'DIY Telescope',
            'cost': '$ 8.40',
            'completion': '1%',
            'image': 'Telescopes.jpg'
        }
    ]
    return render_template('project.html', title='Project', projects=projects)

@app.route('/projects')
def projects():
    user = {'username': 'Kaarthi'}
    posts = [
        {
            'creator': {'username': 'James'},
            'project': 'Hello fellow CODERS, check out my new solar-powered car.'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'That is an okay project, but check out my amazing volcano!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)



