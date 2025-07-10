class meds:
    def __init__(self, Name, tabs,pill,syrup):
        self.Name = Name
        self.tabs = tabs
        self.pill = pill
        self.syrup = syrup
def ShowAllMeds(MedList=[]):
    for meds in MedList:
        print("1)",meds.Name)
        print("Tableta:",meds.tabs," Pildora:", meds.pill," Jarabe:",meds.syrup)
def MedTake (MedList=[]):
    print("Que medicamento estaria tomando?")
    for meds in MedList:
        print("1)", meds.Name)


