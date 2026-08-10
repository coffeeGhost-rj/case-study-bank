# doctors, patients = load_data()

# # doctors = []
# # patients = []
# try:
#     # comment:
#     loaded_data = load_data()

#     # ``load_data`` is typed as returning either a 2-item or 3-item tuple,
#     # so handle both shapes explicitly before binding to the expected names.
#     if len(loaded_data) == 2:
#         doctors, patients = loaded_data
#         vitals = []
#     else:
#         doctors, patients, vitals = loaded_data
# except Exception as e:
#     print(e)
# # end try




from dataHandling import save_data, load_data
from AlertManager import *
from Patient import *
from VitalSigns import *


# ============================================================
# LOAD HOSPITAL DATA
# ============================================================
# The dataHandling module checks whether hospital_data.dat already exists.

# FIRST RUN: sample_data.py is used to create the initial data and the data is saved into hospital_data.dat.

# FUTURE RUNS: Existing doctors and patients are loaded from the hospital_data.dat file.

doctors, patients = load_data()


# ============================================================
# FIND PATIENT
# ============================================================
# Searches for a Patient object using the Patient ID.

def findpatient(p_ID):

    # Iterate through all Patient objects.
    for p in patients:

        # Compare the given ID with the object's patient_id.
        if p.patient_id == p_ID:

            # Return the matching Patient object.
            return p

    # No matching Patient was found.
    raise LookupError("Patient not found in the records.")


# ============================================================
# FIND DOCTOR
# ============================================================
# Searches for a Doctor object using the Doctor ID.
# ============================================================

def findDoctor(doc_ID):

    # Iterate through all Doctor objects.
    for doctor in doctors:

        # Compare the entered ID with the Doctor object's ID.
        if doctor.doc_ID == doc_ID:

            return doctor

    # No matching Doctor was found.
    raise LookupError("Doctor not found in the records.")


# ============================================================
# DISPLAY AVAILABLE DOCTORS
# ============================================================
# Displays doctors associated with the current patient records.
# ASSOCIATION: Each Patient object contains a reference to a Doctor object.
# Therefore: Many Patients --> One Doctor
# ============================================================

def showDoctors():

    print("\nAvailable Doctors")
    print("-" * 40)

    # Temporary list used to avoid displaying the same
    # Doctor object multiple times.
    doctors_list = []

    # Iterating through Patient objects.
    for patient in patients:

        # Each Patient has an associated Doctor object.
        if patient.doctor not in doctors_list:

            doctors_list.append(patient.doctor)

    # Display the unique Doctor objects.
    for doctor in doctors_list:

        print(
            doctor.doc_ID,
            doctor.name,
            doctor.specialization
        )


# ============================================================
# DISPLAY PATIENTS
# ============================================================

def showPatients():

    print("\nAvailable Patients")
    print("-" * 40)

    for patient in patients:

        print(
            patient.patient_id,
            "\t",
            patient.pName,
            "\t",
            patient.doctor.name
        )


# ============================================================
# DISPLAY VITAL RECORDS
# ============================================================
# Displays all VitalSigns readings associated with each Patient.
# ONE-TO-MANY ASSOCIATION: One Patient --> Many VitalSigns objects
# ============================================================

def showVitals():

    print("\nCurrent Vital Records")
    print("-" * 40)

    # Iterate through every Patient object.
    for patient in patients:

        # Check whether the patient has any recorded vitals.
        if len(patient.vitals_history) == 0:

            print(
                "Patient ID: " +
                patient.patient_id +
                " : NO VITAL RECORDS"
            )

        else:

            print(
                "Patient ID: " +
                patient.patient_id +
                ": " +
                patient.pName
            )

            reading_num = 1

            # Iterate through the VitalSigns objects associated with this Patient.
            for vital in patient.vitals_history:

                print(
                    " Reading " +
                    str(reading_num) +
                    "---> \n"
                    "Temperature: " +
                    str(vital.temperature) +
                    "°C \n"
                    "Pulse: " +
                    str(vital.pulse) +
                    " bpm \n"
                    "Oxygen Saturation: " +
                    str(vital.oxygen) +
                    "%"
                )

                reading_num += 1


