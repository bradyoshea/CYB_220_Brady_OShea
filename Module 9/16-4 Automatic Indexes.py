from pathlib import Path
import matplotlib.pyplot as plt
import datetime
import csv

path = Path("death_valley_2021_full.csv")
lines = path.read_text(encoding="utf-8").splitlines()
reader = csv.reader(lines)
header_row = next(reader)

title_index = header_row.index("NAME")
date_index = header_row.index("DATE")
high_index = header_row.index("TMAX")
low_index = header_row.index("TMIN")

dates = []
highs = []
lows = []
for row in reader:
    title = row[title_index]
    date = datetime.datetime.strptime(row[date_index], "%Y-%m-%d")
    dates.append(date)
    high = int(row[high_index])
    highs.append(high)
    low = int(row[low_index])
    lows.append(low)

fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, color="purple", alpha=0.1)
ax.set_title(f"{title} High and Low Temperatures in 2021")
fig.autofmt_xdate()
ax.set_ylim(0, 150)

plt.show()