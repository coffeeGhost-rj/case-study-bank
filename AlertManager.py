from datetime import datetime


def checkTemperature(temp):

    if temp >= 36.5 and temp <= 37.5:
        return "Temperature: NORMAL "

    elif (temp > 37.5 and temp <=38.5) or (temp<36):
        return "Temperature: WARNING"

    elif temp>38.5:
        return " Temperature: CRITICAL"

    else:
        return "Temperature: EMERGENCY"


def checkPulse(pulse):

    if pulse >=60 and pulse<=100:
        return "Pulse: NORMAL"

    elif (pulse>=50 and pulse<60) or (pulse > 100 and pulse<=120):
        return "Pulse: WARNING"

    elif (pulse < 50 or pulse >120):
        return "Pulse: CRITICAL"


def checkOxygen(oxygen):

    if oxygen>=95:
        return "Oxygen Saturation : NORMAL"

    elif oxygen >=90 and oxygen< 95:
        return "Oxygen Saturation: WARNING"
    else:
        return "Oxygen Saturation: EMERGENCY"

def generateAlert(vitalObj):

    alerts = []

    alerts.append(checkTemperature(vitalObj.temperature))
    alerts.append(checkPulse(vitalObj.pulse))
    alerts.append(checkOxygen(vitalObj.oxygen))

    if "EMERGENCY" in str(alerts):
        alerts.append("Overall Status : EMERGENCY - Immediate attention required.")

    elif "CRITICAL" in str(alerts):
        alerts.append("Overall Status : CRITICAL - Doctor review required.")

    elif "WARNING" in str(alerts):
        alerts.append("Overall Status : WARNING - Monitor patient.")

    else:
        alerts.append("Overall Status : NORMAL - Patient stable.")


    return alerts


    # def __init__(self, msg, status):
    #     # self.msg = msg
    #     # self.status = status
    #     self.set_msg(msg)
    #     self.set_status(status)
    #     self.time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


    # def set_msg(self, msg):
    #     if len(msg)<=0:
    #         raise ValueError("The alert message cannot be Empty")
    #     else:
    #         self.msg = msg

    # def set_status(self,status):

    #     status = ["Normal", "Warning", "Critical"]

    #     if status not in status:
    #         raise ValueError("The alert sent is not valid")
    #     else:
    #         self.status = status


    # def showAlerts(self):
    #     print("Message: ", self.msg)
    #     print("Alert Status: ",self.status)
    #     print("Alert sent at: ", self.time)