class Device:
    def __init__(self,id,type,manufacturer,softwareVersion,geolocation=None):
        self.id = id
        self.type = type
        self.manufacturer = manufacturer
        self.softwareVersion  =softwareVersion
        self.geolocation = geolocation