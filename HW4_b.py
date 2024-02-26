from scipy.optimize import fsolve
import numpy as np
'''
Utilized chatGPT
'''

def polynomial1(x):
    """
    First equation to be evaluated
    :param x: Ambiguous x value
    :return: values for the function f(x)
    """
    return x - 3 * np.cos(x)

def polynomial2(x):
    """
    Second equation to be evaluated
    :param x: Ambiguous x value
    :return: values for the function f(x)
    """
    return np.cos(2*x) * x ** 3


def intersection(polynomial1, polynomial2):
    """
    Finds the intersection of two polynomials.  The program will guess a value x and check for matching y values on both functions,
    the function will then find a value x where the y values are the same.
    :param polynomial1: Function 1
    :param polynomial2: Function 2
    :return: Intersection point, (x, y)
    """
    def equations(x):
        return [polynomial1(x[0]) - polynomial2(x[0]), ]

    guess = np.array([0])
    intersection_point = fsolve(equations, guess)

    return intersection_point[0]

def main():
    """
    Prints intersection point of the functions
    """
    intersection_point = intersection(polynomial1, polynomial2)
    if polynomial1(intersection_point) == polynomial2(intersection_point):
        print(f"The polynomials intersect at point ({intersection_point}, {polynomial1(intersection_point)})")
    else:
        print("The polynomials do not intersect.")

if __name__ == '__main__':
    main()
