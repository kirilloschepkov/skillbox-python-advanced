import subprocess
from flask import Flask, request
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
        script, time = form.code.data, form.time.data
        proc = subprocess.Popen(f'python -c "{script}"', shell=True, stdout=subprocess.PIPE)
        try:
            res, errs = proc.communicate(timeout=time)
            res = res.decode()
        except subprocess.TimeoutExpired:
            proc.kill()
            res = 'Исполнение кода не уложилось в данное время'
        return res
    else:
        return 'Invalid data', 400

if __name__ == '__main__':
    server.config['WTF_CSRF_ENABLED'] = False
    server.run(debug=True)

