import matplotlib.pyplot as plt
from Random_Walk import RandomWalk

a = int(input("please input number"))
rw = RandomWalk(a)
rw.fill_walk()
point_number = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues
            , edgecolors='none', s=15)

plt.show()
