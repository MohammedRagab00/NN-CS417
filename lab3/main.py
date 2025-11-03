import numpy as np


def step(x):
    return 1 if x >= 0 else 0


def neuron(x, w, b):
    return step(np.dot(x, w) + b)


def or_perceptron(x):
    return neuron(x, np.array([1, 1]), -1)


def and_perceptron(x):
    return neuron(x, np.array([1, 1]), -2)


def and_not_perceptron(x):
    return neuron(x, np.array([1, -1]), -1)
    #                        ([2, -1]), -2)


def xor_perceptron_v1(x):
    # (a and not b) or (b and not a)
    n1 = and_not_perceptron(x)
    n2 = and_not_perceptron(x)
    return or_perceptron(np.array([n1, n2]))


def xor_perceptron_v2(x):
    # (a or b) and (not a or not b)
    n1 = or_perceptron(x)
    n2 = neuron(x, np.array([-1, -1]), 1)
    return and_perceptron(np.array([n1, n2]))


def question_slide_2_page_14(x):
    #                                         0  1  2  3
    # (a !x z or a !y) and (x y or !x !z) -> [a, x, y, z]
    n1 = neuron(x[[0, 1, 3]], np.array([1, -1, 1]), -2)
    n2 = neuron(x[[0, 2]], np.array([1, -1]), -1)
    n3 = and_perceptron(x[[1, 2]])
    n4 = neuron(x[[1, 3]], np.array([-1, -1]), 0)
    n5 = or_perceptron(np.array([n1, n2]))
    n6 = or_perceptron(np.array([n3, n4]))
    # print(n1, n2, n3, n4, n5, n6, sep=", ")

    return bool(and_perceptron(np.array([n5, n6])))


def q_test(x):
    return bool(((x[0] and not x[1] and x[3]) or (x[0] and not x[2])) and ((x[1] and x[2]) or (not x[1] and not x[3])))


def main():
    x = np.array([
        [a, x, y, z] for a in range(2) for x in range(2) for y in range(2) for z in range(2)
    ])

    print(f"MLP\t\t\tvalue\t\ttest_value")
    print("-" * 34)
    # c = np.array([1, 1, 0, 1])
    for c in x:
        my_result = question_slide_2_page_14(c)
        test_result = q_test(c)
        print(f"{c}\t{my_result}\t\t\t{test_result}")


if __name__ == "__main__":
    main()
