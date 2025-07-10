class meds:
    def __init__(self, Name, tabs=0,pill=0,syrup=0):
        self.Name = Name
        self.tabs = tabs
        self.pill = pill
        self.syrup = syrup
MedList=[]
def ShowAllMeds(MedList=[]):
    contDisp=0
    for meds in MedList:
        contDisp=contDisp+1
        print(contDisp,")",meds.Name)
        print("Tableta:",meds.tabs," Pildora:", meds.pill," Jarabe:",meds.syrup)
def MedTake (MedList=[]):
    contDisp=0
    print("Que medicamento estaria tomando?")
    for meds in MedList:
        print(contDisp,")",meds.Name)

    MedImput= int(input("Ingrese el numero del medicamento a tomar:"))
    if MedImput >0:
        print("En que presentacion estaria tomando ",MedList[MedImput-1].Name)
        print("1)Tableta (",MedList[MedImput-1].tabs," en existencia)")
        print("2)Pildora (",MedList[MedImput-1].pill," en existencia)")
        print("3)Jarabe (",MedList[MedImput-1].syrup," en existencia)")
        KindImput= int(input("Ingrese el numero del tipo de presentacion:"))
        if KindImput >0&KindImput<4:
            if KindImput == 1:
                MedList[MedImput-1].tabs = MedList[MedImput-1].tabs - 1
            elif KindImput == 2:
                MedList[MedImput-1].pill = MedList[MedImput-1].pill - 1
            elif KindImput == 3:
                MedList[MedImput-1].syrup = MedList[MedImput-1].syrup - 1
        elif KindImput <1|KindImput>3:
            print("Dato Invalido")
    elif MedImput < 1:
        print("Dato Invalido")
def MedAdd(MedList=[]):
    print("Cual es el nombre del medicamento que desea agregar?")
    medname= input("")
    print("En que presentacion se estaria agregando?")
    print("1)Tableta")
    print("2)Pildora")
    print("3)Jarabe")
    KindImput = int(input("Ingrese el numero del tipo de presentacion:"))
    if KindImput >0&KindImput<4:
        print("Cuantas unidades se estarian recibiendo?")
        MedCuant= int(input(""))
        if MedCuant >0:
            if KindImput == 1:
                NewMed= meds(medname,MedCuant)
            elif KindImput == 2:
                NewMed= meds(medname,0,MedCuant)
            elif KindImput == 3:
                NewMed= meds(medname,0,0,MedCuant)

        elif MedCuant <1:
            print("Dato Invalido")
    elif KindImput <1|KindImput>3:
        print("Dato Invalido")