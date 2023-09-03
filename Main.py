import re
import banks


class Ibanist:
    def __init__(self, iban='', an='', bank='', accounttype=''):
        self.valid = False
        if an != '':
            self.valid = True
        self.accountype = accounttype
        self.iban = iban
        self.an = an
        self.bi = banks.bank_pishshomare[banks.num_bunk[bank]]

        self.bank, self.an = self.parse(self.iban)
        self.truth(self.iban, self.bank, self.an)

    def truth(self, iban, bank, an):
        iban_realnumber = self.real_number(iban)
        iban_realnumber_ir = iban_realnumber + '1827'
        cd = iban_realnumber[0:2]
        iban_realnumber_ir_cd = iban_realnumber_ir + cd
        iban_realnumber_ir_cd = re.sub(r'^..', '', iban_realnumber_ir_cd)

        if int(iban_realnumber_ir_cd) % 97 == 1 and len(iban_realnumber) == 24:
            return bank
        else:
            print('invalid')

    def parse(self, iban):
        cc = 'IR'
        if self.valid:
            bi = self.bi
            an = self.an
        else:
            bi = self.real_number(iban)[2:5]
            an = self.real_number(iban)[5:]
            an = re.sub(r'^0+', '', an)
        bank = banks.pishshomare_bank[bi]

        match bi:

            case '016':  # bank keshavarzi
                if len(an) == 9:
                    an = '0' + an
                self.bank_keshavarzi(cc, bi, an)

            case '018':  # bank tejarat
                if len(an) == 9:
                    an = '0' + an
                self.bank_tejarat(cc, bi, an)

            case '013':  # bank refah
                an = re.sub(r'^1', '', an)
                an = re.sub(r'^0+', '', an)
                if len(an) == 9:
                    an = '0' + an
                self.bank_refah(cc, bi, an)

            case '019':  # bank saderat
                if len(an) == 12:
                    an = '0' + an
                self.bank_saderat(cc, bi, an)

            case '054':  # bank parsian
                an = re.sub(r'1219', '', an)
                self.bank_parsian(cc, bi, an)

            case '060':  # bank mehriran
                an = an[:-3] + an[-1]
                self.bank_mehriran(cc, bi, an)

            case '017':  # bank meli
                if len(an) == 12:
                    an = '0' + an
                self.bank_meli(cc, bi, an, self.accountype)

            case '012':  # bank melat
                an = re.sub(r'^1', '', an)
                an = re.sub(r'^0+', '', an)
                an = re.sub(r'^2', '', an)
                an = re.sub(r'^0+', '', an)
                self.bank_melat(cc, bi, an, self.accountype)

        return bank, an

    def real_number(self, num):
        num = re.sub(r' ', '', num)
        num = re.sub(r'-', '', num)
        num = re.sub(r'_', '', num)
        num = re.sub(r'IR', '', num)
        num = re.sub(r'Ir', '', num)
        num = re.sub(r'iR', '', num)
        num = re.sub(r'ir', '', num)
        return num

    def bank_keshavarzi(self, cc, bi, an):
        an = re.sub(r' ', '', an)
        if len(an) == 9:
            an = '0' + an
        bban = bi + "000000000" + str(an)
        cd = str(98 - int(bban + "182700") % 97)
        if len(cd) < 2:
            cd = "0" + str(cd)
        iban = cc + cd + bban
        self.iban = iban

    def bank_tejarat(self, cc, bi, an):
        an = re.sub(r' ', '', an)

        if len(an) == 9:
            an = '0' + an
        bban = bi + "000000000" + str(an)
        cd = str(98 - int(bban + "182700") % 97)
        if len(cd) < 2:
            cd = "0" + str(cd)
        iban = cc + cd + bban
        self.iban = iban

    def bank_refah(self, cc, bi, an):
        an = re.sub(r' ', '', an)

        if len(an) == 9:
            an = '0' + an
        bban = bi + "010000000" + str(an)
        cd = str(98 - int(bban + "182700") % 97)
        if len(cd) < 2:
            cd = "0" + str(cd)
        iban = cc + cd + bban
        self.iban = iban

    def bank_saderat(self, cc, bi, an):
        an = re.sub(r' ', '', an)

        if len(an) == 12:
            an = '0' + an
        bban = bi + "000000" + str(an)
        cd = str(98 - int(bban + "182700") % 97)
        if len(cd) < 2:
            cd = "0" + str(cd)
        iban = cc + cd + bban
        self.iban = iban

    def bank_parsian(self, cc, bi, an):
        an = re.sub(r' ', '', an)

        bban = bi + "01219" + str(an)
        cd = str(98 - int(bban + "182700") % 97)
        if len(cd) < 2:
            cd = "0" + str(cd)
        iban = cc + cd + bban
        self.iban = iban

    def bank_mehriran(self, cc, bi, an):
        an = re.sub(r' ', '', an)

        bban = bi + "0" + str(an)[:-1] + "00" + str(an)[-1]

        cd = str(98 - int(bban + "182700") % 97)
        if len(cd) < 2:
            cd = "0" + str(cd)
        iban = cc + cd + bban
        self.iban = iban

    def bank_melat(self, cc, bi, an, accounttype='1'):
        an = re.sub(r' ', '', an)

        if accounttype == "1":
            bban = bi + "000000000" + str(an)
        elif accounttype == "2":
            bban = bi + "001000000" + str(an)
        elif accounttype == "3":
            bban = bi + "002000000" + str(an)
        cd = str(98 - int(bban + "182700") % 97)
        if len(cd) < 2:
            cd = "0" + str(cd)
        iban = cc + cd + bban
        self.iban = iban

    def bank_meli(self, cc, bi, an, accounttype='1'):
        an = re.sub(r' ', '', an)

        if len(an) == 12:
            an = '0' + an
        if accounttype == "1":
            # sepordeh
            bban = bi + "000000" + str(an)
        elif accounttype == "2":
            # tashilat
            bban = bi + "10000" + str(an)
        cd = str(98 - int(bban + "182700") % 97)
        if len(cd) < 2:
            cd = "0" + str(cd)
        iban = cc + cd + bban
        self.iban = iban


# '1': 'bank keshavarzi', '2': 'bank tejarat', '3': 'bank refah', '4': 'bank saderat iran',
#         '5': 'bank parsian', '6': 'bank mehriran', '7': 'bank meli iran', '8': 'bank melat',

