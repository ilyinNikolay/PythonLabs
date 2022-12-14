from tour import Tour
from route import Route
import json

class TravelAgency:
    def __init__(self, number = "", address = "", tours = []):
        self.number = number
        self.address = address
        self.tours = tours
        self.__dict__["tours"] = [i.__dict__ for i in self.tours]
      
    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self)-> str:
        return self.__str__()

def TravelAgencySerialize(TravelAgency, path):
    with open(path, 'w') as outfile:
        json.dump(TravelAgency.__dict__, outfile, indent=4, ensure_ascii = False)
        

def TravelAgencyDeserialize(pas):
    def Decode(obj):
        if "tours" in obj:
            return TravelAgency(obj["number"], obj["address"], [Decode(i) for i in obj["tours"]])
        elif "routes" in obj:
            return Tour(obj["nameT"], [Decode(i) for i in obj["routes"]])
        else:
            return Route(obj["route"], obj["guide"],obj["price"])
    with open(pas) as json_file:
        data = json.load(json_file)
    return Decode(data)

