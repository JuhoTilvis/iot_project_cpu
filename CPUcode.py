import os
import time
import requests


WRITE_KEY = "H98IG5IY5RRHEKZM"
CHANNEL_ID = "2119319"


def get_cpu_temperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return float(res.replace("temp=", "").replace("'C\n", ""))


while True:

    cpu_temp = get_cpu_temperature()

    response = requests.post("https://api.thingspeak.com/update",
                             params={"api_key": WRITE_KEY, "field1": cpu_temp})

    print("Response: {}".format(response.content))

    time.sleep(15)
