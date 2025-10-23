# Hospital Management System (Python + MariaDB)

A beginner-friendly Hospital Management System built using **Python** with **Tkinter GUI** and **MariaDB** as the backend database. This project allows managing **patients, doctors, appointments, medicines, and prescriptions** with a simple graphical interface.

---

## Features

- **Patients Management**
  - Add, view, update, and delete patient records
- **Doctors Management**
  - Add, view, update, and delete doctor records
- **Appointments Management**
  - Schedule, view, update, and delete appointments
- **Medicines Management**
  - Add, view, update, and delete medicines
- **Prescriptions Management**
  - Add, view, update, and delete prescriptions
- User-friendly **Tkinter GUI** for easy interaction
- Fully connected to a **MariaDB database**

---

## Screenshots

*(Optional: Add screenshots of your GUI here to make your project more appealing)*

---

## Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
2.Create and activate a virtual environment (optional but recommended)
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# Windows CMD
.venv\Scripts\activate.bat
# Linux/Mac
source .venv/bin/activate
3.Install required python packages
pip install mariadb tk colorama
4.Setup MariaDB database

Create a database called hospital_db

Run the following SQL commands to create tables:
CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(10),
    dob DATE,
    phone VARCHAR(20),
    email VARCHAR(50),
    address TEXT
);

CREATE TABLE doctors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    specialization VARCHAR(50),
    phone VARCHAR(20),
    email VARCHAR(50)
);

CREATE TABLE appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    date DATETIME,
    reason TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(id)
);

CREATE TABLE medicines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    description TEXT,
    unit_price DECIMAL(10,2),
    quantity INT
);

CREATE TABLE prescriptions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    appointment_id INT,
    medicine_id INT,
    dosage VARCHAR(50),
    duration VARCHAR(50),
    FOREIGN KEY (appointment_id) REFERENCES appointments(id),
    FOREIGN KEY (medicine_id) REFERENCES medicines(id)
);
5.configure database credentials
Edit db_connect.py:
import mariadb

def get_connection():
    return mariadb.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD_HERE",  # replace with your local password
        database="hospital_db"
    )
6.run the gui
python hospital_gui.py

Project Structure
hospital_gui.py       # Main GUI file
db_connect.py         # Database connection
patients.py           # Patient management module
doctors.py            # Doctor management module
appointments.py       # Appointment management module
medicines.py          # Medicines management module
prescriptions.py      # Prescriptions management module
Notes

Ensure that MariaDB server is running before launching the GUI.

This project is beginner-friendly and can be expanded to include features like user authentication, reporting, and export/import functionalities.

Author

Namdrol Tharchen
Student | BCA Data Science (2027)

License

This project is open-source and available under the MIT License.


---

If you want, I can **also prepare a short, catchy description for LinkedIn post** so you can share your project there and attract attention for potential opportunities.  

Do you want me to do that next?
