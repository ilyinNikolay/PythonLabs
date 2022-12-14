from route import Route
import json

class Tour:
    def __init__(self, nameT = "", routes = []):
        self.nameT = nameT
        self.routes = routes
        self.__dict__["routes"] = [i.__dict__ for i in self.routes] 
     
    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self)-> str:
        return self.__str__()
