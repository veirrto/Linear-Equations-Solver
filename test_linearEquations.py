#import linearEquations as lineq
#from linearEquations import gcd
import linearEquations as lineq
import numpy as np
import unittest


class TestGaussianElimination(unittest.TestCase): 

    """Testing Gaussian Elimination"""

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



    """Testing BackSubstitution"""

    def test_backSub_1(self):

        """Testing the system of equations, which has infinite number of solutions"""
        A = [[0, 1, 0, 1], [3, -2, -3, 4], [1, 1, -1, 1], [1, 0, -1, 0]]
        b = [1, -2, 2, 1]
        rref_A, rref_b = lineq.gaussElim(A,b)
        solution = lineq.back_substitution(rref_A, rref_b)
        self.assertEqual(solution, ['1x3+1', '3/2', 'x3', '-1/2']) 
    
    def test_backSub_2(self):

        """Testing the system of equations, which has infinite number of solutions"""
        A = [[1, 4, 3, 2, 1], [2, 8, 4, 0, 0], [0, 0, 3, 6, 9], [2, 8, 7, 6, 3]]
        b = [1, 0, 5, 3]
        rref_A, rref_b = lineq.gaussElim(A,b)
        solution = lineq.back_substitution(rref_A, rref_b)
        self.assertEqual(solution, ['-4x2-3x3-2x4+2/3', 'x2', '-2x4+2/3', 'x4', '1/3'])

    def test_backSub_3(self):

        """Testing the system of equations, which has 0 solution"""
        A = [[2, 2, 8, -3, 9], [2, 2, 4, -1, 3], [1, 1, 3, -2, 3], [3, 3, 5, -2, 3]]
        b = [2, 2, 1, 1]
        rref_A, rref_b = lineq.gaussElim(A,b)
        solution = lineq.back_substitution(rref_A, rref_b)
        #self.assertRaises(TypeError, solution, None)
        self.assertEqual(solution, None)
    
    def test_backSub_4(self):

        """Testing the system of equations, which has 0 solution"""
        A = [[5, -3, 6], [1, -2, 1], [2, 3, 3]]
        b = [2, 3, -1]
        rref_A, rref_b = lineq.gaussElim(A,b)
        solution = lineq.back_substitution(rref_A, rref_b)
        #self.assertRaises(TypeError, solution, None)
        self.assertEqual(solution, None)

    def test_backSub_5(self):

        """Testing matrix, which has more rows than columns"""
        A = [[3, 2, 1], [2, 3, 1], [2, 1, 3], [5, 5, 2]]
        b = [5, 1, 11, 6]
        rref_A, rref_b = lineq.gaussElim(A,b)
        solution = lineq.back_substitution(rref_A, rref_b)
        self.assertEqual(solution, ['2', '-2', '3'])

    def test_backSub_6(self):

        """Testing matrix, which has more rows than columns"""
        A = [[1, 2], [3, 4], [5, 6]]
        b = [1, 2, 3]
        rref_A, rref_b = lineq.gaussElim(A,b)
        solution = lineq.back_substitution(rref_A, rref_b)
        self.assertEqual(solution, ['0', '1/2'])
    
    def test_backSub_7(self): 

        """Testing matrix with one non-zero pivot"""
        A = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        b = [1, 0, 0, 0]
        rref_A, rref_b = lineq.gaussElim(A,b)
        solution = lineq.back_substitution(rref_A, rref_b)
        self.assertEqual(solution, ['1', 'x2', 'x3', 'x4'])

    def test_backSub_8(self):

        """Testing matrix with zero pivot"""
        A = [[0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        b = [1, 0, 0, 0]
        rref_A, rref_b = lineq.gaussElim(A,b)
        solution = lineq.back_substitution(rref_A, rref_b)
        self.assertEqual(solution, None)

    def test_backSub_9(self):

        """Testing zero matrix"""
        A = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        b = [0, 0, 0, 0]
        rref_A, rref_b = lineq.gaussElim(A,b)
        solution = lineq.back_substitution(rref_A, rref_b)
        self.assertEqual(solution, ['x1', 'x2', 'x3', 'x4'])

    def test_backSub_10(self):

        "testing matrix, which has 1 solution"
        A = [[2, -3, 4], [4, 1, 2], [1, -1, 3]]
        b = [2, 2, 3]
        rref_A, rref_b = lineq.gaussElim(A,b)
        solution = lineq.back_substitution(rref_A, rref_b)
        self.assertEqual(solution, ['-1/2', '1', '3/2'])

    
    """Testing EditExpression"""

    def test_edit_expression_1(self):
        
        "testing expression without brackets"
        exp = 'x + 2y + 5z = 8 '
        new_exp = lineq.edit_expression(exp, 4)
        self.assertEqual(new_exp, '1x + 2y + 5z = 8 ')

    def test_edit_expression_2(self):
        
        "testing expression with first negative coefficient (without brackets)"
        exp = '-y + 3z = 9 '
        new_exp = lineq.edit_expression(exp, 4)
        self.assertEqual(new_exp, '0x + -1y + 3z = 9 ')

    def test_edit_expression_3(self):
        
        "testing modified expression with brackes"
        exp = '3x + 2y = 10(5 + x) + 5y '
        new_exp = lineq.edit_expression(exp, 3)
        self.assertEqual(new_exp, '-7x + -3y = 50 ')

    def test_edit_expression_4(self):
        
        "testing modified expression with brackets and digits in the beggining and in the end"
        exp = '-1 + x + 2(-3y + 1) = 3(-4x - 2) - 7 - y '
        new_exp = lineq.edit_expression(exp, 3)
        self.assertEqual(new_exp, '13x + -5y = -14 ')

    def test_edit_expression_5(self):

        "testing modified expression with brackets on both sides"
        exp = '8(-y+0) = 5(y - 5 - 9) '
        new_exp = lineq.edit_expression(exp, 3)
        self.assertEqual(new_exp, '0x + -13y = -70 ')

    def test_edit_expression_6(self):

        "testing modified expression with brackets with 3 variables"
        "and more than one same variable inside brackets"
        exp = '2z - 5(2x - 3y - 1x)  = -4 - 8z '
        new_exp = lineq.edit_expression(exp, 4)
        self.assertEqual(new_exp, '-5x + 15y + 10z = -4 ')

    def test_edit_expression_7(self):

        exp = '3(-x+2y+3x-4y) = y + 9 '
        new_exp = lineq.edit_expression(exp, 3)
        self.assertEqual(new_exp, '6x + -7y = 9 ')


    
if __name__ == '__main__': 
    unittest.main()








    









    
