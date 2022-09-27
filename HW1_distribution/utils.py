from cmath import isclose
import numpy as np


def test_problem(problem_number: int, solution):

    if problem_number == 2:
        correct_2 = 0
        for i in range(1, 11):
            fin = open('./test_data/problem_2/'+str(i)+'.in', 'r')
            line = fin.readlines()
            input_data = [int(i) for i in line]

            fout = open('./test_data/problem_2/'+str(i)+'.out', 'r')
            output_data=''
            while fout:
                line  = fout.readline()
                output_data += line
                if line == "":
                    break
            fout.close() 

            user_output = solution(input_data[0],input_data[1],input_data[2],input_data[3])

            if user_output != output_data:
                print(f"***problem {problem_number} , testing data {i} is wrong")
            else:
                correct_2 += 1

        print(f"problem {problem_number} , you got {correct_2} / 10")


    elif problem_number == 3:
        correct_3 = 0
        for i in range(1, 11):
            fin = open('./test_data/problem_3/'+str(i)+'.in', 'r')
            input_data = int(fin.read())

            output_data = ''

            fout = open('./test_data/problem_3/'+str(i)+'.out', 'r')
            output_data=''
            while fout:
                line  = fout.readline()
                output_data += line
                if line == "":
                    break
            fout.close() 

            user_output = solution(input_data)

            if user_output != output_data:
                print(f"***problem {problem_number} , testing data {i} is wrong")
            else:
                correct_3 += 1

        print(f"problem {problem_number} , you got {correct_3} / 10")


    elif problem_number == 4:
        correct_4 = 0

        for i in range(1,4):

            input_data=float(open('./test_data/problem_4/'+str(i)+'.in', 'r').read())

            user_output = solution(input_data)
            output_data = [float(x) for x in open('./test_data/problem_4/'+str(i)+'.out', 'r').read().split()]


            Ans=(f'The circle with radius {input_data:3.2f} has area {output_data[0]:4.2f} and perimeter {output_data[1]:4.2f}')

            if user_output != Ans:
                print(f"***problem {problem_number} is wrong")
            else:
                correct_4 += 1

        print(f"problem {problem_number} , you got {correct_4} / 3")


    elif problem_number == 5:
        correct_5 = 0
        for i in range(1, 11):
            fin = open('./test_data/problem_5/'+str(i)+'.in', 'r')
            input_data = fin.read()
            
            fout = open('./test_data/problem_5/'+str(i)+'.out', 'r')
            output_data = fout.read().rstrip('\n')

            user_output = solution(input_data)
            if user_output != output_data:
                print(f"***problem {problem_number} , testing data {i} is wrong")
            else:
                correct_5 += 1

        print(f"problem {problem_number} , you got {correct_5} / 10")
    

    elif problem_number == 61:
        correct_61 = 0

        A, B, C = solution()

        Ans_A=np.array([
            [ 7,  0,  0],
            [ 0,  1,  0],
            [ 0,  0, -1]])

        Ans_B=np.array([
            [2, 0, 0, 0],
            [0, 2, 0, 0],
            [0, 0, 2, 0],
            [0, 0, 0, 2]])

        Ans_C=np.array([
            [1, 0, 0, 0],
            [0, 2, 0, 0],
            [0, 0, 3, 0],
            [0, 0, 0, 4]])

        if type(A) is np.ndarray and np.array_equal(Ans_A, A):
            correct_61 += 1
        else:
            print(f"***problem {problem_number} , A matric is wrong")

        if type(B) is np.ndarray and np.array_equal(Ans_B, B):
            correct_61 += 1
        else:
            print(f"***problem {problem_number} , B matric is wrong")

        if type(C) is np.ndarray and np.array_equal(Ans_C, C):
           correct_61 += 1
        else:
            print(f"***problem {problem_number} , C matric is wrong")

        print(f"problem {problem_number} , you got {correct_61} / 3")


    elif problem_number == 62:
        correct_62 = 0

        D_inv, D_tra, D_det = solution()

        Ans_inv = np.array(
        [[ -1.,  -1.,   4.,  -2.],
        [ -3.,  -4.,  12.,  -6.],
        [ 11.,  14., -43.,  22.],
        [ 10.,  14., -41.,  21.]])

        Ans_tra = np.array(
        [[ 4,  3,  2,  0],
        [-1, -1,  3,  7],
        [ 2,  0,  1,  1],
        [-2,  0,  0,  1]])

        Ans_det = 1

        if np.allclose(Ans_inv, D_inv, atol=0.01):
            correct_62 += 1
        else:
            print(f"***problem {problem_number} , the inverse is wrong")

        if np.array_equal(Ans_tra, D_tra):
            correct_62 += 1
        else:
            print(f"***problem {problem_number} , the transpose is wrong")

        if np.isclose(D_det, Ans_det, atol=0.01) :
           correct_62 += 1
        else:
            print(f"***problem {problem_number} , the determinant is wrong")

        print(f"problem {problem_number} , you got {correct_62} / 3")


    elif problem_number == 63:
        correct_63 = 0
        Ans = solution()
        if np.array_equal(Ans, np.array([ 2., -2.,  9.])):
            correct_63 += 1
        else:
            print(f"***problem {problem_number} , is wrong")  

        print(f"problem {problem_number} , you got {correct_63} / 1")




