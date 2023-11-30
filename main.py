print("---------------Start Program!-----------------\n")
#! convert the sample problem into BTL
    #* Indices (Sets):
    #*             i = product, j = material
    #* Parameters:
    #*             b = pre-order_cost, l = production_cost, q = sale, s = inventory_cost, d = demand, c= l-q , a = maxtrix [i,j]
    #* Decision variables:
    #*             x = pre-order_material, y = inventory, z = production
    #* Constraints:
    #*             i,j > 0
    #*             aij >=0
    #*             sj < bj
    #*             0 <= z <= d
    #*             y >= 0
    #*             y = x - A.T*z
    #*             Objective Function: 
    #todo                          (7)  min Z(z,y) = c.T*z - s.T*y
    #todo                          (8)  min g(x,zT,yT) = b.T*x - E(Z(z))

# import pandas as pd
import numpy as np  
from gamspy import Container, Set, Parameter, Variable, Equation, Model, Sum, Sense

model=Container()
n=8 # i type product
m=5 # j type material
scenario = 2 # 2 scenario

sc=Set(model, name ="sc", description="scenario", records= ["sc"+ str(k) for k in range (1, scenario + 1)])
i=Set(model, name="i", description="productions", records=["i" + str(x) for x in range (1,n+1)])
j=Set(model, name="j", description="materials", records=["j" + str(x) for x in range (1,m+1)])

b=Parameter(
    model, name="b", description="pre-order_cost",
    domain=j,
    records= np.random.randint(100, 500, size=(1,m)),
)
s=Parameter(
    model, name="s", description="inventory_cost",
    domain=j,
    records= np.random.randint(1, 99, size=(1,m)),
)
l=Parameter(
    model, name="l", description="production_cost",
    domain=i,
    records= np.random.randint(100, 500, size=(1,n)),
)
q=Parameter(
    model, name="q", description="price product",
    domain=i,
    records= np.random.randint(1000, 10000, size=(1,n)),
)
c=Parameter(
    model, name="c", description="equation c= l-q",
    domain=i,
)
c[i] = l[i]-q[i]

ps=Parameter(
    model, name="ps", description="probability of scenario",
    domain=sc,
    records=np.array([0.5, 0.5]), # ps[sc]= 0.5
)
d=Parameter(
    model, name="d", description="demand",
    domain=[sc,i],
    records= np.random.binomial(10, 0.5, size=(scenario,n)),
)
a=Parameter(
    container=model, name="a",
    domain=[i,j],
    # matrix A(n x m)
    description="aij",
    records= np.random.randint(1,10, size=(8, 5)),
)

x=Variable(
    model, name="x",
    domain=j,
    type="integer", description="Sum pre-order_material",
)
y=Variable(
    model, name="y",
    domain=[sc,j],
    type="integer", description="inventory",
)
z=Variable(
    model, name="z",
    domain=[sc,i],
    type="integer", description="production",
)

# a[i,j] >= 0 đã được thể hiện trong parameter a
# s[j] < b[j] đã được thể hiện trong parameter s và b
#* VÀ VÌ chỉ toàn tham số (hàm ko có biến)

supply1 = Equation(model, name="supply1", domain=j,)
supply1[j] = x[j] >= 0

supply2 = Equation(model,  name="supply2", domain=[sc, j],)
supply2[sc, j]= y[sc,j] == x[j] - Sum(i, a[i,j]*z[sc, i])

supply3 = Equation(model, name="supply3", domain=[sc,j],)
supply3[sc,j] = y[sc,j] >= 0

demand1 = Equation(model, name="demand1",  domain=[sc,i],)
demand1[sc,i] = z[sc,i] <= d[sc,i]

demand2 = Equation(model, name="demand2", domain=[sc,i],)
demand2[sc,i] = z[sc,i] >= 0

#! equation 7+8
equation78 = Model(
    model, name="equation78",
    equations=[supply1, supply2, supply3, demand1, demand2],
    problem="MIP",
    #tính min
    sense=Sense.MIN,
    #hàm mục tiêu
    objective= Sum(j, b[j]*x[j]) + Sum(sc, ps[sc]*(Sum(i, c[i]*z[sc,i]) - Sum(j, s[j]*y[sc,j]))),
)

#  solve : giải optimal
import sys
#in ra toàn bộ chương trình
    # equation78.solve(output=sys.stdout)
equation78.solve()
print("\nThe solution X of the equation is: ")
print(x.records)
print("\nThe solution Y of the equation is: ")
print(y.records)
print("\nThe solution Z of the equation is: ")
print(z.records)
print(f'Optimal solution found = {equation78.objective_value}')
print("\n----------------End program----------------")