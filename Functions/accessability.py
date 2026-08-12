from Users import InPatient, OutPatient
from Functions.dataHandling import save_data
from Functions.AlertManager import generateAlert
from Functions.VitalSigns import VitalSigns

# Runtime state is initialized by Main.py via load_data() and then
# synchronized into these module-level collections.
doctors = []
patients = []
pStaff = []

def findUser(uid, datalist):

    # Iterate through all User objects.
    for i in datalist:

        # Compare the given ID with the object's u_id.
        if i.u_id == uid:

            # Return the matching user object.
            return i

    # No matching user was found.
    raise LookupError("User not found in the records.")

# ============================================================
# FIND PATIENT
# ============================================================
# Searches for a Patient object using the Patient ID.

# def findpatient(p_ID):

#     # Iterate through all Patient objects.
#     for p in patients:

#         # Compare the given ID with the object's patient_id.
#         if p.patient_id == p_ID:

#             # Return the matching Patient object.
#             return p

#     # No matching Patient was found.
#     raise LookupError("Patient not found in the records.")


# ============================================================
# FIND DOCTOR
# ============================================================
# Searches for a Doctor object using the Doctor ID.
# ============================================================

# def findDoctor(doc_ID):

#     # Iterate through all Doctor objects.
#     for doctor in doctors:

#         # Compare the entered ID with the Doctor object's ID.
#         if doctor.doc_ID == doc_ID:

#             return doctor

#     # No matching Doctor was found.
#     raise LookupError("Doctor not found in the records.")

# ============================================================
# DISPLAY AVAILABLE DOCTORS
# ============================================================
# Displays doctors associated with the current patient records.
# ASSOCIATION: Each Patient object contains a reference to a Doctor object.
# Therefore: Many Patients --> One Doctor
# ============================================================

def showDoctors(patientsList):

    print("\nAvailable Doctors")
    print("-" * 40)

    # Temporary list used to avoid displaying the same
    # Doctor object multiple times.
    doctors_list = []

    # Iterating through Patient objects.
    for patient in patientsList:

        # Each Patient has an associated Doctor object.
        if patient.doctor not in doctors_list:

            doctors_list.append(patient.doctor)

    # Display the unique Doctor objects.
    for doctor in doctors_list:

        print(
            doctor.u_id,
            doctor.name,
            doctor.specialization
        )


# ============================================================
# DISPLAY PATIENTS
# ============================================================

def showPatients(patientsList):

    print("\nAvailable Patients")
    print("-" * 40)

    for patient in patientsList:

        print(
            patient.u_id,
            "\t",
            patient.pName,
            "\t",
            patient.doctor.name
        )


# ============================================================
# DISPLAY VITAL RECORDS
# ============================================================
# Displays all VitalSigns readings associated with each Patient.
# ONE-TO-MANY ASSOCIATION: One Patient --> Many VitalSigns objects
# ============================================================

def showVitals(patientsList):

    print("\nCurrent Vital Records")
    print("-" * 40)

    # Iterate through every Patient object.
    for patient in patientsList:

        # Check whether the patient has any recorded vitals.
        if len(patient.vitals_history) == 0:

            print(
                "Patient ID: " +
                patient.u_id +
                " : NO VITAL RECORDS"
            )

        else:

            print(
                "Patient ID: " +
                patient.u_id +
                ": " +
                patient.pName
            )

            reading_num = 1

            # Iterate through the VitalSigns objects associated with this Patient.
            for vital in patient.vitals_history:

                print(
                    " Reading " +
                    str(reading_num) +
                    "---> \n"
                    "Temperature: " +
                    str(vital.temperature) +
                    "°C \n"
                    "Pulse: " +
                    str(vital.pulse) +
                    " bpm \n"
                    "Oxygen Saturation: " +
                    str(vital.oxygen) +
                    "%\n"
                )

                reading_num += 1


