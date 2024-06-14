import matplotlib.pyplot as plt
import math
def f(n):
    return 8**math.log(n)
def g(n):
    return 3*n**7 +7*n
x1=[]
y1=[]
x2=[]
y2=[]

for n in range (0,31):
    y1.append(f(n))
    x1.append(n)
    y2.append(g(n))
    x2.append(n)
plt.plot(x1,y1,label='8^logn',color='red') 
plt.plot(x2,y2,label='3n^7 + 7n',color='green')   
plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.legend()
plt.show()