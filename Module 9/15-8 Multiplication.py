import plotly.express as px
import random

results = []
for roll_num in range(1_000):
    first_die = random.randint(1, 6)
    second_die = random.randint(1, 6)
    result = first_die * second_die
    results.append(result)

possible_results = range(1, 37)
frequencies = []
for value in possible_results:
    frequency = results.count(value)
    frequencies.append(frequency)

fig = px.bar(x=possible_results, y=frequencies)
fig.show()