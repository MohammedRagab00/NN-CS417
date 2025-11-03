import numpy as np


def step(x):
    return 1 if x >= 0 else 0


def neuron(x, w, b):
    return step(x @ w + b)


def or_gate(x):
    result = neuron(x, np.array([1, 1]), -1)
    return result


def and_gate(x):
    result = neuron(x, np.array([1, 1]), -2)
    return result


def xor_gate(x):
    n1 = neuron(x, np.array([1, -1]), -1)
    n2 = neuron(x, np.array([-1, 1]), -1)
    n3 = or_gate(np.array([n1, n2]))
    return n3


# (a!xz or a!y) and (xy or !x!z)   ---> [a , x , y , z] ---> [0 ,1 ,2 ,3 ]
def mlp(x):
    n1 = neuron(x[[0, 1, 3]], np.array([1, -1, 1]), -2)
    n2 = neuron(x[[0, 2]], np.array([1, -1]), -1)
    n3 = and_gate(x[[1, 2]])
    n4 = neuron(x[[1, 3]], np.array([1, 1]), -2)
    n5 = or_gate(np.array([n1, n2]))
    n6 = neuron(np.array([n3, n4]), np.array([1, -1]), 0)
    n7 = and_gate(np.array([n5, n6]))
    return n7


def mlp_test(x):
    return ((x[0] and not x[1] and x[3]) or (x[0] and not x[2])) and ((x[1] and x[2]) or not (x[1] and x[3]))


def main():
    x = [
        [a, x, y, z] for a in range(2) for x in range(2) for y in range(2) for z in range(2)
    ]

    s = '      '
    print(f"MLP\t{s}value\ttest_value")
    print("-" * 35)
    x = np.array(x)
    for c in x:
        my_result = mlp(c)
        test_result = mlp_test(c)
        print(f"{c}\t{my_result}\t{test_result}")


if __name__ == "__main__":
    main()
