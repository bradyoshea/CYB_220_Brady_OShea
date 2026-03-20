import matplotlib.pyplot as plt

cubes = []
values = []
for number in range(1,5_001):
    cube = number ** 3
    cubes.append(cube)
    values.append(number)

fig, ax = plt.subplots()
ax.scatter(values, cubes, c=cubes, cmap=plt.cm.cool, s=30)
ax.set_title('Cubes')

plt.show()