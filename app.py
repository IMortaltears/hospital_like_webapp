from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.String(36), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    new = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(1), nullable=False)

@app.route('/register', methods=['GET'])
def register_form():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_patient():
    try:
        patient_id = str(uuid.uuid4())
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = str(uuid.uuid4())
        new = request.form.get('new')
        dob1 = request.form.get('dob')
        dob = datetime.datetime.strptime(dob1, '%Y-%m-%d')
        gender = request.form.get('gender')

        new_patient = Patient(
            id=patient_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            new=new,
            date_of_birth=dob,
            gender=gender
        )

        db.session.add(new_patient)
        db.session.commit()

        return 'Registration Successful'
    except Exception as e:
        return f'Error creating patient: {str(e)}'

@app.route('/patients', methods=['GET'])
def get_patients():
    try:
        patients = Patient.query.all()
        return render_template('patients.html', patients=patients)
    except Exception as e:
        return f'Error getting patients: {str(e)}'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')
