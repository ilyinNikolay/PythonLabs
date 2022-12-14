import json;

class Route:
    def __init__(self, route = "", guide = "", price = 0):
        self.route = route
        self.guide = guide
        self.price = price
     
    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self)-> str:
        return self.__str__()

