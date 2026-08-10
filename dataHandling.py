import pickle
import os
# from sample_data import *

DATA_FILE = "hospital_data.dat"


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
    if not os.path.exists(DATA_FILE):
        return [], [], []

    try:
        with open(DATA_FILE, "rb") as file:
            data = pickle.load(file)

        doctors = data.get("doctors", [])
        patients = data.get("patients", [])
        vitals = data.get("vitals", [])

        print("Data loaded successfully.")

        return doctors, patients, vitals

    except Exception as e:
        print("Error loading data:", e)
        return [], []
    
    
# -----  Data Testing -------
# load_data()
# save_data(doctors, patients)
# print(load_data()[1][-1].patient_id)

# vitals = load_data()[2]

for p in load_data()[1]:
    print(p.patient_id)
    print(p.pName)
    

# for p in load_data()[2]:
    # print(p.patient_id)
    # print(p.pName)