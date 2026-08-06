from datetime import datetime

# methods to check the vitals to generate alerts
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


# method to generate alerts | takes the vitalObj as parameter and outputs the overall citals status
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
