from . import Device


class MobileDevice(Device):
    def __init__(self,id,type,manufacturer,softwareVersion,geolocation=None,engineType="",pollutionEmission=""):
        super(id,type,manufacturer,softwareVersion,geolocation)
        self.engineType=engineType
        self.pollutionEmission=pollutionEmission




