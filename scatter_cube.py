import matplotlib.pyplot as plt
import numpy
# x_values = [1, 2, 3, 4, 5]
# y_values = [x ** 3 for x in x_values]
# plt.scatter(x_values, y_values, s=40)
# plt.show()
x_values1 = [numpy.arange(1.0, 5001)]
y_values1 = [x ** 3 for x in x_values1]
plt.scatter(x_values1, y_values1, s=30)

plt.title("cube Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("cube", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.savefig('scatter_cube.png',bbox_inche='tight')
plt.show()

