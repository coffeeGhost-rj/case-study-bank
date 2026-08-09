class Doctor():

    #auto generating the Doc ID
    doc_ID = 100

    def __init__(self, name, specialization):

        # Increment the class variable for every new doctor.
        Doctor.doc_ID+=1

        # Each Doctor object gets its own unique Doctor ID.
        self.doc_ID = "D" + str(Doctor.doc_ID)

        # Using setter methods to validate and assign data.
        
        self.setName(name)
        self.setSpeciality(specialization)

    #setter methods for doctor class parameters
    # OOP CONCEPT: ENCAPSULATION

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


    # ===================================
    # METHOD TO DISPLAY DOCTOR DETAILS
    # ===================================
    def showDoctorDetails(self):

        return ("Doctor ID: ", self.doc_ID ,
                "\n Doctor Name: " , self.name ,
                "\n Specialization: ", self.specialization)
        
