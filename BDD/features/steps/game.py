SLOVO = 'АНАГРАММА'

class Game:
    word = SLOVO
    def play(self, inp):
        inp = inp.upper()
        if inp == '':
            return 'Назовите букву!'
        elif len(inp) == 1:
            if inp not in self.word: return 'Нет такой буквы!'
            tmp = ''
            for ch in self.word:
                if inp == ch:
                    tmp += ch
                else:
                    tmp += '_'

            return 'Откройте букву! ' + tmp
        elif inp == self.word:
            return 'Вы угадали слово!'
        else:
            return 'Вы не угадали слово!'
