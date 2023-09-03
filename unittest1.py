import unittest
import index1

class Testing(unittest.TestCase):
    def test_string(self):
        a = index1.Ibanist(iban='8801 6000 0000 0006 2991 0915')
        b = 'bank keshavarzi', '0629910915', 'IR880160000000000629910915'
        self.assertEqual(a, b, 'valid')


if __name__ == '__main__':
    unittest.main()