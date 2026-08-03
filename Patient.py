class Patient():
    p_ID = 1000
    def __init__(self, pName, age, gender, bloodGrp, patient_type, ward, bed, diagnosis, docObj):
        Patient.p_ID+=1
        self.patient_id = "P"+ str(Patient.p_ID)

        self.set_age(age)
        self.set_pname(pName)
        self.set_bg(bloodGrp)
        self.set_gender(gender)
        self.setpatientType(patient_type)
        self.setWard(ward)
        self.setBed(bed)
        self.setDiagnosis(diagnosis)
        self.setDoctor(docObj)

        self.vitals = None


    def setVitals(self,vitalObj):
        if vitalObj is None:
            raise ValueError("Invalid Vital sign.")
        else:
            self.vitals = vitalObj

    def getVitalDetails(self):
        if self.vitals is None:
            raise ValueError("Vitals signs not assigned.")
        else:
            return self.vitals.showVitalDetails()


    def set_pname(self,pName):
        if len(pName)<=0:
            raise ValueError("The name of the patient cannot be Empty!")
        else:
            self.pName = pName

    def set_age(self, age):
        if len(str(age))<=0:
            raise ValueError("The gae of the patient cannot be Empty.")
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

    def setDoctor(self, docObj):
        self.doctor = docObj

    def getDoctorDetails(self):
        return self.doctor.showDoctorDetails()

    def showPatientDetails(self):
        return ("Patient ID: "+ str(self.p_ID) +
                "\nName: "+ self.pName +
                "\nGender: " + self.gender +
                "\nAge: "+ str(self.age) +
                "\nPatient Type: "+ self.patient_type +
                "\nDiagnosis: "+ self.diagnosis +
                "\nWard " + self.ward +
                "\nBed no.: " + str(self.bed))


