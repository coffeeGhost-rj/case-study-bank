from sample_data import *
from AlertManager import *
from Patient import *
from dataHandling import *

# doctors = []
# patients = []
try:
    # comment:
    loaded_data = load_data()

    # ``load_data`` is typed as returning either a 2-item or 3-item tuple,
    # so handle both shapes explicitly before binding to the expected names.
    if len(loaded_data) == 2:
        doctors, patients = loaded_data
        vitals = []
    else:
        doctors, patients, vitals = loaded_data
except Exception as e:
    print(e)
# end try


# ============================
# FIND PATIENT
# ============================
# finding the patient in the patients list usingthe patient ID

def findpatient (p_ID):

    # Iterate through Patient objects stored in the list.
    for p in patients:

        # Access the instance variable of each Patient object.
        if p.patient_id == p_ID:
            return p

    # If no matching object is found.
    raise LookupError("Patient not found in the records.")


# ============================
# FIND DOCTOR
# ============================
# Searches the doctors list using a Doctor ID.

def findDoctor (p_ID):
    for p in doctors:

        if p.doc_ID == p_ID:
            return p

    raise LookupError("Doctor not found in the records.")


# ============================
# DISPLAY AVAILABLE DOCTORS
# ============================
# Displays unique doctors associated with the current patient records.
# Each Patient object contains a reference to its assigned Doctor object through: patient.doctor

def showDoctors():

    print("\nAvailable Doctors")
    print("-" * 40)

    # Temporary list used to avoid displaying the same Doctor object more than once.
    doctors_list = []

    for patient in patients:

        if patient.doctor not in doctors_list:
            doctors_list.append(patient.doctor)

    for doctor in doctors_list:

        print(
            doctor.doc_ID,
            doctor.name,
            doctor.specialization
        )


# ==========================
# DISPLAY PATIENTS
# ==========================
def showPatients():

    print("\nAvailable Patients")
    print("-" * 40)

    for patient in patients:

        print(
            patient.patient_id,
            "\t",
            patient.pName,
            "\t" ,
            patient.doctor.name
        )


# ===============================
# DISPLAY VITAL RECORDS
# ===============================
# Displays the vital-sign history for every patient : ONE-TO-MANY ASSOCIATION
# One Patient --> Many VitalSigns readings

def showVitals():

    print("\nCurrent Vital Records")
    print("-" * 40)

    # Iterate through all Patient objects.
    for patient in patients:

        # Check whether the patient has any VitalSigns objects.
        if len(patient.vitals_history) == 0:
            print("Patient ID: " + patient.patient_id + " : NO VITAL RECORDS")
        else:
            print("Patient ID: " + patient.patient_id + ": " + patient.pName )
            reading_num = 1
            
            # Iterate through the VitalSigns objects belonging to the current Patient.
            for vital in patient.vitals_history:
                print(" Reading " + str(reading_num) + "---> \nTemperature: " + str(vital.temperature) + "°C \nPulse: " + str(vital.pulse) + "bpm \nOxygen Saturation: " + str(vital.oxygen) + "%")
                reading_num+=1


# def showVitals():

#     print("\nCurrent Vital Records")
#     print("-" * 40)

#     for patient in patients:

#         print(
#             "Patient ID", patient.patient_id,
#             "Temp:", patient.vitals.temperature,
#             "Pulse:", patient.vitals.pulse,
#             "O₂:", patient.vitals.oxygen
#         )


# ============================
# UPDATE PATIENT VITALS
# ============================
# Creates a new VitalSigns object and associates it with an existing Patient object.

# Every time a new reading is added, the patient's vitals_history list grows.
def updatePatientVitals():
    try:
        patient_ID = input("Enter Patient ID to update: ")
        patient = findpatient(patient_ID)
        
        print("\nUpdating Vitals for " + patient.pName)
        temp = float(input("Enter Temperature (°C): "))
        pulse = int(input("Enter Pulse (bpm): "))
        spo2 = int(input("Enter Oxygen Saturation (%): "))
        
        # creates a new vitalSigns Object -> Save straight to history list without showing upfront warnings
        new_vitals = VitalSigns(temp, pulse, spo2)

        # Associate the newly created VitalSigns object with the selected Patient object.
        patient.setVitals(new_vitals)
        
        print("[SUCCESS] New reading added successfully! Reading count: " + str(len(patient.vitals_history)))
        
    except ValueError as e :
        print("ERROR: Failed to update vitals")
        print("Reason: ",e)


# =========================
# DOCTOR ACCESS
# =========================
# Provides a menu through which a Doctor can access patient records and perform operations.

def doctorAccess():
    print("\n ------------------------")
    print("Doctors present in the hospital: ", len(doctors))
    print("\n ------------------------")
    
    try:

        doctor_id = input("Enter the Doctor ID: ")

        # Find the corresponding Doctor object.
        dname= findDoctor(doctor_id.upper())

        print("\n")
        print("Hello Dr.",dname.name,"!")
        print("\n")


        #====================
        # MENU
        #====================
        while True:

            print("---- Patient Records ----")

            print("1. Patient Access")
            print("2. Add Patient")
            print("3. Update Patient Vital Signs (New Reading)")
            print("4. Exit from Doctor window.")
            print("\n")

            option = input("Enter the option you would like to choose: ")

            if option == "1":
                
                # Function call to access a Patient object.
                patientAccess()

            elif option == "2":
                
                # Create and add a new Patient object.
                addPatient()
                
            elif option == "3":

                # Add a new VitalSigns object to a Patient.
                updatePatientVitals()

            elif option == "4":
                print("End of program.")
                break

            else:
                print("Invalid option.")


    except LookupError as e:

        print("Error:", e)

    except ValueError as e:

        print("Invalid doctor details:", e)


