import unittest
import Main
class Testing(unittest.TestCase):


    def test_one(self):
        k = Main.Ibanist(iban='8801 6000 0000 0006 2991 0915')
        b = 'IR880160000000000629910915'
        c = 'bank keshavarzi'
        d = '0629910915'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__(), 'valid')

    def test_two(self):
        k = Main.Ibanist(iban='8801 6000 0000  0006 2991 0915')
        b = 'IR880160000000000629910915'
        c = 'bank keshavarzi'
        d = '0629910915'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__(), 'valid')
    def test_three(self):
        k = Main.Ibanist(iban='IR8801 6000 0000  0006 2991 0915')
        b = 'IR880160000000000629910915'
        c = 'bank keshavarzi'
        d = '0629910915'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__(), 'valid')
    def test_four(self):
        k = Main.Ibanist(bank='1', an='0629910915')
        b = 'IR880160000000000629910915'
        c = 'bank keshavarzi'
        d = '0629910915'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__(), 'valid')
    def test_five(self):
        k = Main.Ibanist(bank='1', an='06 29 9109 15')
        b = 'IR880160000000000629910915'
        c = 'bank keshavarzi'
        d = '0629910915'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__(), 'valid')
    def test_six(self):
        k = Main.Ibanist(bank='1', an='6 29 9109 15')
        b = 'IR880160000000000629910915'
        c = 'bank keshavarzi'
        d = '0629910915'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__(), 'valid')
    def test_seven(self):
        k = Main.Ibanist(iban='73 0180 0000 0000 3946 6539 76')
        b = 'IR730180000000003946653976'
        c = 'bank tejarat'
        d = '3946653976'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__(), 'valid')

    def test_eight(self):
        k = Main.Ibanist(iban='IR73 0180 0000 0000 3946 6539 76')
        b = 'IR730180000000003946653976'
        c = 'bank tejarat'
        d = '3946653976'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__(), 'valid')
    def test_nine(self):
        k = Main.Ibanist(bank='2', an='3946653976')
        b = 'IR730180000000003946653976'
        c = 'bank tejarat'
        d = '3946653976'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__(), 'valid')
    def test_ten(self):
        k = Main.Ibanist(bank='2', an='394 6 65 39 76')
        b = 'IR730180000000003946653976'
        c = 'bank tejarat'
        d = '3946653976'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__(), 'valid')
    def test_eleven(self):
        k = Main.Ibanist(iban='IR85016000 03  0006 2991 0915')
        b = 'invalid'
        c = 'invalid'
        d = 'invalid'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__(), 'valid')
    def test_twelve(self):
        k = Main.Ibanist(iban='660540121920100563760602')
        b = 'IR660540121920100563760602'
        c = 'bank parsian'
        d = '20100563760602'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__(), 'valid')
    def test_thirteen(self):
        k = Main.Ibanist(bank='5', an='20100563760602')
        b = 'IR660540121920100563760602'
        c = 'bank parsian'
        d = '20100563760602'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__(), 'valid')
    def test_fourteen(self):
        k = Main.Ibanist(bank='5', an='201 005 637 606 02')
        b = 'IR660540121920100563760602'
        c = 'bank parsian'
        d = '20100563760602'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__(), 'valid')


if __name__ == '__main__':
    unittest.main()