
import unittest

SLOVO = 'АНАГРАММА'

def game(inp):
    inp = inp.upper()
    if inp == '':
        return 'Назовите букву!'
    elif len(inp) == 1:
        if inp not in SLOVO: return 'Нет такой буквы!'
        tmp = ''
        for ch in SLOVO:
            if inp == ch:
                tmp += ch
            else:
                tmp += '_'

        return 'Откройте букву!\n' + tmp
    elif inp == SLOVO:
        return 'Вы угадали слово!'
    else:
        return 'Вы не угадали слово!'
        
        
class TestGame(unittest.TestCase):
    def test_silence(self):
        self.assertEqual(game(''), 'Назовите букву!')

    def test_letterinput_A(self):
        self.assertEqual(game('А'), 'Откройте букву!\nА_А__А__А')

    def test_letterinput_M(self):
        self.assertEqual(game('М'), 'Откройте букву!\n______ММ_')

    def test_letterinput_E(self):
        self.assertEqual(game('Е'), 'Нет такой буквы!')

    def test_wordinput(self):
        self.assertEqual(game(SLOVO), 'Вы угадали слово!')

    def test_wordinput(self):
        self.assertEqual(game(SLOVO.replace('А', 'О')), 'Вы не угадали слово!')
        

if __name__ == '__main__':
    unittest.main()
