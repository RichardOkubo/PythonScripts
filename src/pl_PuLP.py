"""Hands-On Linear Programming: Optimization With Python.

Reference: https://realpython.com/linear-programming-python/
"""

from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable


def report(model):
    print(f"Status: {model.status}, {LpStatus[model.status]}\n"
          f"Objective: {model.objective.value()}\n")
  
    for var in model.variables():
        print(f"{var.name}: {var.value()}")
    print()

    for name, constraint in model.constraints.items():
        print(f"{name}: {constraint.value()}")


# Creating the model
model = LpProblem(name="small-problem", sense=LpMaximize)

# Initialize the decision variables
x = LpVariable(name="x", lowBound=0)
y = LpVariable(name="y", lowBound=0)

# Add the constraints to the model
model += (2 * x + y <= 20, "red_constraint")
model += (4 * x - 5 * y >= -10, "blue_constraint")
model += (-x + 2 * y >= -2, "yellow_constraint")
model += (-x + 5 * y == 15, "green_constraint")

# Add the objective function to the model
model += lpSum([x, 2 * y])

#print(model)

# Solve the problem
status = model.solve()

# Final report
report(model)
