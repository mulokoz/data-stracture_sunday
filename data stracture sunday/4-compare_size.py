import matplotlib.pyplot as plt
import math
def f(n):
    return 5*n**5
def g(n):
    return math.factorial(n)
x1=[]
y1=[]
x2=[]
y2=[]

for n in range (0,31):
    y1.append(f(n))
    x1.append(n)
    y2.append(g(n))
    x2.append(n)
plt.plot(x1,y1,label='5*n**5',color='red') 
plt.plot(x2,y2,label='n!',color='green')   
plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.legend()
plt.show()