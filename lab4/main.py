import numpy as np

from lab3.main import neuron


# 0 1 2 3
# w x y z

def task_1(x):
    n1 = neuron(np.array(x[[2, 3]]), np.array([-1, -1]), 0)
    n2 = neuron(np.array(x[[0, 1, 2]]), np.array([-1, 1, -1]), -1)
    n3 = neuron(np.array(x[[1, 3]]), np.array([-1, -1]), 0)
    # print(n1, n2, n3, sep=", ")
    return neuron(np.array([n1, n2, n3]), np.array([1, 1, 1]), -1)


def test_1(x):
    return int((not x[2] and not x[3]) or (not x[0] and x[1] and not x[2]) or (not x[1] and not x[3]))


def main():
    x = np.array([
        [w, x, y, z] for w in range(2) for x in range(2) for y in range(2) for z in range(2)
    ])

    print(f"Lab4\t\tvalue\t\ttest_value")
    print("-" * 34)
    for c in x:
        my_result = task_1(c)
        test_result = test_1(c)
        print(f"{c}\t{my_result}\t\t\t{test_result}")


if __name__ == "__main__":
    main()
