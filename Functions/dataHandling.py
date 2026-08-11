from Users import Doctor, Patient
from phi import doctors, patients

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

DATA_FILE = PROJECT_ROOT / "phi" / "hospital_data.dat"


def save_data(doctors, patients):
    try:
        with open(DATA_FILE, "wb") as file:
            pickle.dump(
                {
                    "doctors": doctors,
                    "patients": patients
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

        from phi.sample_data import doctors, patients

        # Save the initial sample data into the .dat file.
        save_data(doctors, patients)

        return doctors, patients




    try:
        with open(DATA_FILE, "rb") as file:
            data = pickle.load(file)

        doctors = data.get("doctors", [])
        patients = data.get("patients", [])
        #vitals = data.get("vitals", [])

        if patients:

            max_patient_id = max(
                int(patient.patient_id[1:])
                for patient in patients
            )

            setattr(Patient, "p_ID", max_patient_id)

        if doctors:

            max_doctor_id = max(
                int(doctor.doc_ID[1:])
                for doctor in doctors
            )

            setattr(Doctor, "doc_ID", max_doctor_id)

        print("Data loaded successfully.")

        return doctors, patients

    except Exception as e:
        print("Error loading data:", e)
        return [], []
    
    
# -----  Data Testing -------
# load_data()
# save_data(doctors, patients)
# print(load_data()[1][-1].patient_id)

# vitals = load_data()[2]

# for p in load_data()[1]:
#     print(p.patient_id)
#     print(p.pName)
    

# for p in load_data()[2]:
    # print(p.patient_id)
    # print(p.pName)