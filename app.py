from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ
import uuid
from datetime import datetime
from markupsafe import escape

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)

class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.String(36), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(1), nullable=False)

db.create_all()

# create a registration form
@app.route('/register', methods=['GET'])
def register_form():
    return render_template('register.html')

# create a patient
@app.route('/register', methods=['POST'])
def register_patient():
    try:
        patient_id = str(uuid.uuid4())
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        dob = datetime.strptime(request.form.get('dob'), "%Y-%m-%d").date()
        gender = request.form.get('gender')

        new_patient = Patient(
            id=patient_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            date_of_birth=dob,
            gender=gender
        )

        db.session.add(new_patient)
        db.session.commit()

        return 'Registration Successful'
    except Exception as e:
        return f'Error creating patient: {str(e)}'

# get all patients
@app.route('/patients', methods=['GET'])
def get_patients():
    try:
        patients = Patient.query.all()
        return render_template('patients.html', patients=patients)
    except Exception as e:
        return f'Error getting patients: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