# ============================================================
# UPDATE PATIENT VITALS
# ============================================================
# Creates a new VitalSigns object and associates it with an existing Patient object.
# ASSOCIATION: One Patient --> Many VitalSigns objects
# ============================================================

def updatePatientVitals():

    try:

        patient_ID = input("Enter Patient ID to update: ")

        # Find the Patient object.
        patient = findpatient(patient_ID.upper())

        print("\nUpdating Vitals for " + patient.pName)

        # Take new vital readings from the user.
        temp = float(input("Enter Temperature (°C): "))
        pulse = int(input("Enter Pulse (bpm): "))
        spo2 = int(input("Enter Oxygen Saturation (%): "))

        # Create a new VitalSigns object.
        new_vitals = VitalSigns(temp, pulse, spo2)

        # Associate the new VitalSigns object with the Patient.
        patient.setVitals(new_vitals)

        # --------------------------
        # SAVE UPDATED DATA
        # --------------------------

        save_data(doctors, patients)

        print(
            "[SUCCESS] New reading added successfully! "
            "Reading count: " +
            str(len(patient.vitals_history))
        )

    except LookupError as e:

        print("Error:", e)

    except ValueError as e:

        print("ERROR: Failed to update vitals")
        print("Reason:", e)


# ============================================================
# DOCTOR ACCESS
# ============================================================
# Menu through which a Doctor can access patient records and perform operations.

def doctorAccess():

    print("\n ------------------------")
    print(
        "Doctors present in the hospital: ",
        len(doctors)
    )
    print("\n ------------------------")

    try:

        doctor_id = input("Enter the Doctor ID: ")

        # Finding the corresponding Doctor object.
        doctor = findDoctor(doctor_id.upper())

        inpatient_count = 0
        outpatient_count = 0

        for patient in patients:

            # Checking whether this patient is assigned to the logged-in doctor.
            if patient.doctor is doctor:

                # Separate patients according to their patient type.
                if patient.patient_type == "Inpatient":

                    inpatient_count += 1

                elif patient.patient_type == "Outpatient":

                    outpatient_count += 1


        print("\n")
        print("Hello Dr.", doctor.name, "!")
        print("\n")

        print("Patients under your care:")
        print(
            "Inpatients  :",
            inpatient_count
        )
        print(
            "Outpatients :",
            outpatient_count
        )
        print(
            "Total Patients:",
            inpatient_count + outpatient_count
        )

        print("\n")

        # ====================================================
        # DOCTOR MENU
        # ====================================================

        while True:

            print("---- Patient Records ----")

            print("1. Patient Access")
            print("2. Add Patient")
            print("3. Update Patient Vital Signs (New Reading)")
            print("4. Exit from Doctor window.")
            print("\n")

            option = input(
                "Enter the option you would like to choose: "
            )

            if option == "1":

                # Access a Patient object.
                patientAccess()

            elif option == "2":

                # Create and add a new Patient object.
                addPatient()

            elif option == "3":

                # Create and associate a new VitalSigns object.
                updatePatientVitals()

            elif option == "4":

                print("Exiting Doctor window.")
                break

            else:

                print("Invalid option.")

    except LookupError as e:

        print("Error:", e)

    except ValueError as e:

        print("Invalid doctor details:", e)


# ============================================================
# PATIENT ACCESS
# ============================================================

def patientAccess():

    print("\n ------------------------")
    print(
        "Patients currently admitted to the hospital are: ",
        len(patients)
    )
    print("\n ------------------------")

    try:

        patient_ID = input("Enter Patient ID: ")

        # Retrieve the Patient object using its ID.
        patient = findpatient(patient_ID.upper())

        # ---------------------------
        # DISPLAY PATIENT DETAILS
        # ---------------------------

        print("\n ======= PATIENT REPORT ======")

        print(
            patient.showPatientDetails()
        )

        # --------------------------
        # DISPLAY VITAL HISTORY
        # --------------------------

        print("\n ======= VITAL REPORT ======")

        print(
            patient.getVitalDetails()
        )

        # ---------------------------
        # GENERATE ALERTS
        # ---------------------------
        # Each VitalSigns object is passed to AlertManager. Helps determine the overall status.

        print("\n ========= ALERTS =========")

        reading_num = 1

        # Iterate through all VitalSigns objects belonging
        # to this Patient.
        for vital in patient.vitals_history:

            print(
                "\n--- Reading " +
                str(reading_num) +
                " Alerts ---"
            )

            # Passing the VitalSigns object to AlertManager.
            alerts = generateAlert(vital)

            # Display each generated alert.
            for alert in alerts:

                print(alert)

            reading_num += 1

    except LookupError as e:

        print("Error:", e)

    except ValueError as e:

        print("Invalid details:", e)


