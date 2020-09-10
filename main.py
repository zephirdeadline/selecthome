from subprocess import check_output

from flask import Flask
from flask import render_template

app = Flask(__name__)


def run_program(name):
    return check_output(['python2', './' + name + '.py']).decode('utf-8')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/switch_right_central')
def switch_right_central():
    return run_program("switch_right_central")


@app.route('/switch_left_central')
def switch_left_central():
    return run_program("switch_left_central")


@app.route('/switch_bar_color')
def switch_bar_color():
    return run_program("switch_bar_color")


@app.route('/switch_right_color')
def switch_right_color():
    return run_program("switch_right_color")


@app.route('/switch_left_color')
def switch_left_color():
    return run_program("switch_left_color")


@app.route('/switch_all_central')
def switch_all_central():
    run_program("switch_left_central")
    run_program("switch_right_central")
    return "ok"


@app.route('/switch_all_color')
def switch_all_color():
    run_program("switch_left_color")
    run_program("switch_right_color")
    run_program("switch_bar_color")
    return "ok"


@app.route('/all_light')
def all_light():
    run_program("switch_left_color")
    run_program("switch_right_color")
    run_program("switch_bar_color")
    run_program("switch_left_central")
    run_program("switch_right_central")


if __name__ == "__main__":
    app.run()
