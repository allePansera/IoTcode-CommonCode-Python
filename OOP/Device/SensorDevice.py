from . import Device


class SensorDevice(Device):
    def __init__(self, id, type, manufacturer, softwareVersion, geolocation=None, lastMeasurement=0.0):
        super(id, type, manufacturer, softwareVersion, geolocation)
        self.lastMeasurement = lastMeasurement