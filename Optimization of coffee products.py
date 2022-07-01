# -*- coding: utf-8 -*-

from gurobipy import *
m = Model('Modelo 1')

I = range(1,4) # tipo de cafe
J = range(1,3) #tipo de mezcla

Z = [0.025,0.02,0.015] #% de cafeina
V = [0.022,0.02] #% maximo de cafeina

# se crea una matriz con las variables para ingresarlas a Gurobi 
X = [(i, j) for j in J for i in I]
x = m.addVars(X, vtype=GRB.CONTINUOUS, name='x')

# Restricciones de disponibilidad
m.addConstr(x[1,1] + x[1,2] <= 20000)
m.addConstr(x[2,1] + x[2,2] <= 25000)
m.addConstr(x[3,1] + x[3,2] <= 15000)

#restricciones de demanda
m.addConstr(x[1,1] + x[2,1] + x[3,1] >= 35000)
m.addConstr(x[1,2] + x[2,2] + x[3,2] >= 25000)

 #restricciones de cafeina 
m.addConstr(quicksum(((Z[i-1]*x[i,1])) for i in I) <= 2.2 * (x[1,1] + x[2,1] + x[3,1]))
m.addConstr(quicksum(((Z[i-1]*x[i,2])) for i in I) <= 2.0 * (x[1,2] + x[2,2] + x[3,2]))

m.setObjective(
    72*(x[1,1]+x[2,1]+x[3,1])
    +75*( x[1,2] + x[2,2] + x[3,2])
    -52*(x[1,1] + x[1,2])
    -50*(x[2,1] + x[2,2])
    -48*(x[3,1] + x[3,2]),GRB.MAXIMIZE)

m.optimize()

print('-------------------------------------------')
print(f'Funcion objetivo: {str(round(m.objVal, 2))}')
print()
for v in m.getVars():
    print(f'\t +{str(v.VarName)} = {str(round(v.x,2))}')

