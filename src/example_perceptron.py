from copy import deepcopy

from perceptron import Perceptron, predict

# AND

in_and = [[0, 0], [0, 1], [1, 0], [1, 1]]
out_and = [0, 0, 0, 1]

percetron_and = Perceptron(X=in_and, Y=out_and)
percetron_and.show = True
percetron_and.train()

test_and = deepcopy(in_and)

print("Test AND")
for i, test in enumerate(test_and):
    print(f"x: {test[1:]}\ty: {out_and[i]}\td: {predict(percetron_and, test)}")


# OR

in_or = [[0, 0], [0, 1], [1, 0], [1, 1]]
out_or = [0, 1, 1, 1]

percetron_or = Perceptron(X=in_or, Y=out_or)
percetron_or.train()

test_or = deepcopy(in_or)

print("OR")
for i, test in enumerate(test_or):
    print(f"x: {test[1:]}\ty: {out_or[i]}\td: {predict(percetron_or, test)}")


# THEN

in_then = [[0, 0], [0, 1], [1, 0], [1, 1]]
out_then = [1, 1, 0, 1]

percetron_then = Perceptron(X=in_then, Y=out_then)
percetron_then.train()

test_then = deepcopy(in_then)

print("THEN")
for i, test in enumerate(test_then):
    print(f"x: {test[1:]}\ty: {out_then[i]}\td: {predict(percetron_then, test)}")


# NOT

in_not = [[0], [1]]
out_not = [1, 0]

percetron_not = Perceptron(X=in_not, Y=out_not)
percetron_not.train()

test_not = deepcopy(in_not)

print("NOT")
for i, test in enumerate(test_not):
    print(f"x: {test[1:]}\ty: {out_not[i]}\td: {predict(percetron_not, test)}")


# XOR (bad)

in_xor = [[0, 0], [0, 1], [1, 0], [1, 1]]
out_xor = [0, 1, 1, 0]

percetron_xor = Perceptron(X=in_xor, Y=out_xor)
percetron_xor.train()

test_xor = deepcopy(in_xor)

print("XOR")
for i, test in enumerate(test_xor):
    print(f"x: {test[1:]}\ty: {out_xor[i]}\td: {predict(percetron_xor, test)}")
