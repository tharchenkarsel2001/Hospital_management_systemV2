# prescriptions.py
from db_connect import get_connection

def add_prescription(appointment_id, medicine_id, dosage, duration):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO prescriptions (appointment_id, medicine_id, dosage, duration)
        VALUES (?, ?, ?, ?)
    """, (appointment_id, medicine_id, dosage, duration))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_prescriptions():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM prescriptions")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
