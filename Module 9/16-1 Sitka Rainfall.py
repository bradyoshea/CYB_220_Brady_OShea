from pathlib import Path
import matplotlib.pyplot as plt
import datetime
import csv

path = Path("sitka_weather_2021_full.csv")
lines = path.read_text(encoding="utf-8").splitlines()
reader = csv.reader(lines)
header_row = next(reader)

dates = []
precipitation = []
for row in reader:
    date = datetime.datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(date)
    precip = float(row[5])
    precipitation.append(precip)

fig, ax = plt.subplots()
ax.plot(dates, precipitation)
ax.set_title("Sitka Precipitation in 2021")
fig.autofmt_xdate()

plt.show()



