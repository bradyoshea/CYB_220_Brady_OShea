from pathlib import Path
import matplotlib.pyplot as plt
import datetime
import csv

path2 = Path("sitka_weather_2021_full.csv")
lines2 = path2.read_text(encoding="utf-8").splitlines()
reader2 = csv.reader(lines2)
header_row2 = next(reader2)

dates2 = []
highs2 = []
lows2 = []
for row in reader2:
    date = datetime.datetime.strptime(row[2], "%Y-%m-%d")
    dates2.append(date)
    high = int(row[7])
    highs2.append(high)
    low = int(row[8])
    lows2.append(low)

fig, ax = plt.subplots()
ax.plot(dates2, highs2, color="red", alpha=0.5)
ax.plot(dates2, lows2, color="blue", alpha=0.5)
ax.fill_between(dates2, highs2, lows2, color="purple", alpha=0.1)
ax.set_title("Sitka High and Low Temperatures in 2021")
fig.autofmt_xdate()
ax.set_ylim(0, 150)

plt.show()