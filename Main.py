from Users import *
from Functions import *


# ============================================================
# LOAD HOSPITAL DATA
# ============================================================
# The dataHandling module checks whether hospital_data.dat already exists.

# FIRST RUN: sample_data.py is used to create the initial data and the data is saved into hospital_data.dat.

# FUTURE RUNS: Existing doctors and patients are loaded from the hospital_data.dat file.

doctors, patients = load_data()


# ============================================================
# INITIAL DISPLAY (remove)
# ============================================================
# Display the current data after loading it from the file.
# ============================================================

showDoctors()
showPatients()


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
    print("3. View All Current Vitals Summary")
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
            doctorAccess()
        case (2):
            # =========================
            # PATIENT ACCESS
            # =========================
            patientAccess()
        case (3):
            # =========================
            # VIEW VITALS
            # =========================
            showVitals()
        case (4):
            # =========================
            #  EXIT
            # =========================
            
            # Saving once more before exiting.
            save_data(doctors, patients)

            print("End of program.")

            break
        case (_):
            # comment: Invalid option
            print("INVALID OPTION")
    # end match

