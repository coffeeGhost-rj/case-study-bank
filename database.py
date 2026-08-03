from Doctor import *
from Patient import *
from VitalSigns import *

# creating doctors

doctor1 = Doctor("John Smith", "Cardiology")
doctor2 = Doctor("Rakesh Singh", "Neurology")
doctor3 = Doctor("Will Hall", "Gynaecology")

#create patient

# patient1 = Patient("Amit Shah", 45, "Male", "A+", "Inpatient", "Cardialogy Ward", 12, "Heart Disease", doctor1)
# patient2 = Patient("Emma Wilson", 60, "Female", "O+", "Inpatient", "Neurology Ward", 9, "Stroke Recovery", doctor2)
# patient3 = Patient("Raj Kumar", 30, "Male", "AB-", "Outpatient", "OPD", 2, "Regular checkup", doctor1)
# patient4 = Patient("Ritika Roy", 26, "Female", "A+", "Outpatient", "OPD", 1, "Regular checkup", doctor2)

# Updated sample patient creation to match the current class hierarchy:
# InPatient(pName, age, gender, bloodGrp, patient_type, diagnosis, docObj, ward, bed)
# OutPatient(pName, age, gender, bloodGrp, patient_type, diagnosis, docObj, room)
patient1 = InPatient("Amit Shah", 45, "Male", "A+", "Inpatient", "Heart Disease", doctor1, "Cardialogy Ward", 12)
patient2 = InPatient("Emma Wilson", 60, "Female", "O+", "Inpatient", "Stroke Recovery", doctor2, "Neurology Ward", 9)
patient3 = OutPatient("Raj Kumar", 30, "Male", "AB-", "Outpatient", "Regular checkup", doctor1, "OPD")
patient4 = OutPatient("Ritika Roy", 26, "Female", "A+", "Outpatient", "Regular checkup", doctor2, "OPD")

#creating vital reports

vital1 = VitalSigns(38.8 , 125, 88)
vital2 = VitalSigns(36.5, 75, 98)
vital3 = VitalSigns(37.6 , 105 , 90 )

patient1.setVitals(vital1)
patient2.setVitals(vital2)
patient3.setVitals(vital3)

# list of the patients 
patients = [patient1, patient2 , patient3]
# for p in patients:
#     print(p.showPatientDetails())