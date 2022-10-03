from . import Device


class ActuatorDevice(Device):
    def __init__(self,id,type,manufacturer,softwareVersion,geolocation=None,operatingValue=0.0):
        super(id, type, manufacturer, softwareVersion, geolocation)
        self.operatingValue = operatingValue