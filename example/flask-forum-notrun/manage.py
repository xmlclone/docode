import os
from app import create_app, db
from app.models import User, Post, Category

app = create_app()

@app.cli.command()
def initdb():
    """Initialize database"""
    db.create_all()
    # 创建默认分类
    categories = ['技术讨论', '问题求助', '资源分享', '公告通知']
    for name in categories:
        if not Category.query.filter_by(name=name).first():
            category = Category(name=name)
            db.session.add(category)
    db.session.commit()
    print('Database initialized.')

if __name__ == '__main__':
    app.run()