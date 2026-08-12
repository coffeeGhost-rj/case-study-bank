import os
import pickle
import sys
from pathlib import Path

# When this file is launched as a script (for example, python Functions/dataHandling.py),
# Python puts the Functions directory on sys.path first. That prevents Users and phi
# from being resolved unless the repository root is explicitly added to the import path.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from Users import Doctor, Patient, PermittedStaff
# from phi import doctors, patients, pStaff

DATA_FILE = PROJECT_ROOT / "phi" / "hospital_data.dat"


def save_data(doctors, patients, pStaff):
    try:
        with open(DATA_FILE, "wb") as file:
            pickle.dump(
                {
                    "doctors": doctors,
                    "patients": patients,
                    "pStaff": pStaff
                },
                file
            )
        print("Data saved successfully.")
    except Exception as e:
        print("Error saving data:", e)


def load_data():
    # if not os.path.exists(DATA_FILE):
    #     return [], [], []


    if not os.path.exists(DATA_FILE):

        print("No saved data found.")
        print("Creating initial hospital data...")

        from phi import doctors,patients,pStaff

        # Save the initial sample data into the .dat file.
        save_data(doctors, patients, pStaff)

        return doctors, patients, pStaff




    try:
        with open(DATA_FILE, "rb") as file:
            data = pickle.load(file)

        doctors = data.get("doctors", [])
        patients = data.get("patients", [])
        pStaff = data.get("pStaff", data.get("staffs", []))

        for doctor in doctors:
            if not hasattr(doctor, "u_id"):
                doctor.u_id = doctor.doc_ID

        for patient in patients:
            if not hasattr(patient, "u_id"):
                patient.u_id = patient.patient_id
                
        for staff in pStaff:
            if not hasattr(staff, "u_id"):
                staff.u_id = staff.pms_ID

        if patients:

            max_patient_id = max(
                int(patient.patient_id[1:])
                for patient in patients
            )

            setattr(Patient, "p_ID", max_patient_id)
            
        if pStaff:
        
            max_staff_id = max(
                int(staff.pms_ID[1:])
                for staff in pStaff
            )

            setattr(PermittedStaff, "pms_ID", max_staff_id)

        if doctors:

            max_doctor_id = max(
                int(doctor.doc_ID[1:])
                for doctor in doctors
            )

            setattr(Doctor, "doc_ID", max_doctor_id)

        print("Data loaded successfully.")

        return doctors, patients, pStaff

    except Exception as e:
        print("Error loading data:", e)
        return [], [], []
    
    
# -----  Data Testing -------
# This module is intentionally import-safe. Any quick checks should run under
# __main__ instead of being executed at import time.
if __name__ == "__main__":
    doctors, patients, pStaff = load_data()
    
    # print(doctors)
    for s in pStaff:
        print(s.u_id)
        print(s.name)
#  --------------------------------------------------
    # from phi.sample_data import doctors, patients, pStaff
    # save_data(doctors, patients, pStaff)
    # print("Loaded staff count:", len(load_data()[2]))


# for p in load_data()[2]:
#     print(p.u_id)
#     print(p.name)

# doctors, patients, pStaff = load_data()
    