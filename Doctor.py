class Doctor():

    #auto generating the Doc ID
    doc_ID = 100

    def __init__(self, name, specialization):

        Doctor.doc_ID+=1
        self.doc_ID = "D" + str(Doctor.doc_ID)

        self.setName(name)
        self.setSpeciality(specialization)

    #setter methods for doctor class parameters

    def setName(self, name):
        if len(str(name))==0:
            raise ValueError("Doctor name cannot be Empty.")
        else:
            self.name = name

    def setSpeciality(self, specialization):
        if len(str(specialization)) ==0:
            raise ValueError("Specialization cannot be Empty.")
        else:
            self.specialization = specialization

    def showDoctorDetails(self):

        return ("Doctor ID: ", self.doc_ID ,
                "\n Doctor Name: " , self.name ,
                "\n Specialization: ", self.specialization)
        
