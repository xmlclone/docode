from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User, Category

class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(2, 20)])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 20)])
    confirm_password = PasswordField('确认密码', validators=[
        DataRequired(), 
        EqualTo('password', message='密码必须一致')
    ])
    submit = SubmitField('注册')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('用户名已被使用')