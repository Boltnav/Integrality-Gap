#include <ilcplex/ilocplex.h>
ILOSTLBEGIN

int main() {
    IloEnv env;
    try {
        IloModel model(env);
        IloCplex cplex(model);
        cplex.setOut(env.getNullStream()); // Suppress CPLEX output to the console

        // Problem parameters
        int n = 5; // Number of variables
        // Edges list representing constraints between variables
        int edges[][2] = {{0, 1}, {0, 2}, {0, 3}, {0, 4}, {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4}};
        int numEdges = 10; // Number of edges

        // Define variables
        IloBoolVarArray x(env, n);

        // Objective function: Maximize the sum of all variables
        IloExpr objective(env);
        for (int i = 0; i < n; ++i) {
            objective += x[i];
        }
        model.add(IloMaximize(env, objective));
        objective.end();

        // Add constraints based on the edge list
        for (int i = 0; i < numEdges; ++i) {
            model.add(x[edges[i][0]] + x[edges[i][1]] <= 1);
        }

        // Solve the problem
        if (cplex.solve()) {
            env.out() << "Solution status = " << cplex.getStatus() << endl;
            env.out() << "Solution value  = " << cplex.getObjValue() << endl;
            for (int i = 0; i < n; ++i) {
                env.out() << "x" << i << " = " << cplex.getValue(x[i]) << endl;
            }
        } else {
            env.out() << "No solution" << endl;
        }
    } catch (IloException& e) {
        cerr << "Concert exception caught: " << e << endl;
    } catch (...) {
        cerr << "Unknown exception caught" << endl;
    }
    env.end();
    return 0;
}
