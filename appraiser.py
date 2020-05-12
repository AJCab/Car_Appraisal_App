from tkinter import *
import pickle
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsRegressor
makeVar = None
modelVar = None
VehicleType = None
GearboxVar = None
FuelType = None
Year = None
DamageVar = None
Miles = None



model_opt = None
make_opt = None
vehicleType_opt = None
Gearbox_opt = None
Fuel_opt = None
Damage_opt = None
YearText = None
YearInput = None
MilesText = None
MilesInput = None
HPText = None
HPInput = None
appraise_button = None


def loadData(filename):
    data = pickle.load(open(filename, 'rb'))
    return data

    
def appraise():

    # Make = make_opt.get()
    df = pickle.load(open("Data/default_df.sav", 'rb'))
    print(makeVar.get(), modelVar.get(), vehicleTypeVar.get(), GearboxVar.get(), FuelVar.get(), YearInput.get(), DamageVar.get(), MilesInput.get(), HPInput.get())

    print(df.shape)
    df["vehicleType_" + vehicleTypeVar.get()] = 1
    df["yearOfRegistration"] = int(YearInput.get())
    df["gearbox_" + GearboxVar.get()] = 1
    df["HPower"] = int(HPInput.get())
    df["model_" + modelVar.get()] = 1
    df["miles"] = int(MilesInput.get())
    df["fuelType_"+ FuelVar.get()] = 1
    df["brand_" + makeVar.get()] = 1
    df["notRepairedDamage_" + DamageVar.get()] = 1

    # data_in=[[data[1][vehicleTypeVar.get()],int(YearInput.get()),data[2][GearboxVar.get()], int(HPInput.get()),data[3][modelVar.get()], int(MilesInput.get()), int(YearInput.get()), data[4][FuelVar.get()], data[5][makeVar.get()], data[6][DamageVar.get()]]]
    # df = pd.DataFrame(columns=["vehicleType","yearOfRegistration","gearbox","HPower","model","miles","monthOfRegistration","fuelType","brand","notRepairedDamage"], data=data_in)
    print(df)
    print(data[0].predict([df]))

    ValueVar.set("$" +str(round(data[0].predict([df])[0], 2)))
    return

window = Tk()
window.geometry("500x500")

window.title("CSC 310 Car Appraiser")
data = loadData("Data/data_structures-knn3.sav")

title = Label(window, textvariable=StringVar(window,"Enter your vehicles information"))
MakeList = [key for key in data[5].keys()]
MakeList.sort()

ModelList = [key for key in data[3].keys()]
ModelList.sort()

VehicleTypeList = [key for key in data[1].keys()]
VehicleTypeList.sort()

GearboxList = [key for key in data[2].keys()]
GearboxList.sort()

FuelList = [key for key in data[4].keys()]
FuelList.sort()

modelVar = StringVar(window, "Choose Model")
model_opt = OptionMenu(window, modelVar , *ModelList)
model_opt.config(width=10, font=('Helvetica', 12))

makeVar = StringVar(window, "Choose Make")
make_opt = OptionMenu(window, makeVar, *MakeList)
make_opt.config(width=10, font=('Helvetica', 12))

vehicleTypeVar = StringVar(window, "Choose Vehicle Type")
vehicleType_opt = OptionMenu(window, vehicleTypeVar, *VehicleTypeList)
vehicleType_opt.config(width=15, font=('Helvetica', 12))

GearboxVar = StringVar(window, "Choose Gearbox Type")
Gearbox_opt = OptionMenu(window, GearboxVar, *GearboxList)
Gearbox_opt.config(width=15, font=('Helvetica', 12))

FuelVar = StringVar(window, "Choose Fuel Type")
Fuel_opt = OptionMenu(window, FuelVar, *FuelList)
Fuel_opt.config(width=15, font=('Helvetica', 12))

DamageVar = StringVar(window, "Unrepaired Damage?")
DamageList = [key for key in data[6].keys()]
Damage_opt = OptionMenu(window, DamageVar, *DamageList)
Damage_opt.config(font=('Helvetica', 12))


YearVar = StringVar(window,"Vehicle Year")
YearText = Label(window, textvariable=YearVar)
YearText.config(font=('Helvetica', 12))
YearInput = Entry(window)

MilesVar = StringVar(window,"Mileage")
MilesText = Label(window, textvariable=MilesVar)
MilesText.config(font=('Helvetica', 12))
MilesInput = Entry(window)

HPVar = StringVar(window,"Horsepower")
HPText = Label(window, textvariable=HPVar)
HPText.config(font=('Helvetica', 12))
HPInput = Entry(window)

ValueVar = StringVar(window, "$0")
ValueText = Label(window, textvariable=ValueVar)
ValueText.config(font=('Helvetica', 24))

appraise_button = Button(text='Appraise!', command=appraise)

title.pack()
make_opt.pack()
model_opt.pack()
vehicleType_opt.pack()
Gearbox_opt.pack()
Fuel_opt.pack()
Damage_opt.pack()
YearText.pack()
YearInput.pack()
MilesText.pack()
MilesInput.pack()
HPText.pack()
HPInput.pack()




appraise_button.pack()

ValueText.pack()





window.mainloop()
