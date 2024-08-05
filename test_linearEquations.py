#import linearEquations as lineq
#from linearEquations import gcd
import linearEquations as lineq
import numpy as np
import unittest


class TestGaussianElimination(unittest.TestCase): 


    def test_gaussElim_1(self):
        """Testing the system of equations, which has infinite number of solutions"""
        A = [[0, 1, 0, 1], [3, -2, -3, 4], [1, 1, -1, 1], [1, 0, -1, 0]]
        b = [1, -2, 2, 1]
        rref_A, rref_b = lineq.gaussElim(A,b)
        self.assertEqual(rref_A, [[3, -2, -3, 4], [0, 1, 0, 1], [0, 0, 0, -6], [0, 0, 0, 0]])
        self.assertEqual(rref_b, [-2, 1, 3, 0])
    
    def test_gaussElim_2(self): 
        """Testing the system of equations, which has 0 solution"""
        A = [[2, 2, 8, -3, 9], [2, 2, 4, -1, 3], [1, 1, 3, -2, 3], [3, 3, 5, -2, 3]]
        b = [2, 2, 1, 1]
        rref_A, rref_b = lineq.gaussElim(A,b)
        self.assertEqual(rref_A, [[2, 2, 8, -3, 9], [0, 0, -4, 2, -6], [0, 0, 0, 4, 0], [0, 0, 0, 0, 0]])
        self.assertEqual(rref_b, [2, 0, 0, 8])
    
    def test_gaussElim_3(self):
        """Testing matrix, which has more rows than columns"""
        A = [[3, 2, 1], [2, 3, 1], [2, 1, 3], [5, 5, 2]]
        b = [5, 1, 11, 6]
        rref_A, rref_b = lineq.gaussElim(A,b)
        self.assertEqual(rref_A, [[3, 2, 1], [0, 5, 1], [0, 0, 36], [0, 0, 0]])
        self.assertEqual(rref_b, [5, -7, 108, 0])

    def test_gaussElim_4(self):
        """Testing matrix with one non-zero pivot"""
        A = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        b = [1, 0, 0]
        rref_A, rref_b = lineq.gaussElim(A,b)
        self.assertEqual(rref_A, A)
        self.assertEqual(rref_b, b)

    def test_gaussElim_5(self):
        """Testing matrix with zero pivot"""
        A = [[0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        b = [1, 0, 0, 0]
        rref_A, rref_b = lineq.gaussElim(A,b)
        self.assertEqual(rref_A, [[2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.assertEqual(rref_b, [0, 1, 0, 0])

    def test_gaussElim_6(self):
        """Testing zero matrix"""
        A = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        b = [0, 0, 0, 0]
        rref_A, rref_b = lineq.gaussElim(A,b)
        self.assertEqual(rref_A, A)
        self.assertEqual(rref_b, b)

    def test_gaussElim_7(self):
        "testing matrix, which has 1 solution"
        A = [[2, -3, 4], [4, 1, 2], [1, -1, 3]]
        b = [2, 2, 3]
        rref_A, rref_b = lineq.gaussElim(A,b)
        self.assertEqual(rref_A, [[2, -3, 4], [0, 7, -6], [0, 0, 20]])
        self.assertEqual(rref_b, [2, -2, 30])

#class TestBackSubstitution(unittest.TestCase): 


    



        


if __name__ == '__main__': 
    unittest.main()








    
