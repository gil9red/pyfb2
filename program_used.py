__author__ = 'ipetrash'


""""""


class Program_Used:
    """"""

    # Описание
    # Перечисляются программы, которые использовались при подготовке документа.
    #
    # Атрибуты
    # xml:lang (опционально) - язык.
    #
    # Подчиненные элементы
    # Нет дочерних элементов, содержит текст.
    #
    # Подчинен
    # Может сожержаться в следующих элементах:
    # <document-info> (опционально).
    #
    # Пример использования
    # <program-used>Dn/2, Opera 8.50, Bred3</program-used>

    # TODO: доделать

    def __init__(self):
        self.lang = None
        self.list = []

    def append(self, program):
        if isinstance(program, list):
            for p in program:
                self.append(p)
        else:
            # Добавим программу, если ее нет в списке:
            if not program in self.list:
                self.list.append(program)
            else:
                print('Элемент "" уже есть в списке.'.format(program))

    def get_source(self):
        if not self.list:
            raise NameError('Список использованных программ пуст.')

        source = '<program-used'
        if self.lang:
            source += ' xml:lang="{}"'.format(self.lang)
        source += '>'
        source += ', '.join(self.list)
        source += '</program-used>'
        return source