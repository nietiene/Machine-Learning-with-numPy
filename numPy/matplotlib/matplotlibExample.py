# matplotlib is library which used in ML for Data visualization which allows for better learning and data underdstanding!
import matplotlib.pyplot as plt

# a = [1, 2, 3, 4, 5, 6]
# b = [2, 4, 6, 8, 10, 12]

# # 1. plt.plot() -> create line which links a and b used for show relationships btn data
# plt.plot(a, b)
# plt.title("Line-chart Example") # title of our chart
# plt.xlabel("X-axis") # label in X axis 
# plt.ylabel("Y-axis") # Y axis label
# plt.show() # shows the graph

# # 2. plt.bar() -> used for compare categories
# categories = ["Banana", "Apples", "Cherries"]
# price = [10, 20, 30]

# plt.bar(categories, price)
# plt.title("Bar chart Example")
# plt.xlabel("Fruits")
# plt.ylabel("Price")
# plt.show()

# 3. plt.histogram() -> is used for data distribution
# how it works it find minimum and maximum
# data = [20, 87, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27]
# # bins divide the whole range into into 5 intervals
# # find bin width => max - min / nbr of bins
# # create bin range min + bin range do it until you exceed to max number 
# plt.hist(data, bins=5, color="orange")
# plt.title("Histogram Example")
# plt.xlabel("Range")
# plt.ylabel("Frequency")
# plt.show()

# 4. plt.scatter -> is used to show also relationship  study hours vs exam scores
hour = [5, 7, 8, 7, 6, 9, 5]
scores = [99, 86, 87, 88, 100, 86, 103]

plt.scatter(hour, scores)
plt.title("Scatter chart example")
plt.xlabel("X-axis")
plt.ylabel("Y-Axis")
plt.show()