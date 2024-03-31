# leveling
Выравнивание текста по бокам.
Вывод предложений
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или testmodule.py
Вывод	стандартный вывод или output.txt
Напишите два класса: LeftParagraph и RightParagraph для печати абзаца с выравниванием по левому и правому краю.

При инициализации экземпляры обоих классов должны принимать целое число — ширину поля вывода. В обоих классах нужно реализовать метод add_word для добавления слова в абзац и метод end, выводящий полученный абзац на печать и начинающий формирование нового.

Гарантируется, что длина любого слова меньше ширины поля вывода.

Формат ввода
Каждый тест представляет собой код, в котором будут использоваться ваши классы.
Файл c решением не обязательно называть solution.py, он будет переименован автоматически.
Тест запускается с вашими классами, а его вывод сравнивается с правильным решением.

Пример
Ввод	Вывод
from solution import LeftParagraph, RightParagraph

lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
print()

abc defg
hi
jklmnopq
r stuv

abc defg
      hi
jklmnopq
  r stuv