# ============================================================
# UPDATE PATIENT VITALS
# ============================================================
# Creates a new VitalSigns object and associates it with an existing Patient object.
# ASSOCIATION: One Patient --> Many VitalSigns objects
# ============================================================

def updatePatientVitals(staff, patientsList):

    try:

        patient_ID = input("Enter Patient ID to update: ")

        # Find the Patient object.
        patient = findUser(patient_ID.upper(),patientsList)

        print("\nUpdating Vitals for " + patient.pName)

        # Take new vital readings from the user.
        temp = float(input("Enter Temperature (°C): "))
        pulse = int(input("Enter Pulse (bpm): "))
        spo2 = int(input("Enter Oxygen Saturation (%): "))

        # Create a new VitalSigns object.
        new_vitals = VitalSigns(
            temp, 
            pulse, 
            spo2,
            recorded_by = staff) # type: ignore
        # new_vitals = VitalSigns

        # Associate the new VitalSigns object with the Patient.
        patient.setVitals(new_vitals)

        # --------------------------
        # SAVE UPDATED DATA
        # --------------------------

        save_data(doctors, patients,pStaff)

        print(
            "[SUCCESS] New reading added successfully! "
            "Reading count: " +
            str(len(patient.vitals_history))
        )

        # Display who recorded the reading.
        if staff is not None:

            print(
                "Recorded By:",
                staff.name
            )

            print(
                "Staff ID:",
                staff.u_id
            )

            print(
                "Designation:",
                staff.designation
            )


    except LookupError as e:

        print("Error:", e)

    except ValueError as e:

        print("ERROR: Failed to update vitals")
        print("Reason:", e)


# ============================================================
# DOCTOR ACCESS
# ============================================================
# Menu through which a Doctor can access patient records and perform operations.


# ============================================================
# ADD NEW PATIENT
# ============================================================
# Creates either an InPatient or an OutPatient object.

def addPatient(patients, doctors, patient_type):

    try:

        # patient_type = input(
        #     "Enter the patient type: "
        # )

        # print(patient_type.title())

        doctor_id = input(
            "Enter the Doctor ID to assign the patient: "
        )

        doctor = findUser(doctor_id.upper(),doctors)

        # ====================================================
        # CREATE INPATIENT OBJECT
        # ====================================================

        if patient_type.title() == "Inpatient":

            newpatient = InPatient(

                pName=input(
                    "Enter the patient name: "
                ),

                age=input(
                    "Enter the patient age: "
                ),

                gender=input(
                    "Enter the patient gender: "
                ),

                bloodGrp=input(
                    "Enter the patient Blood group: "
                ),

                patient_type=patient_type,

                diagnosis=input(
                    "Enter the diagnosis: "
                ),

                # --------------------------------------------
                # DOCTOR OBJECT
                # --------------------------------------------
                # A new Doctor object is created and passed to the InPatient object.

                docObj= doctor,

                ward=input(
                    "Enter the patient's ward: "
                ),

                bed=input(
                    "Enter the patient's bed type: "
                )
            )

            # Adding the newly created Patient object to the patients collection.
            patients.append(newpatient)

            # ---------------------
            # SAVE UPDATED DATA
            # ---------------------

            save_data(doctors, patients, pStaff)

            print("\n ------------------------")
            print(
                "New Patient details have been added "
                "to the system."
            )
            print("\n ------------------------")

            print(
                newpatient.showPatientDetails()
            )

            print("\n ------------------------")


        # =================================
        # CREATE OUTPATIENT OBJECT
        # =================================

        elif patient_type.title() == "Outpatient":

            newpatient = OutPatient(

                pName=input(
                    "Enter the patient name: "
                ),

                age=input(
                    "Enter the patient age: "
                ),

                gender=input(
                    "Enter the patient gender: "
                ),

                bloodGrp=input(
                    "Enter the patient Blood group: "
                ),

                patient_type=patient_type,

                diagnosis=input(
                    "Enter the diagnosis: "
                ),

                # --------------------------------------------
                # DOCTOR OBJECT
                # --------------------------------------------

                docObj=doctor,

                room=input(
                    "Enter the consultation room: "
                )
            )

            # Adding the new Patient object to the patients list.
            patients.append(newpatient)

            # Saving the updated data to the .dat file.
            save_data(doctors, patients, pStaff )

            print("\n ------------------------")
            print(
                "New Patient details have been added "
                "to the system."
            )
            print("\n ------------------------")

            print(
                newpatient.showPatientDetails()
            )

            print("\n ------------------------")

        else:

            print(
                "Invalid patient type. "
                "Please enter Inpatient or Outpatient."
            )

    except ValueError as e:

        print("Invalid patient details:", e)

    except LookupError as e:

        print("Record error:", e)

