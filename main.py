__author__ = 'vitor'


def convert_numbers(numbers_str):
    result = 0
    for word in numbers_str.split():
        try:
            result += conversion_dict[word]
        except KeyError:
                result *= multipliers_dict.get(word, 1)
    return result


def read_check(phrase):
    result = 0
    reading_number = 0
    phrase = phrase.replace(' e ', ' ')

    for word in phrase.split():
        try:
            reading_number += conversion_dict[word]
        except KeyError:
            reading_number *= multipliers_dict.get(word, 1)
            result += reading_number
            reading_number = 0

    result = '{:.2f}'.format(result).replace('.', ',')
    return result

conversion_dict = {'um': 1,
                   'dois': 2,
                   'três': 3,
                   'quatro': 4,
                   'cinco': 5,
                   'seis': 6,
                   'sete': 7,
                   'oito': 8,
                   'nove': 9,
                   'dez': 10,
                   'onze': 11,
                   'doze': 12,
                   'treze': 13,
                   'quatorze': 14,
                   'quinze': 15,
                   'dezesseis': 16,
                   'dezesete': 17,
                   'dezoito': 18,
                   'dezenove': 19,
                   'vinte': 20,
                   'trinta': 30,
                   'quarenta': 40,
                   'cinquenta': 50,
                   'sessenta': 60,
                   'setenta': 70,
                   'oitenta': 80,
                   'noventa': 90,
                   'cem': 100,
                   'cento': 100,
                   'duzentos': 200,
                   'trezentos': 300,
                   'quatrocentos': 400,
                   'quinhentos': 500,
                   'seiscentos': 600,
                   'setecentos': 700,
                   'oitocentos': 800,
                   'novecentos': 900
                   }

multipliers_dict = {'mil': 1000,
                    'milhão': 1000000,
                    'centavos': 1/100
                    }

if __name__ == '__main__':
    check = input("Digite um valor de cheque por extenso: ")
    print(read_check(check))