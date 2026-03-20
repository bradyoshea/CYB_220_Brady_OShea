from pathlib import Path
import matplotlib.pyplot as plt
import datetime
import csv

path = Path("death_valley_2021_full.csv")
lines = path.read_text(encoding="utf-8").splitlines()
reader = csv.reader(lines)
header_row = next(reader)

dates = []
precipitation = []
snow = []
for row in reader:
    date = datetime.datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(date)
    precip = float(row[3])
    precipitation.append(precip)
    sno = float(row[4])
    snow.append(sno)

fig, ax = plt.subplots()
ax.plot(dates, precipitation, color="blue")
ax.plot(dates, snow, color="lightblue")
ax.set_title("Death Valley Precipitation and Snowfall in 2021")
fig.autofmt_xdate()

plt.show()