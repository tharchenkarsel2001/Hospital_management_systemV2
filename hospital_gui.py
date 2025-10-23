# hospital_gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from db_connect import get_connection
import patients, doctors, appointments, medicines, prescriptions

class HospitalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.conn = get_connection()
        if not self.conn:
            messagebox.showerror("Error", "Database connection failed!")
            root.destroy()
            return

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        # Initialize tabs
        self.init_patients_tab()
        self.init_doctors_tab()
        self.init_appointments_tab()
        self.init_medicines_tab()
        self.init_prescriptions_tab()

        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(root, textvariable=self.status_var, relief=tk.SUNKEN, anchor='w')
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    # ===== Helper Table Viewer =====
    def show_table(self, title, columns, data):
        table_win = tk.Toplevel(self.root)
        table_win.title(title)
        tree = ttk.Treeview(table_win, columns=columns, show='headings')
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        for row in data:
            tree.insert("", tk.END, values=row)
        tree.pack(fill='both', expand=True)

    # ===== Patients Tab =====
    def init_patients_tab(self):
        self.patients_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.patients_frame, text="Patients")
        ttk.Button(self.patients_frame, text="Add Patient", command=self.add_patient).pack(pady=5)
        ttk.Button(self.patients_frame, text="View Patients", command=self.view_patients).pack(pady=5)

    def add_patient(self):
        form = tk.Toplevel(self.root)
        form.title("Add Patient")
        labels = ["First Name", "Last Name", "Gender", "DOB YYYY-MM-DD", "Phone", "Email", "Address"]
        entries = {}
        for i, label in enumerate(labels):
            ttk.Label(form, text=label).grid(row=i, column=0, padx=5, pady=5)
            entries[label] = ttk.Entry(form)
            entries[label].grid(row=i, column=1, padx=5, pady=5)

        def submit():
            try:
                patients.add_patient(
                    entries["First Name"].get(),
                    entries["Last Name"].get(),
                    entries["Gender"].get(),
                    entries["DOB YYYY-MM-DD"].get(),
                    entries["Phone"].get(),
                    entries["Email"].get(),
                    entries["Address"].get()
                )
                messagebox.showinfo("Success", "Patient added successfully!")
                self.status_var.set("Patient added successfully")
                form.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
                self.status_var.set("Failed to add patient")

        ttk.Button(form, text="Submit", command=submit).grid(row=len(labels), column=0, columnspan=2, pady=10)

    def view_patients(self):
        try:
            data = patients.get_all_patients()
            self.show_table("Patients", ["ID", "First", "Last", "Gender", "DOB", "Phone", "Email", "Address"], data)
            self.status_var.set("Viewing patients")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_var.set("Failed to load patients")

    # ===== Doctors Tab =====
    def init_doctors_tab(self):
        self.doctors_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.doctors_frame, text="Doctors")
        ttk.Button(self.doctors_frame, text="Add Doctor", command=self.add_doctor).pack(pady=5)
        ttk.Button(self.doctors_frame, text="View Doctors", command=self.view_doctors).pack(pady=5)

    def add_doctor(self):
        form = tk.Toplevel(self.root)
        form.title("Add Doctor")
        labels = ["First Name", "Last Name", "Specialization", "Phone", "Email"]
        entries = {}
        for i, label in enumerate(labels):
            ttk.Label(form, text=label).grid(row=i, column=0, padx=5, pady=5)
            entries[label] = ttk.Entry(form)
            entries[label].grid(row=i, column=1, padx=5, pady=5)

        def submit():
            try:
                doctors.add_doctor(
                    entries["First Name"].get(),
                    entries["Last Name"].get(),
                    entries["Specialization"].get(),
                    entries["Phone"].get(),
                    entries["Email"].get()
                )
                messagebox.showinfo("Success", "Doctor added successfully!")
                self.status_var.set("Doctor added successfully")
                form.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
                self.status_var.set("Failed to add doctor")

        ttk.Button(form, text="Submit", command=submit).grid(row=len(labels), column=0, columnspan=2, pady=10)

    def view_doctors(self):
        try:
            data = doctors.get_all_doctors()
            self.show_table("Doctors", ["ID", "First", "Last", "Specialization", "Phone", "Email"], data)
            self.status_var.set("Viewing doctors")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_var.set("Failed to load doctors")

    # ===== Appointments Tab =====
    def init_appointments_tab(self):
        self.appointments_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.appointments_frame, text="Appointments")
        ttk.Button(self.appointments_frame, text="Add Appointment", command=self.add_appointment).pack(pady=5)
        ttk.Button(self.appointments_frame, text="View Appointments", command=self.view_appointments).pack(pady=5)

    def add_appointment(self):
        form = tk.Toplevel(self.root)
        form.title("Add Appointment")
        labels = ["Patient ID", "Doctor ID", "Date YYYY-MM-DD HH:MM", "Reason"]
        entries = {}
        for i, label in enumerate(labels):
            ttk.Label(form, text=label).grid(row=i, column=0, padx=5, pady=5)
            entries[label] = ttk.Entry(form)
            entries[label].grid(row=i, column=1, padx=5, pady=5)

        def submit():
            try:
                appointments.add_appointment(
                    int(entries["Patient ID"].get()),
                    int(entries["Doctor ID"].get()),
                    entries["Date YYYY-MM-DD HH:MM"].get(),
                    entries["Reason"].get()
                )
                messagebox.showinfo("Success", "Appointment added successfully!")
                self.status_var.set("Appointment added successfully")
                form.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
                self.status_var.set("Failed to add appointment")

        ttk.Button(form, text="Submit", command=submit).grid(row=len(labels), column=0, columnspan=2, pady=10)

    def view_appointments(self):
        try:
            data = appointments.get_all_appointments()
            self.show_table("Appointments", ["ID", "Patient ID", "Doctor ID", "Date", "Reason"], data)
            self.status_var.set("Viewing appointments")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_var.set("Failed to load appointments")

    # ===== Medicines Tab =====
    def init_medicines_tab(self):
        self.medicines_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.medicines_frame, text="Medicines")
        ttk.Button(self.medicines_frame, text="Add Medicine", command=self.add_medicine).pack(pady=5)
        ttk.Button(self.medicines_frame, text="View Medicines", command=self.view_medicines).pack(pady=5)

    def add_medicine(self):
        form = tk.Toplevel(self.root)
        form.title("Add Medicine")
        labels = ["Name", "Description", "Unit Price", "Quantity"]
        entries = {}
        for i, label in enumerate(labels):
            ttk.Label(form, text=label).grid(row=i, column=0, padx=5, pady=5)
            entries[label] = ttk.Entry(form)
            entries[label].grid(row=i, column=1, padx=5, pady=5)

        def submit():
            try:
                medicines.add_medicine(
                    entries["Name"].get(),
                    entries["Description"].get(),
                    float(entries["Unit Price"].get()),
                    int(entries["Quantity"].get())
                )
                messagebox.showinfo("Success", "Medicine added successfully!")
                self.status_var.set("Medicine added successfully")
                form.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
                self.status_var.set("Failed to add medicine")

        ttk.Button(form, text="Submit", command=submit).grid(row=len(labels), column=0, columnspan=2, pady=10)

    def view_medicines(self):
        try:
            data = medicines.get_all_medicines()
            self.show_table("Medicines", ["ID", "Name", "Description", "Unit Price", "Quantity"], data)
            self.status_var.set("Viewing medicines")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_var.set("Failed to load medicines")

    # ===== Prescriptions Tab =====
    def init_prescriptions_tab(self):
        self.prescriptions_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.prescriptions_frame, text="Prescriptions")
        ttk.Button(self.prescriptions_frame, text="Add Prescription", command=self.add_prescription).pack(pady=5)
        ttk.Button(self.prescriptions_frame, text="View Prescriptions", command=self.view_prescriptions).pack(pady=5)

    def add_prescription(self):
        form = tk.Toplevel(self.root)
        form.title("Add Prescription")
        labels = ["Appointment ID", "Medicine ID", "Dosage", "Duration"]
        entries = {}
        for i, label in enumerate(labels):
            ttk.Label(form, text=label).grid(row=i, column=0, padx=5, pady=5)
            entries[label] = ttk.Entry(form)
            entries[label].grid(row=i, column=1, padx=5, pady=5)

        def submit():
            try:
                prescriptions.add_prescription(
                    int(entries["Appointment ID"].get()),
                    int(entries["Medicine ID"].get()),
                    entries["Dosage"].get(),
                    entries["Duration"].get()
                )
                messagebox.showinfo("Success", "Prescription added successfully!")
                self.status_var.set("Prescription added successfully")
                form.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))
                self.status_var.set("Failed to add prescription")

        ttk.Button(form, text="Submit", command=submit).grid(row=len(labels), column=0, columnspan=2, pady=10)

    def view_prescriptions(self):
        try:
            data = prescriptions.get_all_prescriptions()
            self.show_table("Prescriptions", ["ID", "Appointment ID", "Medicine ID", "Dosage", "Duration"], data)
            self.status_var.set("Viewing prescriptions")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_var.set("Failed to load prescriptions")

# ===== Run GUI =====
if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalGUI(root)
    root.mainloop()
