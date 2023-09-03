import unittest
import Main

class Testing(unittest.TestCase):
    def test_string(self):
        a = Main.Ibanist(iban='8801 6000 0000 0006 2991 0915')
        b = 'bank keshavarzi'
        self.assertEqual(a, b, 'valid')


if __name__ == '__main__':
    unittest.main()