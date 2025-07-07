from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.forms import PostForm
from app.models import Post, Category
from . import posts_bp

@posts_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = PostForm()
    form.category_id.choices = [(c.id, c.name) for c in Category.query.all()]
    
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            author=current_user,
            category_id=form.category_id.data
        )
        db.session.add(post)
        db.session.commit()
        flash('帖子发布成功！', 'success')
        return redirect(url_for('posts.detail', post_id=post.id))
    
    return render_template('posts/create.html', form=form)

@posts_bp.route('/<int:post_id>')
def detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('posts/detail.html', post=post)