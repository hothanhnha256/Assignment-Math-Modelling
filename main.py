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
lrecord=np.array(np.random.randint(1,5,size=(8)))
qrecord=lrecord+np.array(np.random.randint(10,20,size=(8)))

srecord=np.array(np.random.randint(3,5,size=(5)))

brecord=srecord+np.array(np.random.randint(3,5,size=(5)))
A = np.random.randint(1,10, size=(8, 5))
A=np.array(A)

i=Set(solver, name="i",records=["i" + str(x) for x in range (1,n+1)], description="Product index")
j=Set(solver, name="j",records=["j" + str(x) for x in range (1,m+1)], description="Material index")
b = Parameter(    container=solver, name="preorder_cost", domain=j, records=brecord)

l = Parameter(    container=solver, name="cost_to_made_product", domain=i, records=lrecord)

q = Parameter(    container=solver, name="revenue", domain=i, records=qrecord)

s= Parameter(   container=solver, name="revenue_when_sell_material", domain=j, records=srecord)

A_1=Parameter(    solver,    name="Material_per_product",    domain=[i,j],    records=A)

s1=Parameter(   solver,    name="Scenario1",    domain=i,    records=S1)

s2=Parameter(    solver,    name="Scenario2",    domain=i,    records=S2)
# print(b.records)
# print(l.records)
# print(q.records)
# print(s.records)
# print(A_1.records)
# print(s1.records)
# print(s2.records)

x=Variable(    container=solver,    name="nguyen_lieu_order_truoc",    domain=j,    type="positive",    description="koqt")
y1=Variable(    container=solver,    name="nguyen_lieu_du_th1",    domain=j,    type="positive",    description="koqt")
y2=Variable(    container=solver,    name="nguyen_lieu_du_th2",    domain=j,    type="positive",    description="koqt")
z1=Variable(    container=solver,    name="san_pham_san_xuat_th1",    domain=i,    type="positive",    description="koqt")
z2=Variable(    container=solver,    name="san_pham_san_xuat_th2",    domain=i,    type="positive",    description="koqt")

e1=Equation(    solver,    name="e1",    domain=[i])
e1[i]=z1[i]<=s1[i]
e2=Equation(    solver,    name="e2",    domain=[i])
e2[i]=z2[i]<=s2[i]
e3=Equation(    solver,    name="e3",   domain=[j])
e3[j]=y1[j]==x[j]-A_1*z1
e4=Equation(    solver,    name="e4",domain=[j])
e4[j]=y2[j]==x[j]-A_1*z2



result=Model(
    solver,
    
    name="solver",
    equations=solver.getEquations(),
    problem="LP",
    sense=Sense.MIN ,
    objective=b*x+1/2*((l-q)*z1-s*y1)+1/2*((l-q)*z2-s*y2)
)
import sys
result.solve()
print(x.records)