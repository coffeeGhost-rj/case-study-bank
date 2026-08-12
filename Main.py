from Users import *
from Functions import *


# ============================================================
# LOAD HOSPITAL DATA
# ============================================================
# The dataHandling module checks whether hospital_data.dat already exists.

# FIRST RUN: sample_data.py is used to create the initial data and the data is saved into hospital_data.dat.

# FUTURE RUNS: Existing doctors and patients are loaded from the hospital_data.dat file.

doctors, patients, pStaff = load_data()

# Synchronize the runtime collection objects into the access layer module so its
# display and workflow functions see the same in-memory lists as Main.py.
# import Functions.accessability as accessability
# accessability.doctors = doctors
# accessability.patients = patients
# accessability.pStaff = pStaff


# ============================================================
# INITIAL DISPLAY (remove)
# ============================================================
# Display the current data after loading it from the file.
# ============================================================

showDoctors(patients)
showPatients(patients)


input("\nPress Enter to Continue...")


# ========================
# MAIN MENU
# ========================

while True:

    print("\n ------------------------")
    print("Doctor and Patient Records")
    print(" ------------------------")

    print("1. Doctor access")
    print("2. Patient Access")
    print("3. Permitted Staff Access")
    print("4. Exit")
    print("\n")

    option = input(
        "Enter the option you would like to choose: "
    )

    match (int(option)):
        case (1):
            # =========================
            # DOCTOR ACCESS
            # =========================
            doctorAccess(doctors,patients,pStaff)
        case (2):
            # =========================
            # PATIENT ACCESS
            # =========================
            patientAccess(patients)
        case (3):
            # =========================
            # Staff Access
            # =========================
            pmsAccess(pStaff, patients,doctors)
        case (4):
            # =========================
            #  EXIT
            # =========================
            
            # Saving once more before exiting.
            save_data(doctors, patients, pStaff)

            print("End of program.")

            break
        case (_):
            # comment: Invalid option
            print("INVALID OPTION")
    # end match

