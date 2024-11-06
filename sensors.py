import shared

# The main device that contains the sensors
device              = {
    "identifiers": [
        "rpi3_statistics"
    ],
    "name": "RPI Status Monitor",
    "model": "3b",
    "manufacturer": "Raspberry"
}

# Sensor definition
# https://developers.home-assistant.io/docs/core/entity/sensor/#available-device-classes
sensors = {
    #  psutil.sensors_temperatures()['cpu_thermal'][0].current
    'cpu_temp': {
        "name": "CPU Temperature",
        "state": "measurement",
        "unit": "°C",
        "type": "TEMPERATURE",
        "icon": "mdi:thermometer"
    },

    # psutil.sensors_temperatures()['w1_slave_temp'][0].current
    'ext_temp': {
        "name": "External Temperature",
        "state": "measurement",
        "unit": "°C",
        "type": "TEMPERATURE",
        "icon": "mdi:thermometer"
    },

    # psutil.cpu_percent()
    'cpu': {
        "name": "CPU Usage",
        "state": "measurement",
        "unit": "%",
        "type": "BATTERY",
        "icon": "mdi:cpu-64-bit"
    },

    # psutil.virtual_memory().percent
    'memory': {
        "name": "Memory Usage",
        "state": "measurement",
        "unit": "%",
        "type": "BATTERY",
        "icon": "mdi:memory"
    },

    # psutil.disk_usage('/').percent
    'disk': {
        "name": "Disk Usage",
        "state": "measurement",
        "unit": "%",
        "type": "BATTERY",
        "icon": "mdi:harddisk"
    },
}

# Connects to Home Assistant and creates the sensors if needed
MqqtToHa    = shared.MqqtToHa(device, sensors)
