import subprocess
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import FloatField, StringField
from wtforms.validators import InputRequired


server = Flask(__name__)


class ValidationForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    time = FloatField(validators=[InputRequired()])


@server.route('/code', methods=['POST'])
def code():
    form = ValidationForm()
    if form.validate_on_submit():
        command, timeout = form.code.data, form.time.data
        proc = subprocess.Popen(f'python -c "{command}"', shell=True, stdout=subprocess.PIPE)
        try:
            outs, errs = proc.communicate(timeout=timeout)
            outs = outs.decode()
        except subprocess.TimeoutExpired:
            proc.kill()
            outs = 'Исполнение кода не уложилось в данное время'
        return outs
    else:
        return 'Invalid data', 400

if __name__ == '__main__':
    server.config['WTF_CSRF_ENABLED'] = False
    server.run(debug=True)

