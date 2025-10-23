# appointments.py
from db_connect import get_connection

def add_appointment(patient_id, doctor_id, date, reason):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO appointments (patient_id, doctor_id, date, reason)
        VALUES (?, ?, ?, ?)
    """, (patient_id, doctor_id, date, reason))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_appointments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointments")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
