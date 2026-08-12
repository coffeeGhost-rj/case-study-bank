from datetime import datetime

# This class represents one recorded set of vital signs for a patient.

class VitalSigns():
    def __init__(self, temp, pulse,spo2, recorded_by=None):
        self.setTemp(temp)
        self.setPulse(pulse)
        self.setOxygen(spo2)

        # Stores the exact date and time when this reading was created.
        self.recorded_time = datetime.now()

        self.recorded_by = recorded_by

    def setTemp(self,temp):
        if temp < 30 or temp > 45:
            raise ValueError("Invalid temperature value.")
        else:
            self.temperature = temp

    def setPulse(self, pulse):
        if pulse < 20 or pulse >250:
            raise ValueError("Invalid pulse value.")
        else:
            self.pulse = pulse

    def setOxygen(self,spo2):
        if spo2<0 or spo2>100:
            raise ValueError("Invalid oxygen saturation value.")
        else:
            self.oxygen = spo2


    # def showVitalDetails(self):
        
    #     return ("Temperature: " + str(self.temperature)+ "°C" +
    #             "\nPulse: " + str(self.pulse) + "bpm" +
    #             "\nOxygen saturation : " + str(self.oxygen) + "%" +
    #             "\nRecorded Time: " + self.recorded_time.strftime("%d-%m-%Y  %H:%M:%S")
    #             )

    def showVitalDetails(self):

        vital_details = (
            "Temperature: " + str(self.temperature) + "°C" +
            "\nPulse: " + str(self.pulse) + "bpm" +
            "\nOxygen saturation : " + str(self.oxygen) + "%" +
            "\nRecorded Time: " +
            self.recorded_time.strftime("%d-%m-%Y  %H:%M:%S")
        )

        # Display staff details only when a staff member
        # has recorded the reading.
        recorded_by = getattr(self, "recorded_by", None)
        if recorded_by is not None:

            vital_details = (
                vital_details +
                "\nRecorded By: " + recorded_by.name +
                "\nStaff ID: " + recorded_by.u_id +
                "\nDesignation: " + recorded_by.designation
            )

        return vital_details
        