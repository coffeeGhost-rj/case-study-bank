from database import *
from AlertManager import *

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
            patient.p_ID,
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
            patient.patient_id,
            "Temp:", patient.vitals.temperature,
            "Pulse:", patient.vitals.pulse,
            "O₂:", patient.vitals.oxygen
        )



def doctorAccess():
    try:

        #print(pObj.showPatientDetails())
        doctor_name = input("Enter Doctor name:")
        patient_ID = input("Enter Patient ID: ")
        patient = findpatient(patient_ID)

        if patient.doctor.name!= doctor_name:

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
        patient_name = input("Enter the Patient name")

        patient = findpatient(patient_ID)

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



showDoctors()
showPatients()
showVitals()

input("\nPress Enter to Continue...")



# menu

while True:

    print("\n ------------------------")
    print("Patient Vital Signs Monitor")
    print("\n ------------------------")

    print("1. Doctor access")
    print("2. patient Access")
    print("3. Exit")

    option = input("Enter the option you would like to choose: ")

    if option == "1":
        doctorAccess()

    elif option == "2":
        patientAccess()

    elif option == "3":
        print("End of program.")
        break

    else:
        print("Invalid option.")



        

