import logging
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .models import User


logger = logging.getLogger(__name__)


class RegisterForm(FlaskForm):
    username = StringField('用户名：', validators=[DataRequired(), Length(min=3, max=80)])
    password = PasswordField('密码：', validators=[DataRequired(), Length(min=3, max=80)])
    submit = SubmitField('注册')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        # logger.debug(f'{user=}')
        if user:
            raise ValidationError("用户名已存在。")
