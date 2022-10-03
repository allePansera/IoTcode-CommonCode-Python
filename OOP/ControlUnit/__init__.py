class ControlUnit:
    def __init__(self,pointList=[]):
        self.pointList = pointList

    def addPoint(self,pointOfIntrest):
        self.pointList.append(pointOfIntrest)

    def deletePoint(self,pointOfIntrest):
        """This method works under index of item values"""
        indexToRemove = -1
        for index, PoI in enumerate(self.pointList):
            if PoI.name == pointOfIntrest.name:
                indexToRemove = index
        if indexToRemove != -1:
            self.pointList.pop(indexToRemove)

    def updatePoint(self,pointOfIntrest):
        """This method works under index of item values"""
        indexToEdit = -1
        for index, PoI in enumerate(self.pointList):
            if PoI.name == pointOfIntrest.name:
                indexToEdit = index
        if indexToEdit != -1:
            self.pointList[indexToEdit]=pointOfIntrest