# =========================
# PATIENT ACCESS
# =========================
# Displays detailed information about the Patient who has accessed, including vital history and alerts.

def patientAccess():
    print("\n ------------------------")
    print("Patients currently admitted to the hospital are: ", len(patients))
    print("\n ------------------------")

    try:
        patient_ID = input("Enter Patient ID: " )
        # patient_name = input("Enter the Patient name: ") --- non-necessary ---

        # Retrieve the Patient object.
        patient = findpatient(patient_ID.upper())

        # -----------------------------
        # DISPLAY PATIENT DETAILS
        # -----------------------------
        print("\n ======= PATIENT REPORT ======")
        print(patient.showPatientDetails())

        print("\n =======  VITAL REPORT ======")
        print(patient.getVitalDetails())


        # -----------------------------
        # GENERATE ALERTS FOR EACH VITAL 
        # READING OF THE PATIENT 
        # -----------------------------
        print("\n =========    ALERTS      ========")
        # alerts = generateAlert(patient.vitals)
    
        # for alert in alerts:
        #     print(alert)

        reading_num = 1

        # Iterate through all VitalSigns objects associated with this Patient.
        for vital in patient.vitals_history:
            print("\n--- Reading " + str(reading_num) + " Alerts ---")

            # Pass the VitalSigns object to the alert function.
            alerts = generateAlert(vital)

            # Display each generated alert.
            for alert in alerts:
                print(alert)


            reading_num = reading_num + 1
    
    except LookupError as e:
        print("Error:", e)

    except ValueError as e:
        print("Invalid details:", e)


# =========================
# ADD NEW PATIENT
# =========================
def addPatient():
    try:
        # comment: adding new patient to the record
        patient_type = input("Enter the patient type: ")
        print(patient_type.title())

        # ----- CREATE INPATIENT OBJECT -----
        if patient_type.title() == "Inpatient":
            newpatient = InPatient(
                pName = input("Enter the patient name: "),
                age=input("Enter the patient age: "),
                gender=input("Enter the patient gender: "),
                bloodGrp=input("Enter the patient Blood group: "),
                patient_type=patient_type,
                diagnosis=input("Enter the diagnosis: "),

                # ----- DOCTOR OBJECT CREATION -----
                # A new Doctor object is created and passed to the InPatient object.
                
                docObj=Doctor(name=input("Enter the doctor name: "),
                              specialization=input("Enter the specialization of the Doctor: ")),
                ward=input("Enter the patient's ward: "),
                bed=input("Enter the patient's bed type: ")               
            )


            # Add the newly created Patient object to the patients collection.
            patients.append(newpatient)

            print("\n ------------------------")
            print("New Patient details have been added to the system.")
            print("\n ------------------------")
            print(newpatient.showPatientDetails())
            print("\n ------------------------")


        # ------ CREATE OUTPATIENT OBJECT -------    
        elif patient_type.title() == "Outpatient":
            newpatient = OutPatient(
                pName = input("Enter the patient name: "),
                age=input("Enter the patient age: "),
                gender=input("Enter the patient gender: "),
                bloodGrp=input("Enter the patient Blood group: "),
                patient_type=patient_type,
                diagnosis=input("Enter the diagnosis: "),

                #------- DOCTOR OBJECT CREATION -------
                # Doctor object is created and associated with the new OutPatient.
                
                docObj=Doctor(name=input("Enter the doctor name: "),
                              specialization=input("Enter the specialization of the Doctor: ")),
                room=input("Enter the consultation room: ")              
            )

            # Add the new Patient object to the patients list.
            patients.append(newpatient)
            print("\n ------------------------")
            print("New Patient details have been added to the system.")
            print("\n ------------------------")
            print(newpatient.showPatientDetails())
            print("\n ------------------------")
            
        
    except ValueError as e:
        print("Invalid patient details:",e)

    except LookupError as e:
        print("Record error:", e)
    # end try

# ================================
# INITIAL DISPLAY (program starts)
# ================================
showDoctors()
showPatients()
showVitals()

nullData =  input("\nPress Enter to Continue...")
# try:
#     # comment: 
#     load_data()
# except Exception as e:
#     raise e

# end try

# =========================
# MAIN MENU
# =========================

while True:
    
    print("\n ------------------------")
    print("Doctor and Patient Records")
    print("\n ------------------------")

    print("1. Doctor access")
    print("2. Patient Access")
    print("3. View All Current Vitals Summary")
    print("4. Exit")
    print("\n")

    option = input("Enter the option you would like to choose: ")

    if option == "1":
        doctorAccess()

    elif option == "2":
        patientAccess()

    elif option == "3":
        showVitals()
        
    elif option == "4":
        print("End of program.")
        save_data(doctors, patients)
        break

    else:
        print("Invalid option.")



        

