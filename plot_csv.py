from turtle import color
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

data = np.loadtxt("data/pcloud01.csv")

print(data.shape)

for p in data:
    ax.scatter(p[0],p[1],p[2],s=3,color="red")
    ax.set_xlim([-0.5,0.5])
    ax.set_ylim([-0.5,0.5])
    ax.set_zlim([0,1])

plt.show()