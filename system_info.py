from __future__ import division
from subprocess import PIPE, Popen
from time import sleep
import psutil
import sensors

#https://psutil.readthedocs.io/en/latest/

while True:
    val = psutil.sensors_temperatures()['cpu_thermal'][0].current
    sensors.MqqtToHa.send_value("CPU Temperature", val)

    val = psutil.sensors_temperatures()['w1_slave_temp'][0].current
    sensors.MqqtToHa.send_value("External Temperature", val)

    val = psutil.cpu_percent()
    sensors.MqqtToHa.send_value("CPU Usage", val)

    val = psutil.virtual_memory().percent
    sensors.MqqtToHa.send_value("Memory Usage", val)

    val = psutil.disk_usage('/').percent
    sensors.MqqtToHa.send_value("Disk Usage", val)

    sleep(10)