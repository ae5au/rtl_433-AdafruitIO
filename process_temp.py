# rtl_433 -C customary -p 24 -F json | python3 ~/process_temp.py
# for Celsius, remove "-C customary" and change instances of "temperature_F" to "temperature_C"
# set -p to be PPM error

import sys
import time
import json
from Adafruit_IO import Client, Feed

from process_temp_config import sensors
from process_temp_config import secrets

for sensor in sensors:
    sensor["last_update"] = 0
    sensor["last_temp"] = -999

aio = Client(secrets['aio_username'], secrets['aio_key'])

lastline = ""

for line in sys.stdin:
    if line == lastline:
        continue
    lastline = line
    reading = json.loads(line)
    reading_time = time.monotonic()
    sensor = [s for s in sensors if s['id'] == reading.get("id") and s['model'] == reading.get("model")]
    if len(sensor) == 0:
        print("Sensor not configured:")
        print(line)
    elif len(sensor) > 1:
        print("Multiple sensors configured:")
        print(line)
    else:
        sensor = sensor[0]
        print("{:>10} {} {} ".format(reading.get("id"),reading.get("channel"),reading.get("temperature_F")),end = '')
        if (sensor["last_update"] + sensor["interval"] < reading_time) or (abs(sensor["last_temp"] - reading.get("temperature_F")) > sensor["max_temp_delta"]):
            try:
                aio.send_data(sensor["feed"], reading["temperature_F"])
                print("Posted: Temp",end = '')
                if sensor.get("humidity_feed"):
                    aio.send_data(sensor["humidity_feed"], reading["humidity"])
                    print(", Humidity",end = '')
                if sensor.get("battery_feed"):
                    aio.send_data(sensor["battery_feed"], reading["battery_ok"])
                    print(", Battery",end = '')
                sensor["last_update"] = reading_time
                sensor["last_temp"] = reading.get("temperature_F")
            except:
                print("Unexpected error:", sys.exc_info()[0])
    print("")
