# matplotlib is library which used in ML for Data visualization which allows for better learning and data underdstanding
import matplotlib.pyplot as plt

a = [1, 2, 3, 4, 5, 6]
b = [2, 4, 6, 8, 10, 12]

# create line which links a and b
plt.plot(a, b)
plt.title("Line-chart Example") # title of our chart
plt.xlabel("X-axis") # label in X axis 
plt.ylabel("Y-axis") # Y axis label
plt.show() # shows the graph
