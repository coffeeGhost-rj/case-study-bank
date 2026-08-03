from datetime import datetime

class VitalSigns():
    def __init__(self, temp, pulse,spo2):
        self.setTemp(temp)
        self.setPulse(pulse)
        self.setOxygen(spo2)

        self.recorded_time = datetime.now()

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


    def showVitalDetails(self):
        
        return ("Temperature: " + str(self.temperature)+ "°C" +
                "\nPulse: " + str(self.pulse) + "bpm" +
                "\nOxygen saturation : " + str(self.oxygen) + "%" +
                "\nRecorded Time: " + self.recorded_time.strftime("%d-%m-%Y  %H:%M:%S")
                )
        