import matplotlib.pyplot as plt

# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]

#用列表进行循环数据作图
x_vaules =list(range(1,1001))
y_vaules =[x**2 for x in x_vaules]
plt.scatter(x_vaules,y_vaules,c='red',edgecolors='none',s=40)
#plt.scatter(input_values,squares,s=200)

plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square", fontsize=14)
plt.tick_params(axis='both', labelsize=14)

#保存图像。将保存在文件所在的目录内
plt.savefig('square_plot.png', bbox_inche='tight')




plt.show()