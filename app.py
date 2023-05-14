from flask import Flask, request, render_template
import psycopg2
from psycopg2 import sql
import uuid

app = Flask(__name__)

# Database setup
def create_database():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="db"
    )
    conn.set_isolation_level(0)
    cur = conn.cursor()
    cur.execute("CREATE DATABASE your_database")
    conn.close()

def create_table():
    conn = psycopg2.connect(
        dbname="your_database",
        user="postgres",
        password="postgres",
        host="db"
    )
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id UUID PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        date_of_birth DATE,
        gender CHAR(1)
    )
    """)
    conn.commit()
    conn.close()

try:
    conn = psycopg2.connect(
        dbname="your_database",
        user="postgres",
        password="postgres",
        host="db"
    )
    create_database()
    create_table()
    conn.close()
except:
    print("error")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        patient_id = uuid.uuid4()
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        dob = request.form.get('dob')
        gender = request.form.get('gender')

        conn = psycopg2.connect(
            dbname="your_database",
            user="postgres",
            password="postgres",
            host="db"
        )

        cur = conn.cursor()

        insert_query = sql.SQL("INSERT INTO patients (id, first_name, last_name, email, date_of_birth, gender) VALUES (%s, %s, %s, %s, %s, %s)")
        data = (str(patient_id), first_name, last_name, email, dob, gender)

        cur.execute(insert_query, data)
        conn.commit()
        conn.close()

        return 'Registration Successful'
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
