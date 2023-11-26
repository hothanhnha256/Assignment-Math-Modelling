import numpy as np
import numpy.matlib 
from gamspy import Container, Set, Parameter, Variable, Equation, Model, Sum, Sense
model=Container()
solver=Container()
n=8 #loai san pham
m=5 #loai nguyen lieu
S1=np.random.binomial(10,.5,n)
S2=np.random.binomial(10,.5,n) 
S=0.5 #senario
S1=np.array(S1)
S2=np.array(S2)
#x,y,z
b=np.array([6,6,6,6,6]) #gia preorder
l=np.array([5,5,5,5,5,5,5,5]) #gia san xuat san pham
q=np.array([8,8,8,8,8,8,8,8]) #gia ban san pham
s=np.array([4,4,4,4,4]) #gia ban ton kho
c=l-q # coefficients
#gia preorder
l1=np.array([5,5,5,5,5,5,5,5]) #gia san xuat san pham
q1=np.array([17,17,17,17,17,17,17,17]) #gia ban san pham
c1=l1-q1 # coefficients


print(c)
A = np.random.randint(10, size=(8, 5))
A=np.matrix(A)
print(A)
y=[0] * m
x=[0] * m
z=[0] * n

print(y)
i=Set(model, name = "preorder",)
j=Set(model, name = "optimize",)

i=Set(solver, name="i",description="gido",records=["i" + str(x) for x in range (1,n+1)])
j=Set(solver, name="j",description="gido2",records=["j" + str(x) for x in range (1,m+1)])

b=Parameter(
    solver,
    name="b",
    domain=j,
    records=np.array([6,6,6,6,6]),
)
l=Parameter(
    solver,
    name="l",
    domain=i,
    records=np.array([5,5,5,5,5,5,5,5]),
)
q=Parameter(
    solver,
    name="q",
    domain=i,
    records=np.array([17,17,17,17,17,17,17,17]),
)
s=Parameter(
    solver,
    name="s",
    domain=j,
    records=np.array([4,4,4,4,4]),
)
c=Parameter(
    solver,
    name="c",
    domain=i,
    records=c1,
)

s1=Parameter(
    solver,
    name="S1",
    domain=i,
    records=S1
)
s2=Parameter(
    solver,
    name="S2",
    domain=i,
    records=S2
)
x=Variable(
    container=solver,
    name="x",
    domain=i,
    type="positive",
    description="koqt"
)
y1=Variable(
    container=solver,
    name="y1",
    domain=j,
    type="positive",
    description="koqt"
)
y2=Variable(
    container=solver,
    name="y2",
    domain=j,
    type="positive",
    description="koqt"
)
z1=Variable(
    container=solver,
    name="z1",
    domain=i,
    type="positive",
    description="koqt"
)
z2=Variable(
    container=solver,
    name="z2",
    domain=i,
    type="positive",
    description="koqt"
)

e1=Equation(
    solver,
    name="spam1",
    domain=[i],
    definition=z1[i] <= s1[i]
)
e2=Equation(
    solver,
    name="spam2",
    domain=[i],
    definition=z2[i]<=s1[i]
)

e3=Equation(
    solver,
    name="spam3",
    domain=[i,j],
    definition=y1[j] == (x[i]-np.multiply(A, z1[i]))
)
e4=Equation(
    solver,
    name="spam4",
    domain=[i,j],
    definition=y2[j] == (x[i]-np.multiply(A,z2[i]))
)


result=Model(
    solver,
    equations=[e1,e2,e3,e4],
    problem="LP",
    sense=Sense.MIN ,
    objective=Sum((i) ,     1/2*((S1[i]*((l-q)*z1[i]-s*y1[i])) +  c*x)    +     1/2*((S2[i]*((l-q)*z2[i]-s*y2[i])) +  c*x)        ),
)
import sys

result.solve(output=sys.stdout)