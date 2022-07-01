# -*- coding: utf-8 -*-

from gurobipy import *
m = Model('Modelo 2')


x1 = m.addVar(vtype=GRB.CONTINUOUS, name='x1')
x2 = m.addVar(vtype=GRB.CONTINUOUS, name='x2')

m.setObjective(x1+(3*x2),GRB.MAXIMIZE)

m.addConstr(x1 - (3*x2) <= 3)
m.addConstr((-2 * x1) + x2 <= 2)
m.addConstr((-3 * x1) + (4 * x2) <= 12)
m.addConstr((3 * x1) + x2 <= 9)

m.display()
m.optimize()

print('-------------------------------------------')
print(f'Funcion objetivo: {str(round(m.objVal, 2))}')
print()
for v in m.getVars():
    print(f'\t +{str(v.VarName)} = {str(round(v.x,2))}')