import cplex
from collections import namedtuple

Rectangle = namedtuple('Rectangle', field_names= ['bottomLeft', 'topRight'])

# The labels are just the positions of the rectangles in the list

def intervalsIntersect(int1, int2):     # int1 and int2 are namedtuples
    return not (int1[0] >= int2[1] or int2[0] >= int1[1])

def isIntersecting(rect1, rect2):
    xInterval1, xInterval2, yInterval1, yInterval2 = (rect1.bottomLeft[0], rect1.topRight[0]), (rect2.bottomLeft[0], rect2.topRight[0]), (rect1.bottomLeft[1], rect1.topRight[1]), (rect2.bottomLeft[1], rect2.topRight[1])
    return (intervalsIntersect(xInterval1, xInterval2) and intervalsIntersect(yInterval1, yInterval2))

def edgeListGeneration(rects):
    edgeList = []
    for i in range(len(rects)):
        for j in range(i+1, len(rects)):
            if isIntersecting(rects[i], rects[j]):
                edgeList.append((i, j))
    return edgeList

def constraintListGeneration(rects):
    constraintList = []
    indexList = []
    for i in range(len(rects)):
        for j in range(len(constraintList)):
            if i in indexList[j]:
                pass
            else:
                flag = 1
                for k in range(len(constraintList[j])):
                    if (isIntersecting(rects[i], constraintList[j][k]) == False):
                        flag = 0
                        break
                if flag:
                    constraintList[j].append(rects[i])
                    indexList[j].append(i)
                    
        for j in range(i+1, len(rects)):  
            if (isIntersecting(rects[i], rects[j])):
                constraintList.append([rects[i], rects[j]])
                indexList.append([i, j])
        
        # print(f'{i}: {indexList}')

    return constraintList, indexList

def rewardILP(n, indexList):
    c = cplex.Cplex()
    c.objective.set_sense(c.objective.sense.maximize)
    c.set_problem_name("IntegerLinearProgram")
    t = c.variables.type.binary  

    var_names = ["x" + str(i) for i in range(n)]
    c.variables.add(names=var_names, types=[t] * n)

    c.objective.set_linear([(name, 1.0) for name in var_names])

    for indices in indexList:
        c.linear_constraints.add(
            lin_expr=[cplex.SparsePair(ind=[var_names[i] for i in indices], val=[1.0] * len(indices))],
            senses=["L"],  
            rhs=[1.0]      
        )

    c.solve()

    print("Solution status =", c.solution.get_status(), ":", c.solution.status[c.solution.get_status()])
    print("Solution value  =", c.solution.get_objective_value())
    for name in var_names:
        print(name, "=", c.solution.get_values(name))

