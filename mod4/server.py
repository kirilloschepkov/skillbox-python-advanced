from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, Field
from wtforms.validators import InputRequired, Email, NumberRange, ValidationError, Length
from typing import Optional
from uptime import uptime as up
from shlex import quote


server = Flask(__name__)


def number_length(min: int, max: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: Field):
        if field.data < min or max < field.data:
            raise ValidationError(message)
    return _number_length


class NumberLength:
    def __init__(self, min: int, max: int, message: Optional[str] = None):
        self.min, self.max, self.message = min, max, message

    def __call__(self, form: FlaskForm, field: Field):
        if field.data < self.min or self.max < field.data:
            raise ValidationError(self.message)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired('My message about blank email'), Email('My message about invalid email')])
    # phone = IntegerField(validators=[InputRequired(), NumberRange(10**9, int('9'*10), 'My message about invalid number')])
    # phone = IntegerField(validators=[InputRequired(), number_length(1000000000, 9999999999, 'My message about invalid number from function validation')])
    phone = IntegerField(validators=[InputRequired(), NumberLength(1000000000, 9999999999, 'My message about invalid number from class validation')])
    name = StringField(validators=[InputRequired('My message about blank name'), Length(2, 15)])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired(), NumberLength(100000, 999999, 'Invalid length of index')])
    comment = StringField()


@server.route('/registration', methods=['POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data
        return f'Successfully registered user {email} with phone +7{phone}', 200
    return f'Invalid input: {form.errors}', 400


@server.route('/uptime', methods=['GET'])
def uptime():
    return f'Current uptime is {up()}'


@server.route('/ps', methods=['GET'])
def ps():
    return f'ps {quote(" ".join(map(str, request.args.getlist("arg"))))}'

if __name__ == '__main__':
    server.config['WTF_CSRF_ENABLED'] = False
    server.run(debug=True)
