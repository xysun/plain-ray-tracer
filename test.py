'''
unit tests
'''
import unittest

from vector import Vector3

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


if __name__ == '__main__':
    unittest.main()
