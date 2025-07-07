from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User, Category

class PostForm(FlaskForm):
    title = StringField('标题', validators=[
        DataRequired(message='标题不能为空'),
        Length(max=120, message='标题长度不能超过120个字符')
    ])
    content = TextAreaField('内容', validators=[
        DataRequired(message='内容不能为空'),
        Length(min=20, message='内容至少需要20个字符')
    ])
    category_id = SelectField('分类', coerce=int)
    submit = SubmitField('发布帖子')