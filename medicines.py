# medicines.py
from db_connect import get_connection

def add_medicine(name, description, unit_price, quantity):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO medicines (name, description, unit_price, quantity)
        VALUES (?, ?, ?, ?)
    """, (name, description, unit_price, quantity))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_medicines():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicines")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
