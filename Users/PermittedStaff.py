class PermittedStaff():
    _pms_ID = 100
    
    def __init__(self, name, designation):

        # Increment the class variable for every new doctor.
        # Use the type of the counter explicitly in the arithmetic.
        PermittedStaff._pms_ID = int(PermittedStaff._pms_ID) + 1

        # Each Doctor object gets its own unique Doctor ID.
        self.pms_ID = "S" + str(PermittedStaff._pms_ID)

        # Unified lookup ID used by the common doctor/patient finder.
        self.u_id = self.pms_ID

        # Using setter methods to validate and assign data.
        self.setName(name)
        self.setDesignation(designation)
        
        
    def setName(self, name):
            if len(str(name))==0:
                raise ValueError("Doctor name cannot be Empty.")
            else:
                self.name = name
    
    def setDesignation(self, designation):
        if len(str(designation)) ==0:
            raise ValueError("Specialization cannot be Empty.")
        else:
            self.designation = designation