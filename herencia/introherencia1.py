class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass
class TrackedVehicle(Vehicle):
    pass
#print (issubclass(trackedVehicle, Vehicle, LandVehicle))

for clas1 in [Vehicle,LandVehicle, TrackedVehicle]:
    for clas2 in [Vehicle,LandVehicle, TrackedVehicle]:
        print (issubclass(clas1, clas2), end="\t")
        print ()
# for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
#      for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
#          print(issubclass(cls1, cls2), end="\t")
#      print()