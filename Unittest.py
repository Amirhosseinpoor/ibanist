import unittest
import Main


class Testing(unittest.TestCase):

    def test_one(self):
        k = Main.Ibanist(iban='8801 6000 0000 0006 2991 0915')
        b = 'IR880160000000000629910915'
        c = 'bank keshavarzi'
        d = '0629910915'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_two(self):
        k = Main.Ibanist(iban='8801 6000 0000  0006 2991 0915')
        b = 'IR880160000000000629910915'
        c = 'bank keshavarzi'
        d = '0629910915'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_three(self):
        k = Main.Ibanist(iban='IR8801 6000 0000  0006 2991 0915')
        b = 'IR880160000000000629910915'
        c = 'bank keshavarzi'
        d = '0629910915'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_four(self):
        k = Main.Ibanist(bank='1', an='0629910915')
        b = 'IR880160000000000629910915'
        c = 'bank keshavarzi'
        d = '0629910915'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_five(self):
        k = Main.Ibanist(bank='1', an='06 29 9109 15')
        b = 'IR880160000000000629910915'
        c = 'bank keshavarzi'
        d = '0629910915'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_six(self):
        k = Main.Ibanist(bank='1', an='6 29 9109 15')
        b = 'IR880160000000000629910915'
        c = 'bank keshavarzi'
        d = '0629910915'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_seven(self):
        k = Main.Ibanist(iban='73 0180 0000 0000 3946 6539 76')
        b = 'IR730180000000003946653976'
        c = 'bank tejarat'
        d = '3946653976'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_eight(self):
        k = Main.Ibanist(iban='IR73 0180 0000 0000 3946 6539 76')
        b = 'IR730180000000003946653976'
        c = 'bank tejarat'
        d = '3946653976'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_nine(self):
        k = Main.Ibanist(bank='2', an='3946653976')
        b = 'IR730180000000003946653976'
        c = 'bank tejarat'
        d = '3946653976'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_ten(self):
        k = Main.Ibanist(bank='2', an='394 6 65 39 76')
        b = 'IR730180000000003946653976'
        c = 'bank tejarat'
        d = '3946653976'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_eleven(self):
        k = Main.Ibanist(iban='IR85016000 03  0006 2991 0915')
        b = 'invalid'
        c = 'invalid'
        d = 'invalid'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_twelve(self):
        k = Main.Ibanist(iban='660540121920100563760602')
        b = 'IR660540121920100563760602'
        c = 'bank parsian'
        d = '20100563760602'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_thirteen(self):
        k = Main.Ibanist(bank='5', an='20100563760602')
        b = 'IR660540121920100563760602'
        c = 'bank parsian'
        d = '20100563760602'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_fourteen(self):
        k = Main.Ibanist(bank='5', an='201 005 637 606 02')
        b = 'IR660540121920100563760602'
        c = 'bank parsian'
        d = '20100563760602'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_fifteen(self):
        k = Main.Ibanist(iban='57 0600 3019 0251 4083 0360 01')
        b = 'IR570600301902514083036001'
        c = 'bank mehriran'
        d = '3019025140830361'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_sixteen(self):
        k = Main.Ibanist(iban='ir57 0600 3019 0251 4083 0360 01')
        b = 'IR570600301902514083036001'
        c = 'bank mehriran'
        d = '3019025140830361'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_seventeen(self):
        k = Main.Ibanist(an='3019025140830361', bank='6')
        b = 'IR570600301902514083036001'
        c = 'bank mehriran'
        d = '3019025140830361'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_eighteen(self):
        k = Main.Ibanist(an='30190 25140   830361', bank='6')
        b = 'IR570600301902514083036001'
        c = 'bank mehriran'
        d = '3019025140830361'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_nineteen(self):
        k = Main.Ibanist(iban='IR570600301902514083036001', bank='6', an='3019025140830361')
        b = 'IR570600301902514083036001'
        c = 'bank mehriran'
        d = '3019025140830361'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_twenty(self):
        k = Main.Ibanist(iban='520150000000171300615501')
        b = 'IR520150000000171300615501'
        c = 'bank sepah'
        d = '0171300615501'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_22(self):
        k = Main.Ibanist(iban='52015000 000017 1300 615501')
        b = 'IR520150000000171300615501'
        c = 'bank sepah'
        d = '0171300615501'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_23(self):
        k = Main.Ibanist(an='0171300615501', bank='9')
        b = 'IR520150000000171300615501'
        c = 'bank sepah'
        d = '0171300615501'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_24(self):
        k = Main.Ibanist(an='017 130 0 6 1 5  501', bank='9')
        b = 'IR520150000000171300615501'
        c = 'bank sepah'
        d = '0171300615501'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_25(self):
        k = Main.Ibanist(an='17 130 0 6 1 5  501', bank='9')
        b = 'IR520150000000171300615501'
        c = 'bank sepah'
        d = '0171300615501'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())

    def test_26(self):
        k = Main.Ibanist(iban='52015000 000017 1300 615501', an='17 130 0 6 1 5  501', bank='9')
        b = 'IR520150000000171300615501'
        c = 'bank sepah'
        d = '0171300615501'
        e = f'{b} {c} {d}'
        self.assertEqual(e, k.__str__())


if __name__ == '__main__':
    unittest.main()
