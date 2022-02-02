# Acurite-AdafruitIO
Parses data from rtl_433 decoded output and submits to Adafruit IO.  Specifically written for Acurite temperature sensors, but could easily be adapted to other devices.

## Setup:

### Obtain hardware:
* RTL-SDR Dongle
* Sensors compatible with rtl_433
* Computer such as Raspberry Pi

### Install software:
* [Adafruit IO Python Client Library]([https://github.com/adafruit/Adafruit_IO_Python/)
* [rtl_433](https://github.com/merbanan/rtl_433)

### Configuration:
* Create configuration file and add sensors.  Sample file has examples. Run rtl_433 without piping to the Python script to see received sensor data.
* Humidity and battery feeds will only be sent if configured.
* 'interval' is the time in seconds to wait between submissions to Adafruit IO.  The sensors usually submit data quite often (every 16 seconds for the Acurite "Tower" sensors).  Submitting all updates to IO is wasteful and will consume your quota quickly.
* 'max_temp_delta' is the amount of temperate change that will override 'interval' to post an update sooner.
* Set Adafruit IO username and key.

### Run
```rtl_433 -C customary -p 24 -F json | python3 ~/process_temp.py```

* Set -p to the proper PPM adjustment, if needed.  If not needed, remove.
* For Celsius, remove "-C customary" and change instances of "temperature_F" to "temperature_C" in code.
