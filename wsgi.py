from flask import Flask

from flask import render_template
from flask import request

application= Flask(__name__)

@application.route("/")
def index():
    return render_template('index.html', course_id=None)

@application.route("/course_id/<int:course_id>")
def index_with_param(course_id=None):
    return render_template('index.html', course_id=course_id)


@application.route("/files")
def files(name=None):
    return render_template('files.html', name=name)


@application.route("/grades")
def grades():
    return render_template('grades.html')

@application.route("/files/multiple_bar")
def multiple_bar():
    return render_template('small_multiples_files_bar_chart.html')

if __name__ == "__main__":
    application.run()