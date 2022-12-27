N = 8888

from random import randint
from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Sum, Avg, RandSum, RandMed, Res, Summary, Range, Length, ListSummary, Mas, Median, RandMas')

(Summary[Range] == sum_(X, for_each = X)) <= X.in_(range_(Range + 1))
print(f"{Sum == Summary[N]}")

(Length[Range] == len_(X, for_each = X)) <= X.in_(range_(Range + 1))
print(f"{Avg == (Summary[N] / Length[N])}")

RandMas = [randint(0, 99) for t in range(0, 100)]
RandMas.sort()
(ListSummary[Mas] == sum_(X, for_each = X)) <= X.in_(Mas)
print(f"{RandSum == ListSummary[RandMas]}")

(Res == Median[Mas]) <= (Res == (Mas[49] + Mas[50]) / 2)
print(f"{RandMed == Median[RandMas]}")
