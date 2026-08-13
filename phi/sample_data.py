from Users.Doctor import *
from Users.Patient import *
from Users.PermittedStaff import PermittedStaff
from Functions.VitalSigns import *

# ============================
# CREATING DOCTOR OBJECTS
# ============================
doctor1 = Doctor("John Smith", "Cardiology")
doctor2 = Doctor("Rakesh Singh", "Neurology")
doctor3 = Doctor("Will Hall", "Gynaecology")

#  List Containing all the doctor objects

doctors = [doctor1, doctor2, doctor3]

# =============================
# CREATING PATIENT OBJECTS
# =============================
# Only the first three sample patients are kept in the active patient list.
patient1 = InPatient("Amit Shah", 45, "Male", "A+", "Inpatient", "Heart Disease", doctor1, "Cardialogy Ward", 12)
patient2 = InPatient("Emma Wilson", 60, "Female", "O+", "Inpatient", "Stroke Recovery", doctor2, "Neurology Ward", 9)
patient3 = OutPatient("Raj Kumar", 30, "Male", "AB-", "Outpatient", "Regular checkup", doctor1, "OPD")


# ==============================
# CREATING VITALSIGNS OBJECTS
# ==============================
#creating vital reports - Each object represents ONE vital-sign reading of a patient.

vital1 = VitalSigns(38.8 , 125, 88)
vital2 = VitalSigns(36.5, 75, 98)
vital3 = VitalSigns(37.6 , 105 , 90 )

# vitals = [vital1, vital2, vital3]


# =======================================================
# ASSOCIATING VITALSIGNS OBJECTS WITH PATIENT OBJECTS
# =======================================================
# OOP CONCEPT:
# ONE-TO-MANY ASSOCIATION - One Patient can have MANY VitalSigns readings.

patient1.setVitals(vital1)
patient2.setVitals(vital2)
patient3.setVitals(vital3)

# list of the patients 
patients = [patient1, patient2 , patient3]


# =======================================================
# CREATING PERMITTED STAFF MEMBERS
# =======================================================
# These are sample staff records used for the staff lookup workflow.
# The 3-member initial list includes two nurses and one receptionist.

nurse1 = PermittedStaff("Nurse Alice", "Nurse")
nurse2 = PermittedStaff("Nurse Bob", "Nurse")
receptionist1 = PermittedStaff("Jeremy", "Receptionist")
receptionist2 = PermittedStaff("Selena", "Receptionist")

pStaff = [nurse1, nurse2, receptionist1, receptionist2]
