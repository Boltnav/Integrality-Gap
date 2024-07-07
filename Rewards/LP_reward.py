import cplex
from collections import namedtuple

Rectangle = namedtuple('Rectangle', field_names= ['bottomLeft', 'topRight'])

# The labels are just the positions of the rectangles in the list

def intervalsIntersect(int1, int2):     # int1 and int2 are namedtuples ; this is a helper to isIntersecting
    return not (int1[0] >= int2[1] or int2[0] >= int1[1])

def isIntersecting(rect1, rect2):
    xInterval1, xInterval2, yInterval1, yInterval2 = (rect1.bottomLeft[0], rect1.topRight[0]), (rect2.bottomLeft[0], rect2.topRight[0]), (rect1.bottomLeft[1], rect1.topRight[1]), (rect2.bottomLeft[1], rect2.topRight[1])
    return (intervalsIntersect(xInterval1, xInterval2) and intervalsIntersect(yInterval1, yInterval2))

# need to ensure single constraint case

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


def rewardLP(n, indexList):
    c = cplex.Cplex()
    c.objective.set_sense(c.objective.sense.maximize)
    c.set_problem_name("BinaryLinearProgram")
    t = c.variables.type.continuous  

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

    solution_status = c.solution.get_status()
    solution_value = c.solution.get_objective_value()
    solution_variables = c.solution.get_values()
    
    print("Solution status =", solution_status, ":", c.solution.status[solution_status])
    print("Solution value  =", solution_value)
    for i, value in enumerate(solution_variables):
        print(f"x{i} =", value)



        
# rects = [Rectangle(bottomLeft=(14, 17), topRight=(58, 72)), Rectangle(bottomLeft=(17, 74), topRight=(64, 90)), Rectangle(bottomLeft=(21, 53), topRight=(27, 79)), Rectangle(bottomLeft=(50, 2), topRight=(92, 19)), Rectangle(bottomLeft=(50, 32), topRight=(67, 33)), Rectangle(bottomLeft=(43, 10), topRight=(65, 25))]
rects = [Rectangle(bottomLeft=(52, 4), topRight=(69, 71)), Rectangle(bottomLeft=(41, 72), topRight=(60, 91)), Rectangle(bottomLeft=(60, 32), topRight=(87, 97)), Rectangle(bottomLeft=(11, 19), topRight=(84, 36)), Rectangle(bottomLeft=(3, 74), topRight=(12, 85)), Rectangle(bottomLeft=(60, 32), topRight=(96, 63)), Rectangle(bottomLeft=(29, 6), topRight=(63, 100)), Rectangle(bottomLeft=(46, 54), topRight=(86, 75)), Rectangle(bottomLeft=(12, 93), topRight=(60, 96)), Rectangle(bottomLeft=(32, 22), topRight=(100, 88)), Rectangle(bottomLeft=(43, 19), topRight=(93, 64)), Rectangle(bottomLeft=(21, 5), topRight=(62, 61)), Rectangle(bottomLeft=(60, 14), topRight=(95, 65)), Rectangle(bottomLeft=(26, 20), topRight=(48, 34)), Rectangle(bottomLeft=(12, 35), topRight=(91, 87)), Rectangle(bottomLeft=(68, 39), topRight=(69, 44)), Rectangle(bottomLeft=(17, 20), topRight=(53, 49)), Rectangle(bottomLeft=(95, 61), topRight=(99, 84)), Rectangle(bottomLeft=(26, 56), topRight=(28, 57))]

n = len(rects)

constraintList, indexList = constraintListGeneration(rects)
# print("Rectangle Constraints =", constraintList)
print("\nIndex of Constraints =", indexList)

rewardLP(n, indexList)



# def edgeListGeneration(rects):
#     edgeList = []
#     for i in range(len(rects)):
#         for j in range(i+1, len(rects)):
#             if isIntersecting(rects[i], rects[j]):
#                 edgeList.append((i, j))
#     return edgeList