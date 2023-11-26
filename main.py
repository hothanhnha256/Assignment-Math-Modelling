import pandas as pd
import numpy as np
import numpy.matlib 
from gamspy import Container, Set, Parameter, Variable, Equation, Model, Sum, Sense
solver=Container()
n=8 #loai san pham
m=5 #loai nguyen lieu
S1=np.random.binomial(10,.5,n)
S2=np.random.binomial(10,.5,n) 
S1=np.array(S1)
S2=np.array(S2)
#x,y,z
#gia preorder
l1=np.array([5,5,5,5,5,5,5,5]) #gia san xuat san pham
q1=np.array([17,17,17,17,17,17,17,17]) #gia ban san pham
c1=l1-q1 # coefficients

A = np.random.randint(10, size=(8, 5))
A=np.matrix(A)
print(A)

i=Set(solver, name="i",description="gido",records=["i" + str(x) for x in range (1,n+1)])
j=Set(solver, name="j",description="gido2",records=["j" + str(x) for x in range (1,m+1)])

b=Parameter(    solver,  name="b",  domain=j,  records=np.array([6,6,6,6,6]))
l=Parameter(    solver,   name="l",   domain=i,   records=np.array([5,5,5,5,5,5,5,5]),)
q=Parameter(    solver, name="q",   domain=i,   records=np.array([17,17,17,17,17,17,17,17]),)
s=Parameter(    solver,    name="s",    domain=j,    records=np.array([4,4,4,4,4]),) #gia mua vat lieu vao
c=Parameter(    solver,    name="c",    domain=i,    records=c1,)

s1=Parameter(    solver,    name="scenario 1",    domain=i,    records=S1) #scenario
s2=Parameter(    solver,    name="scenario 2",    domain=i,    records=S2) #scenario
x=Variable(    container=solver,    name="x",    domain=i,    type="positive",    description="koqt1")
y1=Variable(    container=solver,    name="y1",    domain=j,    type="positive",    description="koqt2")
y2=Variable(    container=solver,    name="y2",    domain=j,    type="positive",    description="koqt3")
z1=Variable(    container=solver,    name="z1",   domain=i,    type="positive",    description="koqt4")
z2=Variable(    container=solver,    name="z2",    domain=i,    type="positive",    description="koqt5")

e1=Equation(    solver,    name="spam1",    domain=[i],    definition=z1[i] <= s1[i])
e2=Equation(    solver,    name="spam2",    domain=[i],    definition=z2[i]<=s1[i])

e3=Equation(    solver,    name="spam3",    domain=j,    definition=y2==x-np.multiply(A , z2) )
e4=Equation(    solver,    name="spam4",    domain=j,    definition=y1==x-np.multiply(A, z2) )


result=Model(    solver,
    equations=[e1,e2,e3,e4],
    problem="LP",
    sense=Sense.MIN ,
    objective=Sum((i) ,     1/2*((s1[i]*((l-q)*z1[i]-s1*y1[i])) +  b*x)    +     1/2*((s2[i]*((l-q)*z2[i]-s2*y2[i])) +  b*x)        ),
)

import sys

result.solve(output=sys.stdout)
