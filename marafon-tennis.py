from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from more_itertools import chunked
from betting import Bets

csvFile = open("/root/marafon.csv", 'wt')
writer = csv.writer(csvFile)
html = urlopen("https://www.marathonbet.ru/su/popular/Tennis")
bsObj = BeautifulSoup(html, features="lxml")

# -----------------------------------работа с коэффициентами-------------------------------------------#
# выделяем блок с коэффициентами
rows = bsObj.findAll("td", {"class": "height-column-with-price"})  # находим все ячейки с коэффициентами
A = []

for row in rows:
    tabs = row.findAll('span')  # все коэффициенты находятся в теге span
    for tab in tabs:
        A.append(tab.get_text())  # список коэффициентов

coefficients = list(chunked(A, 6))
# print(coefficients)
# -------------------------------------------------------------------------------------------------#

# -------------------------------работа с блоком названий команд-----------------------------------#
array = []
# находим все блоки с названиями команд и добавляем их в список
titles = bsObj.findAll("a", {"class": "member-link"})
for title in titles:
    names = title.findAll('span')
    for name in names:
        array.append(name.get_text())

titles_array = list(chunked(array, 2))
# print(titles_array)

counterstrike = 0
table = []

# соединяем блоки коффициентов и названий команд для большей удобочитаемости
for el in titles_array:
    table.append(coefficients[counterstrike])
    print(f'{titles_array[counterstrike]} || {coefficients[counterstrike]}')
    counterstrike += 1

# -------------------------------------------------------------------------------------------------#
csvFile.close()

# ------------------------------------------анализ вилок-------------------------------------------#

# for el in table:
#     bets = Bets(el[0], el[1], 150, 100, 50)
#     bets.calculate_for_x()

# for el in table:
#     bets = Bets(el[0], el[1], 150, 100, 50)
#     bets.calculate_for_handicap()
k1 = 0
for el in table:
    print(f'{titles_array[k1]}')
    k1 += 1
    bets = Bets(el[0], el[1], 150, 100)
    bets.calculate_for_owerall_win()

