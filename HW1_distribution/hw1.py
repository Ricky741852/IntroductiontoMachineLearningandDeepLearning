from re import A
from utils import *
from typing import Tuple
import math
import numpy as np

def problem_2(row_start: int, row_end: int, col_start: int, col_end: int) -> str:
    output = '    '
    for k in range(col_start, col_end+1):
        output += str(repr(k).rjust(4))
    output += '\n'

    for i in range(row_start, row_end+1):
        output += str(repr(i).rjust(4))
        for j in range(col_start, col_end+1):
            output += str(repr(i*j).rjust(4))
        output += '\n'
    return output
    
FibArray = [0, 1]
def Fibonacci(n):
    if n < len(FibArray):
        return FibArray[n]
    else:       
        FibArray.append(Fibonacci(n - 1) + Fibonacci(n - 2))
        return FibArray[n]

def problem_3(level: int) -> str:
    output = ''
    num = 0
    for i in range(1, level+1):
        for j in range(1, i+1):
            num += 1
            output += f'{Fibonacci(num)}' + ' '
        if(i != level):
            output += '\n'
    return output

def problem_4(radius: float) -> str:
    output = (f'The circle with radius {radius:3.2f} has area {radius * radius * math.pi:4.2f} and perimeter {radius * 2 * math.pi:4.2f}')
    return output

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True
    
def problem_5(s: str) -> str:
    output = s
    if is_number(s):
        output += ' is a'
        dig = float(s)
        if  dig > 0:
            output += ' positive'
        else:
            output += ' negative'
            dig = abs(dig)
        
        if dig.is_integer():
            output += ' integer'
        else:
            output += ' decimal'
    else:
        output += ' is not integer nor decimal'
    return output

def problem_61() -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    a = [7, 1, -1]
    b = [2, 2, 2, 2]
    c = [1, 2, 3, 4]
    A = np.diag(a)
    B = np.diag(b)
    C = np.diag(c)
    return A, B, C

def problem_62() -> Tuple[np.ndarray, np.ndarray, float]:
    origin = np.array([
        [ 4, -1, 2, -2],
        [ 3, -1, 0,  0],
        [ 2,  3, 1,  0],
        [ 0,  7, 1,  1]
    ])
    A = np.linalg.inv(origin)
    B = origin.T
    C = np.linalg.det(origin)
    return A, B, C

def problem_63() -> Tuple[float, float, float]:
    A = np.array([
        [3, 2, 0],
        [1, -1, 0],
        [0, 5, 1]
    ])
    B = np.array([2, 4, -1]).reshape(3, 1)
    ans = np.linalg.solve(A, B)
    return ans.reshape(1, 3)[0]




if __name__ == '__main__':
    test_problem(2, problem_2)
    test_problem(3, problem_3)
    test_problem(4, problem_4)
    test_problem(5, problem_5)
    test_problem(61, problem_61)
    test_problem(62, problem_62)
    test_problem(63, problem_63)
