import json
from route import Route
from tour import Tour
from travelAgency import TravelAgency, TravelAgencySerialize, TravelAgencyDeserialize

firstTravelAgency = TravelAgency("1", "Комсомольский проспект, 62", 
                [Tour("Уральский Марс и Шарташский каменные палатки", [
                    Route("1", "Разумовская Е.В.", "1400"),
                    Route("2","Новикова Н.В.", "18700"),
                    Route("3","Корякина П.А.", "11500"),
                    Route("4","Петров А.Д.","5000")]),
                Tour("Верхотурье - Меркушино", [
                    Route("1", "Гордеев К.М.", "3200"),
                    Route("2","Щукин Ю.А", "5500"),
                    Route("3","Кононов В.В","2000"),
                    Route("4","Попов А.А.","1500")])])

TravelAgencySerialize(firstTravelAgency, "firstS.json")
secondTravelAgency = TravelAgencyDeserialize("firstS.json")

print(secondTravelAgency.__dict__)
