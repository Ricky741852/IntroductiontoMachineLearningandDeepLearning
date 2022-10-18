from cmath import isclose
import numpy as np
import random
from sklearn import datasets

##### Generate Data #####
def generateData():
    # We use random.seed to make sure the answer will be the same.
    random.seed(1215)
    np.random.seed(1215) 
    # Generate the dataset using sklearn module. 
    X, y = datasets.make_classification(2000, 10, random_state=1215)
    y[y==0] = -1
    X_train = X[:1002]
    y_train = y[:1002]
    X_test = X[1002:]
    y_test = y[1002:]

    return X_train, y_train, X_test, y_test
# Store the generated data in X, y, X_test, y_test
X, y, X_test, y_test = generateData()


def test_problem(problem_number: int, solution):

    if problem_number == 51:
        correct_5 = 0
        for i in range(1, 2):
            fout = open('./test_data/problem_51/'+str(i)+'.out', 'r')
            output_data = fout.read().rstrip('\n')

            user_output = solution(X, y, X_test, y_test)
            # For debug
            # print(user_output)
            if user_output != output_data:
                print(f"***problem {problem_number} , testing data {i} is wrong")
            else:
                correct_5 += 1

        print(f"problem {problem_number} , you got {correct_5} / 1")
    
    elif problem_number == 52:
        correct_5 = 0
        for i in range(1, 2):
            fout = open('./test_data/problem_52/'+str(i)+'.out', 'r')
            output_data = fout.read().rstrip('\n')

            user_output = solution(X, y, X_test, y_test)
            if user_output != output_data:
                print(f"***problem {problem_number} , testing data {i} is wrong")
            else:
                correct_5 += 1

        print(f"problem {problem_number} , you got {correct_5} / 1")