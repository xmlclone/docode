from app import create_app, db
from app.models.user import User

app = create_app()

@app.cli.command('init-db')
def init_db():
    db.create_all()
    admin = User(username='admin', role='admin')
    admin.set_password('admin123')
    db.session.add(admin)
    db.session.commit()

if __name__ == '__main__':
    app.run()