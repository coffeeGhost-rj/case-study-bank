
from datetime import datetime

class Patient():
    p_ID = 1000
    def __init__(self, pName, age, gender, bloodGrp, patient_type, diagnosis, docObj):
        Patient.p_ID+=1
        self.patient_id = "P"+ str(Patient.p_ID)

        self.set_age(age)
        self.set_pname(pName)
        self.set_bg(bloodGrp)
        self.set_gender(gender)
        self.setpatientType(patient_type)
        self.setDiagnosis(diagnosis)
        self.setDoctor(docObj)

        
        # a list for adding multiple readings for multiple patients
        self.vitals_history = []

    # method for appending new readings to the list - invoked in the database.py file 
    def setVitals(self,vitalObj):
        if vitalObj is None:
            raise ValueError("Invalid Vital sign.")
        else:
            self.vitals_history.append(vitalObj)

    #get method to print the readings of each patient in the list
    def getVitalDetails(self):

        if not self.vitals_history:
            raise ValueError("No vital signs have been recorded for this patient yet.")

        vital_log = "\n====== Vitals History ======"
        reading_num = 1

        for vital in self.vitals_history:
            vital_log = vital_log + "\n\n -- Reading -- " + str(reading_num)
            vital_log = vital_log + "\n" + vital.showVitalDetails()
            reading_num +=1

        return vital_log


    def set_pname(self,pName):
        if len(pName)<=0:
            raise ValueError("The name of the patient cannot be Empty!")
        else:
            self.pName = pName

    def set_age(self, age):
        if len(str(age))<=0:
            raise ValueError("The age of the patient cannot be Empty.")
        else:
            self.age = age

    def set_gender(self, gender):

        gender_opt=["Male", "Female", "Other"]

        if gender not in gender_opt:
            raise ValueError("The Specified Gender is invalid.")
        else:
            self.gender = gender

    def set_bg(self,bloodGrp):

        blood_group = ["A+", "A-", "B+", "B-", "O+", "AB+", "AB-" , "O-"]

        if bloodGrp not in blood_group:
            raise ValueError("Invalid Blood Group")
        else:
            self.bloodGrp = bloodGrp


    def setpatientType(self,patient_type):
        patient_type_opt = ["Inpatient", "Outpatient", "Emergency"]

        if patient_type not in patient_type_opt:
            raise ValueError("Invalid Patient type.")
        else:
            self.patient_type = patient_type


    def setDiagnosis(self, diagnosis):
        if len(diagnosis)<=0:
            raise ValueError("The diagnosis cannot empty.")
        else:
            self.diagnosis = diagnosis


    def setDoctor(self, docObj):
        self.doctor = docObj

    def getDoctorDetails(self):
        return self.doctor.showDoctorDetails()

    def showPatientDetails(self):
        return (
            "Patient ID: " + str(self.patient_id) +
            "\nName: " + self.pName +
            "\nGender: " + self.gender +
            "\nAge: " + str(self.age) +
            "\nPatient Type: " + self.patient_type +
            "\nDiagnosis: " + self.diagnosis +
            "\nAssigned Doctor: " + self.doctor.name
        )


class InPatient(Patient):
    def __init__(self, pName, age, gender, bloodGrp, patient_type, diagnosis, docObj,  ward, bed):
        super().__init__(pName, age, gender, bloodGrp, patient_type, diagnosis, docObj)

        self.setWard(ward)
        self.setBed(bed)

        self.admission_date= datetime.now()


    def setWard(self,ward):
        if len(ward)<=0:
            raise ValueError("The ward cannot be empty.")
        else:
            self.ward = ward
                
    
    def setBed(self, bed):
        if(len(str(bed)))<=0:
            raise ValueError("This field cannot be empty.")
        else:
            self.bed = bed



    def showPatientDetails(self):
        return (
            super().showPatientDetails() +
            "\nWard: " + self.ward +
            "\nBed: " + str(self.bed) +
            "\nAdmission Date: " + self.admission_date.strftime("%d-%m-%Y %H:%M:%S")
        )



class OutPatient(Patient):
    def __init__(self, pName, age, gender, bloodGrp, patient_type, diagnosis, docObj , room):
        super().__init__(pName, age, gender, bloodGrp, patient_type, diagnosis, docObj)

        self.appointmentDate = datetime.now()
        self.setConsultation_room(room) 


    def setConsultation_room(self,room):
        if len(room)==0:
            raise ValueError("Consultation Room field cannot be Empty. Pls specify all details.")
        else:
            self.room =room


    def showPatientDetails(self):
        return (
            super().showPatientDetails() +
            "\nConsultation Room: " + self.room +
            "\nAppointment Date: " + self.appointmentDate.strftime("%d-%m-%Y %H:%M:%S")
        )






        
