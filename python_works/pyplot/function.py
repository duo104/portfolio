import matplotlib.pyplot as plt
x = []
y = []
for i in range(0,1000):
    x.append(i)
    y.append(i**2)
print(x)
print(y)
plt.plot(x,y)
plt.show()