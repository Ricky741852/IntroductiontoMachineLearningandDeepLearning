## Tree ##
import numpy as np
from scipy import stats
import sys

class TreeNode():
    def __init__(self):
        self.left = None
        self.right = None
        self.theta = None
        self.dimension = None
        self.is_branch = False
        self.tree_depth = 0

    def branch_stump(self, theta, dimension):
        self.left = TreeNode()
        self.right = TreeNode()
        self.theta = theta
        self.dimension = dimension
        self.is_branch = True
        return self.left, self.right

    def save_label(self, class_pred):
        self.prediction = class_pred

    def show(self, indent=0):
        if(self.is_branch == True):
            print("Tree theta is %f and dimension is %f" %(self.theta, self.dimension))
            print("---" * indent)
            self.left.show(indent=indent+1)
            self.right.show(indent=indent+1)
class CRTree():

    def __init__(self, tree_depth):
        self.root = TreeNode()
        self.tree_depth = tree_depth

    def train(self, data, y):
        self.branch(data, self.root, y)

    def showTree(self):
        self.root.show()

    def branch(self, data, node, y):

        # check if stop branching 
        if(np.unique(y).shape[0] == 1 or np.unique(data).shape[0] == 1 or node.tree_depth == self.tree_depth):
            node.save_label(stats.mode(y)[0][0])
            return

        # calculate the spliting dimenstion and theta
        theta, dimension  = self.cal_branch(data, y)

        # split the data
        data_right = data[np.where(data[:, dimension] >= theta)]
        y_right = y[np.where(data[:, dimension] >= theta)]
        data_left = data[np.where(data[:, dimension] < theta)]
        y_left = y[np.where(data[:, dimension] < theta)]
                        
        # recorde in the node
        left_node, right_node = node.branch_stump(theta, dimension)
        left_node.tree_depth = node.tree_depth+1
        right_node.tree_depth = node.tree_depth+1
        self.branch(data_right, right_node, y_right)
        self.branch(data_left, left_node, y_left)

        return    

    def cal_branch(self, data, y):

        # store the best impuraty, theta, dimension
        best_impuraty = sys.float_info.max
        best_theta = None
        best_dimension = None

        # iterate over the feature dimension
        for d in range(data.shape[1]):
            feature_array = data[:, d]
            unique_feature = np.unique(feature_array)

            # iterate the segment
            for segment in range(unique_feature.shape[0]-1):
                theta = (unique_feature[segment] + unique_feature[segment+1])/2
                b_score = self.cal_score(data, d, theta, y)
                if(b_score < best_impuraty):
                    best_impuraty = b_score
                    best_theta = theta
                    best_dimension = d

        return best_theta, best_dimension

    def cal_score(self, data, dimension, theta, y):
        # calculate the impuraty over left and right
        split_left = np.where(data[:, dimension] >= theta)[0]
        split_right = np.where(data[:, dimension] < theta)[0]
        return (split_left.shape[0])*self.cal_impuraty(data, y, split_left) + (split_right.shape[0])*self.cal_impuraty(data, y, split_right)

    def cal_impuraty(self, data, y, index):
        # calculate the gini impuraty
        y_split = y[index]
        label = np.unique(y_split)
        puraty = 0
        for k in label:
            puraty += (np.sum(y_split == k)/y_split.shape)**2

        return 1-puraty

    def predict(self, data):
        # predict the label 
        return self.predict_node(self.root, data)

    def predict_node(self, node, data):
        # predict the leaf 
        if(node.is_branch == False):
            y_predict = np.zeros(data.shape[0])
            y_predict = y_predict + node.prediction

            return y_predict


        data_left_indic = np.where(data[:, node.dimension] >= node.theta)
        data_right_indic = np.where(data[:, node.dimension] < node.theta)

        y_left_predict = self.predict_node(node.right, data[data_left_indic])
        y_right_predict = self.predict_node(node.left, data[data_right_indic])

        y_predict = np.zeros(data.shape[0])

        for i in range(y_left_predict.shape[0]):
            y_predict[data_left_indic[0][i]] = y_left_predict[i]
        for i in range(y_right_predict.shape[0]):
            y_predict[data_right_indic[0][i]] = y_right_predict[i]

        return y_predict

class RandomCRTforest():

    # initialize with given tree number and tree depth
    def __init__(self, tree_num, tree_depth):
        self.tree_num = tree_num
        self.all_tree = []
        self.tree_depth = tree_depth

    # train the forest
    def train(self, X, y):
        np.random.seed(1215) # We use random.seed to make sure the answer will be the same.
        for i in range(self.tree_num):
            index = np.random.choice(X.shape[0], X.shape[0]//10)
            train_bag_x = X[index]
            train_bag_y = y[index]
            oneTree = CRTree(self.tree_depth)
            oneTree.train(train_bag_x, train_bag_y)
            self.all_tree.append(oneTree)
        
    # predict 
    def predict(self, X):
        predict_array = np.zeros((self.tree_num, X.shape[0]))
        for i, tree in enumerate(self.all_tree):
            predict_array[i] = tree.predict(X)
        predict_array = np.sign(np.sum(predict_array, axis=0))
        predict_array[np.where(predict_array == 0)] = 1
        return predict_array