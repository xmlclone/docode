from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from ..models import Post, Reply
from .. import db

forum_bp = Blueprint('forum', __name__)

@forum_bp.before_request
@login_required
def require_login():
    pass

@forum_bp.route('/')
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('forum/index.html', posts=posts)

@forum_bp.route('/post', methods=['POST'])
def create_post():
    title = request.form['title']
    content = request.form['content']
    post = Post(title=title, content=content, author=current_user)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('forum.index'))