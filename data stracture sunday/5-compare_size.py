import matplotlib.pyplot as plt
import math
def f(n):
    return n**15*2**n/100
def g(n):
    return 100*n**15
x1=[]
y1=[]
x2=[]
y2=[]

for n in range (0,31):
    y1.append(f(n))
    x1.append(n)
    y2.append(g(n))
    x2.append(n)
plt.plot(x1,y1,label='n^152^n/100',color='red') 
plt.plot(x2,y2,label='100n^15',color='green')   
plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.legend()
plt.show()