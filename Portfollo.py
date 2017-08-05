from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_work():
    return render_template('root.html', template_folder='templates')

@app.route('/projects')
def projects_work():
    return render_template('projects.html', template_folder='templates')

@app.route('/about')
def about_work():
    return render_template('aboutMe.html', template_folder='templates')

app.run(debug=True)
