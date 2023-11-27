import numpy as np
import numpy.matlib 
import pandas as pd
from gamspy import Container, Set, Parameter, Variable, Equation, Model, Sum, Sense
solver=Container()
n=8 #loai san pham
m=5 #loai nguyen lieu
S1=np.random.binomial(10,.5,n)
S2=np.random.binomial(10,.5,n) 
S=0.5 #senario
S1=np.array(S1)
S2=np.array(S2)
#x,y,z
#gia preorder

A = np.random.randint(10, size=(8, 5))
A=np.array(A)

i=Set(solver, name="i",records=["i" + str(x) for x in range (1,n+1)], description="Product index")
j=Set(solver, name="j",records=["j" + str(x) for x in range (1,m+1)], description="Material index")
b = Parameter(    container=solver, name="preorder_cost", domain=j, records=np.array([6,6,6,6,6]))

l = Parameter(    container=solver, name="cost_to_made_product", domain=i, records=np.array([5,5,5,5,5,5,5,5]))

q = Parameter(    container=solver, name="revenue", domain=i, records=np.array([17,17,17,17,17,17,17,17]))

s= Parameter(   container=solver, name="revenue_when_sell_material", domain=j, records=np.array([4,4,4,4,4]))

A_1=Parameter(    solver,    name="Material_per_product",    domain=[i,j],    records=A)

s1=Parameter(   solver,    name="Scenario1",    domain=i,    records=S1)

s2=Parameter(    solver,    name="Scenario2",    domain=i,    records=S2)
print(b.records)
print(l.records)
print(q.records)
print(s.records)
print(A_1.records)
print(s1.records)
print(s2.records)

x=Variable(    container=solver,    name="nguyen_lieu_order_truoc",    domain=j,    type="positive",    description="koqt")
y1=Variable(    container=solver,    name="nguyen_lieu_du_th1",    domain=j,    type="positive",    description="koqt")
y2=Variable(    container=solver,    name="nguyen_lieu_du_th2",    domain=j,    type="positive",    description="koqt")
z1=Variable(    container=solver,    name="san_pham_san_xuat_th1",    domain=i,    type="positive",    description="koqt")
z2=Variable(    container=solver,    name="san_pham_san_xuat_th2",    domain=i,    type="positive",    description="koqt")

e1=Equation(    solver,    name="e1",    domain=[i],    definition=z1[i]<=s1[i])
e2=Equation(    solver,    name="e2",    domain=[i],    definition=z2[i]<=s1[i])

e3=Equation(    solver,    name="e3",    domain=[i,j],   definition=y1 == x-A_1*z1)
e4=Equation(    solver,    name="e4",    domain=[i,j],    definition=y2 == x-A_1*z2)

print(b.records)
print(l.records)
print(q.records)
print(s.records)

result=Model(
    solver,
    equations=[e1,e2,e3,e4],
    problem="LP",
    sense=Sense.MIN ,
    objective=b*x+1/2*((l-q)*z1-s*y1)+1/2*((l-q)*z2-s*y2),
    name="solver"
)
import sys
result.solve()
print(x.records)