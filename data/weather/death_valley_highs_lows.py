import csv
import matplotlib.pyplot as plt 
from datetime import datetime

filename = 'C:/Users/Kceni/Desktop/personal_projects/math/data/weather/2422763.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
        if column_header == 'TMAX':
            max = index
        if column_header == 'TMIN':
            min = index
    
    highs, dates, lows = [], [], []
    for row in reader:
        name = row[1]
        date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[max])
            low = int(row[min])
        except ValueError:
            print(f"Missing data for {date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(date)

#Наснесение данных на диаграмму
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Форматирование диаграммы
plt.title(f"Daily high and low temperatures - 2018\n{name}", fontsize=20)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

#Назначение диапазона для оси y
ax.set_ylim([10, 130])

plt.show()