# doctors.py
from db_connect import get_connection

def add_doctor(first, last, specialization, phone, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO doctors (first_name, last_name, specialization, phone, email)
        VALUES (?, ?, ?, ?, ?)
    """, (first, last, specialization, phone, email))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_doctors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctors")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
