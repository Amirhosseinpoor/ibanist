import re
import banks


def main():

    class Ibanist:
        def __init__(self):
            print("shomare shaba:1\nshomare hesab:2\nsehat shomare shaba:3")
            inp = input('vared konid:')
            match inp:
                case '1':
                    self.shomare_shaba()
                case '2':
                    self.shomare_hesab()
                case '3':
                    self.sehat_shomare_shaba()

        def shomare_shaba(self, generate=True):
            if generate:
                iban = self.sehat_shomare_shaba(valid=False)
            self.tajzie(iban)

        def tajzie(self, iban):
            bi = self.real_number(iban)[2:5]
            bank = banks.pishshomare_bank[bi]
            an = self.real_number(iban)[5:]
            an = re.sub(r'^0+', '', an)
            match bi:
                case '016':  # bank keshavarzi
                    if len(an) == 9:
                        an = '0' + an
                case '018':  # bank tejarat
                    if len(an) == 9:
                        an = '0' + an
                case '013':  # bank refah
                    an = re.sub(r'^1', '', an)
                    an = re.sub(r'^0+', '', an)
                    if len(an) == 9:
                        an = '0' + an
                case '019':  # bank saderat
                    if len(an) == 12:
                        an = '0' + an
                case '054':  # bank parsian
                    an = re.sub(r'1219', '', an)
                case '060':  # bank mehriran
                    an = an[:-3] + an[-1]
                case '017':  # bank meli
                    if len(an) == 12:
                        an = '0' + an
                case '012':  # bank melat
                    an = re.sub(r'^1', '', an)
                    an = re.sub(r'^0+', '', an)
                    an = re.sub(r'^2', '', an)
                    an = re.sub(r'^0+', '', an)

            iban = 'IR' + self.real_number(iban)
            iban_realnumber = self.real_number(iban)
            iban_realnumber_ir = iban_realnumber + '1827'
            cd = iban_realnumber[0:2]
            iban_realnumber_ir_cd = iban_realnumber_ir + cd
            iban_realnumber_ir_cd = re.sub(r'^..', '', iban_realnumber_ir_cd)

            if int(iban_realnumber_ir_cd) % 97 == 1 and len(iban_realnumber) == 24:
                print(iban, '\t', an, '\t', bank)
            else:
                print("invalid")

        def shomare_hesab(self):
            print('bank keshavarzi:1\nbank tejarat:2\nbank refah:3\nbank saderat:4\n'
                  'bank parsian:5\nbank mehriran:6\nbank meli:7\nbank melat:8')
            inp = input('bank ra entekhab konid : ')
            match inp:
                case '1':
                    self.bank_keshavarzi()
                case '2':
                    self.bank_tejarat()
                case '3':
                    self.bank_refah()
                case '4':
                    self.bank_saderat()
                case '5':
                    self.bank_parsian()
                case '6':
                    self.bank_mehriran()
                case '7':
                    self.bank_meli()
                case '8':
                    self.bank_melat()

        def sehat_shomare_shaba(self, valid=True):
            while True:
                iban = input("shomare shaba ra vared konid:")
                iban_realnumber = self.real_number(iban)
                if len(iban_realnumber) != 24:
                    print("invalid")
                    continue
                iban_realnumber_ir = iban_realnumber + '1827'
                cd = iban_realnumber[0:2]
                iban_realnumber_ir_cd = iban_realnumber_ir + cd
                iban_realnumber_ir_cd = re.sub(r'^..', '', iban_realnumber_ir_cd)
                if int(iban_realnumber_ir_cd) % 97 == 1:
                    break
                else:
                    print("invalid")
                    continue

            if valid:
                print('valid')
            else:
                return iban

        def real_number(self, num):
            num = re.sub(r' ', '', num)
            num = re.sub(r'-', '', num)
            num = re.sub(r'_', '', num)
            num = re.sub(r'IR', '', num)
            num = re.sub(r'Ir', '', num)
            num = re.sub(r'iR', '', num)
            num = re.sub(r'ir', '', num)
            return num

        def bank_keshavarzi(self):
            cc = 'IR'
            bi = banks.bank_pishshomare['bank keshavarzi']
            an = input('shomare hesab ra vared konid : ')
            an = re.sub(r' ', '', an)
            if len(an) == 9:
                an = '0' + an
            bban = bi + "000000000" + str(an)
            cd = str(98 - int(bban + "182700") % 97)
            if len(cd) < 2:
                cd = "0" + str(cd)
            iban = cc + cd + bban
            self.tajzie(iban)

        def bank_tejarat(self):
            cc = 'IR'
            bi = banks.bank_pishshomare['bank tejarat']
            an = input('shomare hesab :')
            an = re.sub(r' ', '', an)
            if len(an) == 9:
                an = '0' + an
            bban = bi + "000000000" + str(an)
            cd = str(98 - int(bban + "182700") % 97)
            if len(cd) < 2:
                cd = "0" + str(cd)
            iban = cc + cd + bban
            self.tajzie(iban)

        def bank_refah(self):
            cc = 'IR'
            bi = banks.bank_pishshomare['bank refah']
            an = input('shomare hesab :')
            an = re.sub(r' ', '', an)
            if len(an) == 9:
                an = '0' + an
            bban = bi + "010000000" + str(an)
            cd = str(98 - int(bban + "182700") % 97)
            if len(cd) < 2:
                cd = "0" + str(cd)
            iban = cc + cd + bban
            self.tajzie(iban)

        def bank_saderat(self):
            cc = 'IR'
            bi = banks.bank_pishshomare['bank saderat iran']
            an = input('shomare hesab :')
            an = re.sub(r' ', '', an)
            if len(an) == 12:
                an = '0' + an
            bban = bi + "000000" + str(an)
            cd = str(98 - int(bban + "182700") % 97)
            if len(cd) < 2:
                cd = "0" + str(cd)
            iban = cc + cd + bban
            self.tajzie(iban)

        def bank_parsian(self):
            cc = 'IR'
            bi = banks.bank_pishshomare['bank parsian']
            an = input('shomare hesab :')
            an = re.sub(r' ', '', an)
            bban = bi + "01219" + str(an)
            cd = str(98 - int(bban + "182700") % 97)
            if len(cd) < 2:
                cd = "0" + str(cd)
            iban = cc + cd + bban
            self.tajzie(iban)

        def bank_mehriran(self):
            cc = 'IR'
            bi = banks.bank_pishshomare['bank mehriran']
            an = input('shomare hesab :')
            an = re.sub(r' ', '', an)
            bban = bi + "0" + str(an)[:-1] + "00" + str(an)[-1]

            cd = str(98 - int(bban + "182700") % 97)
            if len(cd) < 2:
                cd = "0" + str(cd)
            iban = cc + cd + bban
            self.tajzie(iban)

        def bank_melat(self):
            cc = 'IR'
            bi = banks.bank_pishshomare['bank melat']
            an = input('shomare hesab :')
            an = re.sub(r' ', '', an)
            accounttype = input('accounttype 1 or 2 or 3: ')
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
            self.tajzie(iban)

        def bank_meli(self):
            cc = 'IR'
            bi = banks.bank_pishshomare['bank meli']
            an = input('shomare hesab :')
            an = re.sub(r' ', '', an)
            if len(an) == 12:
                an = '0' + an
            accounttype = input('accounttype sepordeh = 1 , tashilat = 2: ')
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
            self.tajzie(iban)
            
    Ibanist()

if __name__ == '__main__':
    main()