def doctorAccess(doctorsList , patientsList, staffList):

    print("\n ------------------------")
    print(
        "Doctors present in the hospital: ",
        len(doctorsList)
    )
    print("\n ------------------------")

    try:

        doctor_id = input("Enter the Doctor ID: ")

        # Finding the corresponding Doctor object.
        doctor = findUser(doctor_id.upper(), doctorsList)

        inpatient_count = 0
        outpatient_count = 0

        for patient in patientsList:

            # Checking whether this patient is assigned to the logged-in doctor.
            if patient.doctor is doctor:

                # Separate patients according to their patient type.
                if patient.patient_type == "Inpatient":

                    inpatient_count += 1

                elif patient.patient_type == "Outpatient":

                    outpatient_count += 1


        print("\n")
        print("Hello Dr.", doctor.name, "!")
        print("\n")

        print("Patients under your care:")
        print(
            "Inpatients  :",
            inpatient_count
        )
        print(
            "Outpatients :",
            outpatient_count
        )
        print(
            "Total Patients:",
            inpatient_count + outpatient_count
        )

        print("\n")

        # ====================================================
        # DOCTOR MENU
        # ====================================================

        while True:

            print("---- Patient Records ----")

            print("1. Patient Access")
            # print("2. Add Patient")
            print("2. Update Patient Vital Signs (New Reading)")
            print("3. Exit from Doctor window.")
            print("\n")

            option = input(
                "Enter the option you would like to choose: "
            )
            
            match (int(option)):
                case (1):
                    # comment: Access a Patient Object
                    patientAccess(patientsList)
                case (2):
                    # comment: Create and add a new Patient object.
                #     addPatient()
                # case (3):
                    # comment: Create and associate a new VitalSigns object.
                    updatePatientVitals(staffList, patientsList)
                case (3):
                    # comment: Exit Doctor's window
                    print("\n","Exiting the Doctor Window.....")
                    break
                case (_):
                    # comment: 
                    print("INVALID OPTION")
            # end match


    except LookupError as e:

        print("Error:", e)

    except ValueError as e:

        print("Invalid doctor details:", e)


# ============================================================
# PATIENT ACCESS
# ============================================================

def patientAccess(patients):

    print("\n ------------------------")
    print(
        "Patients currently admitted to the hospital are: ",
        len(patients)
    )
    print("\n ------------------------")

    try:

        patient_ID = input("Enter Patient ID: ")

        # Retrieve the Patient object using its ID.
        patient = findUser(patient_ID.upper(),patients)

        # ---------------------------
        # DISPLAY PATIENT DETAILS
        # ---------------------------

        print("\n ======= PATIENT REPORT ======")

        print(
            patient.showPatientDetails()
        )

        # --------------------------
        # DISPLAY VITAL HISTORY
        # --------------------------

        print("\n ======= VITAL REPORT ======")

        print(
            patient.getVitalDetails()
        )

        # ---------------------------
        # GENERATE ALERTS
        # ---------------------------
        # Each VitalSigns object is passed to AlertManager. Helps determine the overall status.

        print("\n ========= ALERTS =========")

        reading_num = 1

        # Iterate through all VitalSigns objects belonging
        # to this Patient.
        for vital in patient.vitals_history:

            print(
                "\n--- Reading " +
                str(reading_num) +
                " Alerts ---"
            )

            # Passing the VitalSigns object to AlertManager.
            alerts = generateAlert(vital)

            # Display each generated alert.
            for alert in alerts:

                print(alert,"\n")

            reading_num += 1

    except LookupError as e:

        print("Error:", e)

    except ValueError as e:

        print("Invalid details:", e)

