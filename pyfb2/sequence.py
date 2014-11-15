__author__ = 'ipetrash'


""""""


class SequenceItem:
    """"""

    # TODO: Доделать

    # Описание
    # Серия изданий, в которую входит книга, и номер в серии.
    #
    # Атрибуты
    # name (обязательный) - название серии;
    # number (опциональный) - номер книги в серии;
    # xml:lang (опциональный) - язык.
    #
    # Подчиненные элементы
    # Нет дочерних элементов.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <title-info> - 0..n (любое число, опционально);
    # <src-title-info> - 0..n (любое число, опционально);
    # <publish-info> - 0..n (любое число, опционально).
    #
    # Пример использования
    # <sequence name="Грегор Эйзенхорн" number="2"/>

    def __init__(self, name=None, number=None, lang=None):
        self.name = name
        self.number = number
        self.lang = lang

    def get_source(self):
        if not self.name or not self.number:
            raise NameError('Не определено название или номер в серии.')

        if self.lang:
            return ('<sequence xml:lang="{}" name="{}" '
                    'number="{}"/>').format(self.lang, self.name, self.number)
        else:
            return '<sequence name="{}" number="{}"/>'.format(self.name, self.number)


class Sequence:
    """"""

    # TODO: Доделать

    def __init__(self):
        self.__list = []

    def append(self, name, number, lang=None):
        si = SequenceItem(name, number, lang)
        self.__list.append(si)
        return si

    def get_source(self):
        source = ''
        for s in self.__list:
            source += s.get_source()

        return source