class Doctor():

    # Auto-generating a unique Doctor ID.
    # Use a separate counter for class-level state so the instance
    # attribute `doc_ID` is always a string and never conflicts with the
    # numeric counter type used for increments.
    _doc_ID = 100

    def __init__(self, name, specialization):

        # Increment the class variable for every new doctor.
        # Use the type of the counter explicitly in the arithmetic.
        Doctor._doc_ID = int(Doctor._doc_ID) + 1

        # Each Doctor object gets its own unique Doctor ID.
        self.doc_ID = "D" + str(Doctor._doc_ID)

        # Unified lookup ID used by the common doctor/patient finder.
        self.u_id = self.doc_ID

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

        return ("Doctor ID: ", self.u_id ,
                "\n Doctor Name: " , self.name ,
                "\n Specialization: ", self.specialization)
        
