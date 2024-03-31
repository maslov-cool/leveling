class LeftParagraph:
    def __init__(self, n):
        self.n = n
        self.text = ['']

    def add_word(self, word):
        if self.n - len(self.text[-1].strip()) > len(word):
            self.text[-1] = (self.text[-1].strip() +
                             ' ' * (1 if self.n - len(self.text[-1].strip()) - len(word) and
                                    self.text[-1].strip() else 0) + word +
                             ' ' * (self.n - len(self.text[-1].strip()) - len(word) - 1))
        else:
            self.text.append(word)

    def end(self):
        print(*[i for i in self.text if i], sep='\n')
        self.text = ['']


class RightParagraph:
    def __init__(self, n):
        self.n = n
        self.text = ['']

    def add_word(self, word):
        if 8 - len(self.text[-1].strip()) > len(word):
            self.text[-1] = (' ' * (self.n - len(self.text[-1].strip()) - len(word) - (self.text[-1].strip() != ''))
                             + self.text[-1].strip() +
                             ' ' * (1 if self.n - len(self.text[-1].strip()) - len(word) and
                                         self.text[-1].strip() else 0) + word)
        else:
            self.text.append(' ' * (self.n - len(word)) + word.strip())

    def end(self):
        print(*[i for i in self.text if i], sep='\n')
        self.text = ['']


lp = LeftParagraph(8)
lp.add_word('btdwmgil')
lp.add_word('sfwvgybz')
lp.add_word('fkq')
lp.add_word('dtovf')
lp.add_word('p')
lp.add_word('sqjulmv')
lp.add_word('erwao')
lp.add_word('kx')
lp.add_word('r')
lp.add_word('ehypl')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('btdwmgil')
rp.add_word('sfwvgybz')
rp.add_word('fkq')
rp.add_word('dtovf')
rp.add_word('p')
rp.add_word('sqjulmv')
rp.add_word('erwao')
rp.add_word('kx')
rp.add_word('r')
rp.add_word('ehypl')
rp.end()
print()
