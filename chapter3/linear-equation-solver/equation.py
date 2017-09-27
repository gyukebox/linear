import numpy as np
import matplotlib.pyplot as plt


class Equation:
    """
    선형방정식을 행렬로 바꿔주는 클래스
    """
    def __init__(self, num_equation):
        self.num_variables = num_equation
        self.equations = list()
        self.matrix = None

    def __str__(self):
        pass

    def add_equation(self, equation):
        self.equations.append(equation)

    def plot_equations(self):
        pass


if __name__ == '__main__':
    num_equation = int(input())
    for i in range(num_equation):
        equation = input()
        print(equation)
