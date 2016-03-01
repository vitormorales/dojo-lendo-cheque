__author__ = 'vitor'

import unittest
from main import read_check, conversion_dict


class ConversionTest(unittest.TestCase):
    def test_convert_units(self):
        unit_list = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
        for string, value in zip(unit_list, range(1, 10)):
            self.assertEqual(conversion_dict[string], value, 'Erro conversão de unidades')

    def test_convert_exceptions(self):
        except_list = ['dez',
                   'onze',
                   'doze',
                   'treze',
                   'quatorze',
                   'quinze',
                   'dezesseis',
                   'dezesete',
                   'dezoito',
                   'dezenove']
        for string, value in zip(except_list, range(10, 20)):
            self.assertEqual(conversion_dict[string], value, 'Erro conversão numeros > 9 e < 20')

    def test_convert_tens(self):
        tens_list = ['vinte',
                   'trinta',
                   'quarenta',
                   'cinquenta',
                   'sessenta',
                   'setenta',
                   'oitenta',
                   'noventa']
        for string, value in zip(tens_list, range(20, 100, 10)):
            self.assertEqual(conversion_dict[string], value, 'Erro conversão de dezenas')

    def test_convert_hundreds(self):
        hundreds_list = ['cem',
                   'duzentos',
                   'trezentos',
                   'quatrocentos',
                   'quinhentos',
                   'seiscentos',
                   'setecentos',
                   'oitocentos',
                   'novecentos']
        for string, value in zip(hundreds_list, range(100, 1000, 100)):
            self.assertEqual(conversion_dict[string], value, 'Erro conversão de centenas')

        self.assertEqual(conversion_dict['cento'], 100, 'Erro conversão de "cento"')


class ReadCheckTests(unittest.TestCase):
    def test_read_0e50(self):
        self.assertEqual(read_check('cinquenta centavos'), '0,50')

    def test_read_1(self):
        self.assertEqual(read_check('um real'), '1,00')

    def test_read_2(self):
        self.assertEqual(read_check('dois reais'), '2,00')

    def test_read_2e29(self):
        self.assertEqual(read_check('dois reais e vinte e nove centavos'), '2,29')

    def test_read_2523e18(self):
        self.assertEqual(read_check('dois mil quinhentos e vinte e três reais e dezoito centavos'), '2523,18')

    def test_read_1527e19(self):
        self.assertEqual(read_check('um mil quinhentos e vinte e sete reais e dezenove centavos'), '1527,19')

    def test_read_invalid(self):
        self.assertEqual(read_check('um milhão duzentos mil quatrocentos e quarenta '
                                    'e dois reais e noventa e nove centavos'), '1200442,99')

    def test_read_invalid(self):
        self.assertEqual(read_check('nada consta'), '0,00')

if __name__ == "__main__":
    unittest.main(verbosity=2)