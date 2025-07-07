import logging
from flask import Blueprint, redirect, flash, render_template, request, url_for
from flask_login import login_required, login_user, logout_user, current_user
from ..models import User, db
from ..forms import RegisterForm


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
logger = logging.getLogger(__name__)


@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    logger.debug(f'login: {request.method=}')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            user = User.query.filter_by(username=username, password=password).one_or_none()
            logger.debug(f'login: {username=}, {password=}, {user=}')
            if not user:
                flash('登录失败，用户名与密码不匹配')
                return render_template('auth/login.html')
        except:
            flash('登录失败')
            return render_template('auth/login.html')
        else:
            flash('登录成功')
            login_user(user)
            return redirect(url_for('main.index'))
    return render_template('auth/login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logger.debug(f'{current_user=} logout.')
    logout_user()
    return redirect(url_for('auth.login'))


@auth_bp.route('/register1', methods=['POST', 'GET'])
def register1():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        logger.debug(f'register: {username=}, {password=}')
        try:
            db.session.add(User(username=username, password=password))
            db.session.commit()
        except:
            flash('注册失败')
            return render_template('auth/register.html')
        else:
            flash('注册成功')
            return redirect(url_for('auth.login'))
    return render_template('auth/register1.html')


@auth_bp.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        db.session.add(User(username=username, password=password))
        db.session.commit()
        flash('注册成功')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)