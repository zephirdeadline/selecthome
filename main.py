from subprocess import check_output

from flask import Flask
from flask import render_template

app = Flask(__name__)


def run_program(name, argv):
    return check_output(['python2', './' + name + '.py'] + argv).decode('utf-8')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/switch_right_central')
def switch_right_central():
    return run_program("push_button", ["PIN_RIGHT_CENTRAL"])


@app.route('/switch_left_central')
def switch_left_central():
    return run_program("push_button", ["PIN_LEFT_CENTRAL"])


@app.route('/switch_bar_color')
def switch_bar_color():
    return run_program("va_et_viens", ['PIN_BAR_COLOR'])


@app.route('/switch_right_color')
def switch_right_color():
    return run_program("va_et_viens", ['PIN_RIGHT_COLOR'])


@app.route('/switch_left_color')
def switch_left_color():
    return run_program("va_et_viens", ['PIN_LEFT_COLOR'])


@app.route('/switch_all_central')
def switch_all_central():
    run_program("push_button", ["PIN_LEFT_CENTRAL"])
    run_program("push_button", ["PIN_RIGHT_CENTRAL"])
    return "ok"


@app.route('/switch_all_color')
def switch_all_color():
    run_program("va_et_viens", ['PIN_LEFT_COLOR'])
    run_program("va_et_viens", ['PIN_RIGHT_COLOR'])
    run_program("va_et_viens", ['PIN_BAR_COLOR'])
    return "ok"


@app.route('/all_light')
def all_light():
    run_program("va_et_viens", ['PIN_LEFT_COLOR'])
    run_program("va_et_viens", ['PIN_RIGHT_COLOR'])
    run_program("va_et_viens", ['PIN_BAR_COLOR'])
    run_program("push_button", ["PIN_LEFT_CENTRAL"])
    run_program("push_button", ["PIN_RIGHT_CENTRAL"])

@app.route('/switch_rad_1')
def switch_rad_1():
    return run_program("switch_interupt", ['PIN_RAD1'])

@app.route('/switch_rad_2')
def switch_rad_2():
    return run_program("switch_interupt", ['PIN_RAD2'])

@app.route('/volet_stop')
def switch_rad_2():
    return run_program("volet", ['PIN_VOLET', 'STOP'])

@app.route('/volet_up')
def switch_rad_2():
    return run_program("volet", ['PIN_VOLET', 'UP'])

@app.route('/volet_down')
def switch_rad_2():
    return run_program("volet", ['PIN_VOLET', 'DOWN'])


if __name__ == "__main__":
    app.run(host="0.0.0.0")
