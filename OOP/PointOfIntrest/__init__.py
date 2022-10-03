class PointOfIntrest:
    def __init__(self,name,deviceList=[],geolocation=[]):
        self.name=name
        self.deviceList=deviceList
        self.geolocation=geolocation

    def addDevice(self,device):
        self.deviceList.append(device)

    def removeDevice(self,device):
        """This method works under index of item values"""
        indexToRemove=-1
        for index,dev in enumerate(self.deviceList):
            if dev.id==device.id:
                indexToRemove=index
        if indexToRemove!=-1:
            self.deviceList.pop(indexToRemove)

    def updateDevice(self,device):
        """This method works under index of item values"""
        indexToEdit = -1
        for index, dev in enumerate(self.deviceList):
            if dev.id == device.id:
                indexToEdit = index
        if indexToEdit != -1:
            self.deviceList[indexToEdit]=device