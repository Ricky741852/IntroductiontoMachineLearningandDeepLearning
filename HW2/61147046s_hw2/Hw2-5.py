### **Problem Description**
# In the homework you will have fun to find the best parameter of the classification algorithm using a simple holdout validation and 3-fold cross validation of an in-house classification algorithm. We are using the C&RT tree. We generate 2000 data with 1 or -1 classification problem and split the first 1002 as training data and the rest as testing data.

import numpy as np
import random
from sklearn import datasets
from tree import *
from typing  import Tuple
from array import array
from utils import *

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

##### Validation ######
# We show how to produce a fix validation set, we split the first 1/3 data as validation set and last 2/3 data as train set. We then choose the hyperparameters (tree number and tree depth) with the highest accuracy. And we will predict the test data with the best hyperparameters. Please run the following code and report the best_acc, best tree number, best tree depth and test accuracy.

## Tree Parameters:
# tree number [1, 10, 50]
# tree depth [1, 3, 5]

def problem_51(X: array, y: array, X_test: array, y_test: array) -> Tuple[str]:
    print("-----Running problem_51-----")

    # We split the full training dataset into training dataset and validation dataset.
    X_val =  X[:X.shape[0]//3]
    y_val =  y[:y.shape[0]//3]
    X_train = X[X.shape[0]//3:]
    y_train = y[y.shape[0]//3:]

    # initialize the best_XXX parameters 
    best_accuracy = 0
    best_tree_number = 0
    best_tree_depth = 0

    # Run a for loop to search the best parameters.
    for tree_number in [1, 10, 50]:
        for tree_depth in [1, 3, 5]:
            # Generate the RandomCRTforest
            forest = RandomCRTforest(tree_number, tree_depth)
            # Train the model
            forest.train(X_train, y_train)
            # We use the current model to predict the results using validation dataset.
            y_predict = forest.predict(X_val)
            # Get the accuracy.
            accuracy = sum(y_predict==y_val)/y_predict.shape[0]
            print("For tree number {} and tree depth {} the accuracy is {}".format(tree_number, tree_depth, accuracy))

            # If the current accuracy > best_accuracy, we update the best parameters.
            if(accuracy > best_accuracy):
                best_accuracy = accuracy
                best_tree_number = tree_number
                best_tree_depth = tree_depth
    
    # print the best parameters.
    print(f'Validation: best acc = {best_accuracy:.2f}, best tree_num = {best_tree_number:.2f}, best tree_depth = {best_tree_depth:.2f}')

    # We use the best parameters to train the model with the full training dataset.
    forest = RandomCRTforest(best_tree_number, best_tree_depth)
    forest.train(X, y)
    y_test_predict = forest.predict(X_test)
    test_accuracy = sum(y_test_predict==y_test)/y_test_predict.shape[0]
    print(f"The test accuracy is {test_accuracy:.2f}")

    return f'Validation: best acc = {best_accuracy:.2f}, best tree_num = {best_tree_number:.2f}, best tree_depth = {best_tree_depth:.2f}, test accuracy = {test_accuracy:.2f}'

##### 3-Fold Cross Validation ######
# Please implement the 3-fold cross validation. Please use the first, second and third 1/3 data as validation set respectively.


def problem_52(X: array, y: array, X_test: array, y_test: array) -> Tuple[str]:
    ## TODO: implement a 3-fold cross validation.
    print("-----Running problem_52-----")
    pass

if __name__ == '__main__':
    test_problem(51, problem_51)
    test_problem(52, problem_52)