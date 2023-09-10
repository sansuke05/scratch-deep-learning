import numpy as np


def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    left = x1*w1 + x2*w2
    if left <= theta:
        return 0
    elif left > theta:
        return 1


def NPAND(x1, x2):
    w1, w2, theta = 0.5, 0.5, -0.7
    x = np.array([x1, x2])
    w = np.array([w1, w2])
    return np.sum(x * w) + theta > 0


def NAND(x1, x2):
    w1, w2, b = -0.5, -0.5, 0.7
    x = np.array([x1, x2])
    w = np.array([w1, w2])
    return np.sum(x * w) + b > 0


# print(NPAND(0, 0))
# print(NPAND(1, 0))
# print(NPAND(0, 1))
# print(NPAND(1, 1))
# print(NAND(0, 0))
# print(NAND(1, 0))
# print(NAND(0, 1))
# print(NAND(1, 1))


def OR(x1, x2):
    w1, w2, b = 0.5, 0.5, -0.2
    x = np.array([x1, x2])
    w = np.array([w1, w2])
    return np.sum(x * w) + b > 0


def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    return AND(s1, s2)


# print(OR(0, 0))
# print(OR(1, 0))
# print(OR(0, 1))
# print(OR(1, 1))
print(XOR(0, 0))
print(XOR(1, 0))
print(XOR(0, 1))
print(XOR(1, 1))
