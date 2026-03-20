from pathlib import Path
import matplotlib.pyplot as plt
import datetime
import csv

path = Path("death_valley_2021_full.csv")
lines = path.read_text(encoding="utf-8").splitlines()
reader = csv.reader(lines)
header_row = next(reader)

dates = []
highs = []
lows = []
for row in reader:
    date = datetime.datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(date)
    high = int(row[6])
    highs.append(high)
    low = int(row[7])
    lows.append(low)

fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, color="purple", alpha=0.1)
ax.set_title("Death Valley High and Low Temperatures in 2021")
fig.autofmt_xdate()
ax.set_ylim(0, 150)

plt.show()

