-- Hospital Database
CREATE DATABASE IF NOT EXISTS hospital_db;
USE hospital_db;

-- Patients Table
CREATE TABLE IF NOT EXISTS patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(10),
    dob DATE,
    phone VARCHAR(20),
    email VARCHAR(50),
    address VARCHAR(100)
);

-- Doctors Table
CREATE TABLE IF NOT EXISTS doctors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    specialization VARCHAR(50),
    phone VARCHAR(20),
    email VARCHAR(50)
);

-- Appointments Table
CREATE TABLE IF NOT EXISTS appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    appointment_date DATETIME,
    reason VARCHAR(100),
    FOREIGN KEY (patient_id) REFERENCES patients(id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(id)
);

-- Medicines Table
CREATE TABLE IF NOT EXISTS medicines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    description TEXT,
    unit_price DECIMAL(10,2),
    quantity INT
);

-- Prescriptions Table
CREATE TABLE IF NOT EXISTS prescriptions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    appointment_id INT,
    medicine_id INT,
    dosage VARCHAR(50),
    duration VARCHAR(50),
    FOREIGN KEY (appointment_id) REFERENCES appointments(id),
    FOREIGN KEY (medicine_id) REFERENCES medicines(id)
);
