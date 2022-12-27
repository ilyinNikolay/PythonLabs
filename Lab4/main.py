from functools import reduce
import csv

with open("Mall_Customers.csv", "r") as file:
    keys = file.readline()
    reader = csv.reader(file, delimiter=",")
    dataset = [x for x in reader]


def to_dictionary(keys, values):
    dictionary = {}
    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]
    return dictionary


keys = list(keys.split(","))
dataset = list(map(lambda x: to_dictionary(keys, x), dataset))

ageNotes = list(map(lambda x: int(x['Age']), dataset))
ageSum = reduce(lambda x, y: x + y, ageNotes)

annualIncomes = list(map(lambda x: int(x['Annual Income (k$)']), dataset))
annualIncomeSum = reduce(lambda x, y: x + y, annualIncomes)

avgIncome = round(annualIncomeSum / len(dataset), 2)
avgAge = round(ageSum / len(dataset), 2)

print(f"Количество записей: {len(dataset)}\n"
      f"Средний возраст покупателей: {avgAge}\n"
      f"Среднегодовой доход покупателей: {avgIncome} тыс. долларов")
