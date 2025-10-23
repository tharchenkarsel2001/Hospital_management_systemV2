# patients.py
from db_connect import get_connection

def add_patient(first, last, gender, dob, phone, email, address):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO patients (first_name, last_name, gender, dob, phone, email, address)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (first, last, gender, dob, phone, email, address))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_patients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