# rects = [Rectangle(bottomLeft=(66, 8), topRight=(68, 40)), Rectangle(bottomLeft=(37, 7), topRight=(50, 68)), Rectangle(bottomLeft=(17, 12), topRight=(93, 58)), Rectangle(bottomLeft=(5, 16), topRight=(86, 90)), Rectangle(bottomLeft=(2, 37), topRight=(18, 72)), Rectangle(bottomLeft=(16, 23), topRight=(98, 94)), Rectangle(bottomLeft=(42, 3), topRight=(56, 93)), Rectangle(bottomLeft=(59, 31), topRight=(90, 78)), Rectangle(bottomLeft=(47, 18), topRight=(63, 96)), Rectangle(bottomLeft=(16, 55), topRight=(74, 73))]
# rects = [Rectangle(bottomLeft=(1, 1), topRight=(5, 5)), Rectangle(bottomLeft=(95, 1), topRight=(99, 5)), Rectangle(bottomLeft=(50, 95), topRight=(55, 99)), Rectangle(bottomLeft=(2, 2), topRight=(97, 97))]
# rects = [Rectangle(bottomLeft=(59, 41), topRight=(78, 52)), Rectangle(bottomLeft=(20, 51), topRight=(72, 57)), Rectangle(bottomLeft=(45, 24), topRight=(61, 52)), Rectangle(bottomLeft=(61, 62), topRight=(99, 71)), Rectangle(bottomLeft=(24, 8), topRight=(53, 37)), Rectangle(bottomLeft=(48, 2), topRight=(59, 18)), Rectangle(bottomLeft=(13, 36), topRight=(21, 83)), Rectangle(bottomLeft=(21, 75), topRight=(42, 98)), Rectangle(bottomLeft=(33, 23), topRight=(52, 71)), Rectangle(bottomLeft=(18, 47), topRight=(27, 80)), Rectangle(bottomLeft=(12, 46), topRight=(93, 51)), Rectangle(bottomLeft=(25, 19), topRight=(39, 65)), Rectangle(bottomLeft=(24, 60), topRight=(100, 69)), Rectangle(bottomLeft=(38, 27), topRight=(86, 54)), Rectangle(bottomLeft=(47, 16), topRight=(80, 20)), Rectangle(bottomLeft=(3, 70), topRight=(5, 77)), Rectangle(bottomLeft=(71, 40), topRight=(97, 71)), Rectangle(bottomLeft=(4, 35), topRight=(93, 94)), Rectangle(bottomLeft=(16, 2), topRight=(96, 44)), Rectangle(bottomLeft=(16, 71), topRight=(62, 80)), Rectangle(bottomLeft=(46, 14), topRight=(79, 54)), Rectangle(bottomLeft=(2, 31), topRight=(33, 71)), Rectangle(bottomLeft=(70, 18), topRight=(85, 46)), Rectangle(bottomLeft=(13, 15), topRight=(31, 18)), Rectangle(bottomLeft=(58, 21), topRight=(67, 67)), Rectangle(bottomLeft=(94, 87), topRight=(95, 88)), Rectangle(bottomLeft=(60, 72), topRight=(82, 93)), Rectangle(bottomLeft=(10, 88), topRight=(89, 93)), Rectangle(bottomLeft=(27, 55), topRight=(31, 75)), Rectangle(bottomLeft=(24, 91), topRight=(53, 94)), Rectangle(bottomLeft=(31, 18), topRight=(89, 86)), Rectangle(bottomLeft=(14, 6), topRight=(51, 39)), Rectangle(bottomLeft=(90, 63), topRight=(91, 81)), Rectangle(bottomLeft=(10, 36), topRight=(44, 66)), Rectangle(bottomLeft=(53, 24), topRight=(56, 93)), Rectangle(bottomLeft=(36, 49), topRight=(78, 66)), Rectangle(bottomLeft=(18, 24), topRight=(81, 35)), Rectangle(bottomLeft=(4, 18), topRight=(78, 55)), Rectangle(bottomLeft=(45, 41), topRight=(65, 62)), Rectangle(bottomLeft=(8, 24), topRight=(86, 41)), Rectangle(bottomLeft=(5, 55), topRight=(90, 91)), Rectangle(bottomLeft=(52, 22), topRight=(65, 37)), Rectangle(bottomLeft=(3, 40), topRight=(77, 60)), Rectangle(bottomLeft=(28, 61), topRight=(84, 90)), Rectangle(bottomLeft=(40, 14), topRight=(43, 62)), Rectangle(bottomLeft=(68, 48), topRight=(73, 71)), Rectangle(bottomLeft=(18, 23), topRight=(58, 62)), Rectangle(bottomLeft=(41, 40), topRight=(67, 88)), Rectangle(bottomLeft=(28, 21), topRight=(52, 52)), Rectangle(bottomLeft=(25, 7), topRight=(78, 67))]
rects = [Rectangle(bottomLeft=(52, 4), topRight=(69, 71)), Rectangle(bottomLeft=(41, 72), topRight=(60, 91)), Rectangle(bottomLeft=(60, 32), topRight=(87, 97)), Rectangle(bottomLeft=(11, 19), topRight=(84, 36)), Rectangle(bottomLeft=(3, 74), topRight=(12, 85)), Rectangle(bottomLeft=(60, 32), topRight=(96, 63)), Rectangle(bottomLeft=(29, 6), topRight=(63, 100)), Rectangle(bottomLeft=(46, 54), topRight=(86, 75)), Rectangle(bottomLeft=(12, 93), topRight=(60, 96)), Rectangle(bottomLeft=(32, 22), topRight=(100, 88)), Rectangle(bottomLeft=(43, 19), topRight=(93, 64)), Rectangle(bottomLeft=(21, 5), topRight=(62, 61)), Rectangle(bottomLeft=(60, 14), topRight=(95, 65)), Rectangle(bottomLeft=(26, 20), topRight=(48, 34)), Rectangle(bottomLeft=(12, 35), topRight=(91, 87)), Rectangle(bottomLeft=(68, 39), topRight=(69, 44)), Rectangle(bottomLeft=(17, 20), topRight=(53, 49)), Rectangle(bottomLeft=(95, 61), topRight=(99, 84)), Rectangle(bottomLeft=(26, 56), topRight=(28, 57))]

n = len(rects)
edgeList = edgeListGeneration(rects)
print("Edges =", edgeList)
rewardILP(n, edgeList)




"""
    # c = cplex.Cplex()
    # c.objective.set_sense(c.objective.sense.maximize)
    # c.set_problem_name("BinaryIntegerLinearProgram")
    # t = c.variables.type

    # var_names = ["x" + str(i) for i in range(n)]
    # types = [t.binary] * n  # Values are binary
    
    # indices = c.variables.add(names = var_names, lb = [0] * n, ub = [1] * n, types = types)

    # c.objective.set_linear([(name, 1.0) for name in var_names])

    # for i, j in edgeList:
    #     c.linear_constraints.add(
    #         lin_expr = [cplex.SparsePair(ind = [var_names[i], var_names[j]], val = [1.0, 1.0])],
    #         senses = ["L"],
    #         rhs = [1.0]
    #     )

    # c.solve()
"""