def pmsAccess(pStaff, patients,doctors):

    try:

        pms_id = input("Enter the staff ID: ")

        # Finding the corresponding Doctor object.
        staff = findUser(pms_id.upper(), pStaff)
        
        #print("\n",staff.name,"\n")



        print("\n================================")
        print("Welcome", staff.name + "!")
        print("Staff ID:", staff.u_id)
        print("Designation:", staff.designation)
        print("================================")


        # ====================================================
        # NURSE ACCESS
        # ====================================================

        if staff.designation.title() == "Nurse":

            print("\nYou have access to update patient vitals.")

            while True:

                print("\n----- Nurse Window -----")
                print("1. Update Patient Vital Signs")
                print("2. Exit")
                print()

                option = input(
                    "Enter the option you would like to choose: "
                )

                match int(option):

                    case 1:
                        updatePatientVitals(staff,patients)

                    case 2:
                        print("\nExiting the Nurse Window.....")
                        break

                    case _:
                        print("INVALID OPTION")

        # ====================================================
        # RECEPTIONIST ACCESS
        # ====================================================

        elif staff.designation.title() == "Receptionist":

            print("\nYou have access to add patients.")

            while True:

                print("\n----- Receptionist Window -----")
                print("1. Add Inpatient")
                print("2. Add Outpatient")
                print("3. Exit")
                print()

                option = input(
                    "Enter the option you would like to choose: "
                )

                match int(option):

                    case 1:

                        addPatient(
                            patients,
                            doctors,
                            "Inpatient"
                        )

                    case 2:

                        addPatient(
                            patients,
                            doctors,
                            "Outpatient"
                        )

                    case 3:
                        print(
                            "\nExiting the Receptionist Window....."
                        )
                        break

                    case _:
                        print("INVALID OPTION")

        # ====================================================
        # OTHER DESIGNATION
        # ====================================================

        else:

            print("\nAccess denied.")
            print(
                "This staff designation does not have "
                "assigned system permissions."
            )

    except LookupError as e:

        print("Error:", e)

    except ValueError as e:

        print("Invalid staff details:", e)

    except Exception as e:

        print("An unexpected error occurred:", e)



        # ====================================================
        # DOCTOR MENU
        # ====================================================

    #     while True:

    #         print("----- Staff Window ----")

    #         print("1. Patient Access")
    #         print("2. Add Patient")
    #         print("3. Update Patient Vital Signs (New Reading)")
    #         print("4. Exit from Staff window.")
    #         print("\n")

    #         option = input(
    #             "Enter the option you would like to choose: "
    #         )
            
    #         match (int(option)):
    #             case (1):
    #                 # comment: Access a Patient Object
    #                 patientAccess(patients)
    #             case (2):
    #                 # comment: Create and add a new Patient object.
    #                 addPatient()
    #             case (3):
    #                 # comment: Create and associate a new VitalSigns object.
    #                 updatePatientVitals()
    #             case (4):
    #                 # comment: Exit Doctor's window
    #                 print("Exiting the Staff Window.....")
    #                 break
    #             case (_):
    #                 # comment: 
    #                 print("INVALID OPTION")
    #         # end match


    # except LookupError as e:

    #     print("Error:", e)

    # except ValueError as e:

    #     print("Invalid doctor details:", e)