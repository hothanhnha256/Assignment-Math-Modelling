import numpy as np
import numpy.matlib 
from gamspy import Container, Set, Parameter, Variable, Equation, Model, Sum, Sense
model=Container()
n=8 #loai san pham
m=5 #loai nguyen lieu
S1=np.random.binomial(10,.5,n)
S2=np.random.binomial(10,.5,n) 
S=0.5 #senario
#x,y,z
b=np.array([6,6,6,6,6]) #gia preorder
l=np.array([5,5,5,5,5,5,5,5]) #gia san xuat san pham
q=np.array([8,8,8,8,8,8,8,8]) #gia ban san pham
s=np.array([4,4,4,4,4]) #gia ban ton kho
c=l-q

print(c)
A = np.random.randint(10, size=(8, 5))
print(A)
y=[0] * m
x=[0] * m
z=[0] * n
print("eeeee")
print(y)
i=Set(model, name = "preorder", )
# print(D)
m=5