# ============================================================
# ADD NEW PATIENT
# ============================================================
# Creates either an InPatient or an OutPatient object.

def addPatient():

    try:

        patient_type = input(
            "Enter the patient type: "
        )

        print(patient_type.title())

        doctor_id = input(
            "Enter the Doctor ID to assign the patient: "
        )

        doctor = findDoctor(doctor_id.upper())

        # ====================================================
        # CREATE INPATIENT OBJECT
        # ====================================================

        if patient_type.title() == "Inpatient":

            newpatient = InPatient(

                pName=input(
                    "Enter the patient name: "
                ),

                age=input(
                    "Enter the patient age: "
                ),

                gender=input(
                    "Enter the patient gender: "
                ),

                bloodGrp=input(
                    "Enter the patient Blood group: "
                ),

                patient_type=patient_type,

                diagnosis=input(
                    "Enter the diagnosis: "
                ),

                # --------------------------------------------
                # DOCTOR OBJECT
                # --------------------------------------------
                # A new Doctor object is created and passed to the InPatient object.

                docObj= doctor,

                ward=input(
                    "Enter the patient's ward: "
                ),

                bed=input(
                    "Enter the patient's bed type: "
                )
            )

            # Adding the newly created Patient object to the patients collection.
            patients.append(newpatient)

            # ---------------------
            # SAVE UPDATED DATA
            # ---------------------

            save_data(doctors, patients)

            print("\n ------------------------")
            print(
                "New Patient details have been added "
                "to the system."
            )
            print("\n ------------------------")

            print(
                newpatient.showPatientDetails()
            )

            print("\n ------------------------")


        # =================================
        # CREATE OUTPATIENT OBJECT
        # =================================

        elif patient_type.title() == "Outpatient":

            newpatient = OutPatient(

                pName=input(
                    "Enter the patient name: "
                ),

                age=input(
                    "Enter the patient age: "
                ),

                gender=input(
                    "Enter the patient gender: "
                ),

                bloodGrp=input(
                    "Enter the patient Blood group: "
                ),

                patient_type=patient_type,

                diagnosis=input(
                    "Enter the diagnosis: "
                ),

                # --------------------------------------------
                # DOCTOR OBJECT
                # --------------------------------------------

                docObj=doctor,

                room=input(
                    "Enter the consultation room: "
                )
            )

            # Adding the new Patient object to the patients list.
            patients.append(newpatient)

            # Saving the updated data to the .dat file.
            save_data(doctors, patients)

            print("\n ------------------------")
            print(
                "New Patient details have been added "
                "to the system."
            )
            print("\n ------------------------")

            print(
                newpatient.showPatientDetails()
            )

            print("\n ------------------------")

        else:

            print(
                "Invalid patient type. "
                "Please enter Inpatient or Outpatient."
            )

    except ValueError as e:

        print("Invalid patient details:", e)

    except LookupError as e:

        print("Record error:", e)


# ============================================================
# INITIAL DISPLAY (remove)
# ============================================================
# Display the current data after loading it from the file.
# ============================================================

showDoctors()
showPatients()
showVitals()


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


    # =========================
    # DOCTOR ACCESS
    # =========================

    if option == "1":

        doctorAccess()


    # ==========================
    # PATIENT ACCESS
    # ==========================

    elif option == "2":

        patientAccess()


    # ==========================
    # VIEW VITALS
    # ==========================

    elif option == "3":

        showVitals()


    # ==================
    # EXIT
    # ==================

    elif option == "4":

        # Saving once more before exiting.
        save_data(doctors, patients)

        print("End of program.")

        break


    else:

        print("Invalid option.")
