import csv
import matplotlib.pyplot as plt 
from datetime import datetime

filename = 'C:/Users/Kceni/Desktop/personal_projects/math/data/weather/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    prcps, dates = [], []
    for row in reader:
        prcp = float(row[3])
        prcps.append(prcp)
        date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(date)

#Наснесение данных на диаграмму
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, prcps, c='red', alpha=0.5)

#Форматирование диаграммы
plt.title("Daily precipitations - 2018", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)


plt.show()

