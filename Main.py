from database import *
from AlertManager import *
from Patient import *

# finding the patient in the records

def findpatient (p_ID):
    for p in patients:

        if p.patient_id == p_ID:
            return p

    raise LookupError("Patient not found in the records.")


def showDoctors():

    print("\nAvailable Doctors")
    print("-" * 40)

    doctors = []

    for patient in patients:

        if patient.doctor not in doctors:
            doctors.append(patient.doctor)

    for doctor in doctors:

        print(
            doctor.doc_ID,
            doctor.name,
            doctor.specialization
        )


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


def showVitals():

    print("\nCurrent Vital Records")
    print("-" * 40)

    for patient in patients:

        print(
            "Patient ID", patient.patient_id,
            "Temp:", patient.vitals.temperature,
            "Pulse:", patient.vitals.pulse,
            "O₂:", patient.vitals.oxygen
        )



def doctorAccess():
    try:

        #print(pObj.showPatientDetails())
        # doctor_name = input("Enter Doctor name:")
        doctor_id = input("Enter the Doctor ID: ")
        
        patient_ID = input("Enter Patient ID: ")
        patient = findpatient(patient_ID.upper())

        if patient.doctor.doc_ID!= doctor_id.upper():

            raise ValueError("Doctor is not assigned to this patient.")

        print("\n ========= PATIENT REPORT ========")
        print(patient.showPatientDetails())

        print("\n =========  VITAL REPORT  ========")
        print(patient.getVitalDetails())

        print("\n =========    ALERTS      ========")
        alerts = generateAlert(patient.vitals)

        for alert in alerts:
            print(alert)

    except ValueError:
        print("The details provided are invalid.")



#patient access

def patientAccess():

    try:
        patient_ID = input("Enter Patient ID:" )
        # patient_name = input("Enter the Patient name")

        patient = findpatient(patient_ID.upper())

        print("\n ======= PATIENT REPORT ======")
        print(patient.showPatientDetails())

        print("\n =======  VITAL REPORT ======")
        print(patient.getVitalDetails())

        print("\n =========    ALERTS      ========")
        alerts = generateAlert(patient.vitals)
    
        for alert in alerts:
            print(alert)
    
    except ValueError:
        print("The details provided are invalid.")


def addPatient():
    try:
        # comment: adding new patient to the record
        patient_type = input("Enter the patient type: ")
        print(patient_type.title())
        
        if patient_type.title() == "Inpatient":
            newpatient = InPatient(
                pName = input("Enter the patient name: "),
                age=input("Enter the patient age: "),
                gender=input("Enter the patient gender: "),
                bloodGrp=input("Enter the patient Blood group: "),
                patient_type=patient_type,
                diagnosis=input("Enter the diagnosis: "),
                docObj=Doctor(name=input("Enter the doctor name: "),
                              specialization=input("Enter the specialization of the Doctor: ")),
                ward=input("Enter the patient's ward: "),
                bed=input("Enter the patient's bed type: ")               
            )
            
            patients.append(newpatient)
            print("\n ------------------------")
            print("New Patient details have been added to the system.")
            print("\n ------------------------")
            print(newpatient.showPatientDetails())
            print("\n ------------------------")
            
        elif patient_type.title() == "Outpatient":
            newpatient = OutPatient(
                pName = input("Enter the patient name: "),
                age=input("Enter the patient age: "),
                gender=input("Enter the patient gender: "),
                bloodGrp=input("Enter the patient Blood group: "),
                patient_type=patient_type,
                diagnosis=input("Enter the diagnosis: "),
                docObj=Doctor(name=input("Enter the doctor name: "),
                              specialization=input("Enter the specialization of the Doctor: ")),
                room=input("Enter the consultation room: ")              
            )
            
            patients.append(newpatient)
            print("\n ------------------------")
            print("New Patient details have been added to the system.")
            print("\n ------------------------")
            print(newpatient.showPatientDetails())
            print("\n ------------------------")
            
        
    except Exception as e:
        print(e)
    # end try


showDoctors()
showPatients()
showVitals()

input("\nPress Enter to Continue...")



# menu

while True:

    print("\n ------------------------")
    print("Doctor and Patient Records")
    print("\n ------------------------")

    print("1. Doctor access")
    print("2. Patient Access")
    print("3. Add Patient")
    print("4. Exit")

    option = input("Enter the option you would like to choose: ")

    if option == "1":
        doctorAccess()

    elif option == "2":
        patientAccess()

    elif option == "3":
        addPatient()
        
    elif option == "4":
        print("End of program.")
        break

    else:
        print("Invalid option.")



        

