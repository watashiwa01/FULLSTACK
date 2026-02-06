from app import app, db, Employee

with app.app_context():
    db.create_all()
    if not Employee.query.first():
        e = Employee(name='Alice Example', email='alice@example.com')
        db.session.add(e)
        db.session.commit()
        print('Inserted sample row')
    else:
        print('Row already exists, count =', Employee.query.count())