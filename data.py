class useValues:
    def __init__(self, occupants, electricUse, gasUse):
        self.occupants = occupants
        self.electricUse = electricUse
        self.gasUse = gasUse

    def printInfo(self):
        return f"Occupants: {self.occupants}, Electric Use: {self.electricUse}, Gas Use: {self.gasUse}"