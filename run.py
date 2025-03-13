from app import create_app, db
from app.models import User, Subject, Chapter, Quiz, Question, Score

app = create_app()

with app.app_context():
    db.create_all()

    # Add an admin user if it doesn't exist
    if not User.query.filter_by(username='admin').first():
        admin_user = User(username='admin', password='admin', full_name='Admin', qualification='Admin', dob='1970-01-01')
        db.session.add(admin_user)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Changed port to 5001