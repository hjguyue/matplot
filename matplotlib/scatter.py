# .*.coding : utf-8 .*.
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,20,2)
y = np.arange(0,20,2)

print x
print y

# plt.figure()
plt.scatter(x,y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('X * Y')

plt.show()