from flask import Flask, request, render_template
from sqlalchemy.orm import scoped_session
from sqlalchemy import create_engine
from database import SessionLocal, Base
from models import Patient

app = Flask(__name__)

# Set up database
engine = create_engine("postgresql://postgres:postgres@db/your_database")
db_session = scoped_session(SessionLocal, scopefunc=_app_ctx_stack.__ident_func__)

@app.teardown_appcontext
def cleanup(resp_or_exc):
    db_session.remove()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        patient_id = uuid.uuid4()
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        dob = request.form.get('dob')
        gender = request.form.get('gender')

        new_patient = Patient(
            id=str(patient_id),
            first_name=first_name,
            last_name=last_name,
            email=email,
            date_of_birth=dob,
            gender=gender
        )

        db_session.add(new_patient)
        db_session.commit()

        return 'Registration Successful'
    return render_template('register.html')

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    app.run(debug=True, host='0.0.0.0')
