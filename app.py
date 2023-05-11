from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        dob = request.form.get('dob')
        gender = request.form.get('gender')

        conn = psycopg2.connect(
            dbname="your_database",
            user="your_username",
            password="your_password",
            host="localhost"
        )

        cur = conn.cursor()

        insert_query = f"INSERT INTO patients (first_name, last_name, email, date_of_birth, gender) VALUES ('{first_name}', '{last_name}', '{email}', '{dob}', '{gender}')"

        cur.execute(insert_query)
        conn.commit()

        return 'Registration Successful'
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
