'''
unit tests
'''
import unittest

from vector import Vector3, Matrix3, LinearSystem3

class TestCamera(unittest.TestCase):
    
    def test_cross_product(self):
        x = Vector3(1, 0, 0)
        y = Vector3(0, 1, 0)
        # x * y = z
        z1 = x.cross_product(y)
        self.assertEqual(z1.z, 1)
        # y * x = -z
        z2 = y.cross_product(x)
        self.assertEqual(z2.z, -1)


class TestMath(unittest.TestCase):
    
    def test_determinant(self):
        m = Matrix3([[2,1,1], [1,-1,2], [1,-1,1]])
        self.assertEqual(m.determinant(), 3)
        
    def test_solve_linear_system(self):
        A = Matrix3([[2,1,1], [1, -1, 2], [1,4,-2]])
        B = Vector3(1, 0, 3)
        system = LinearSystem3(A, B)
        solution = system.solve()
        self.assertEqual(solution.z, 2)
                
    def test_vector_subtraction(self):
        v1 = Vector3(1,2,3)
        v2 = Vector3(4,5,6)
        v = v1 - v2
        self.assertEqual(v.x, -3)


if __name__ == '__main__':
    unittest.main(verbosity = 2)
