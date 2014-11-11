from lxml.objectify import NoneElement

__author__ = 'ipetrash'


""""""


class GenreItem:
    """Описывает жанровую принадлежность книги. Используется для помещения
    книги в рубрикатор библиотеки, по этой причине список возможных жанров
    жестко задается. Допускается указание нескольких жанров."""

    # Атрибуты
    # match (опциональный, значение по умолчанию "100") ? число от "1" до "100",
    # задающее субъективное процентное соответствие данному жанру.
    #
    # Содержит текст - обозначение жанра из списка жанров.
    # http://www.fictionbook.org/index.php/Жанры_FictionBook_2.1

    # Пример:
    # Вестерн с элементами детектива можно описать следующим образом:
    # <genre>adv_western</genre>
    # <genre match="20">detective</genre>

    def __init__(self, name=None, match=None):
        self.name = name
        self.match = match

    def get_source(self):
        if not self.name:
            raise NameError('Не определен жанр.')

        if self.match:
            return '<genre match="{}">{}</genre>'.format(self.match, self.name)
        else:
            return '<genre>{}</genre>'.format(self.name)


class Genre:
    """"""

    # TODO: доделать

    def __init__(self):
        self.list = []

    def append(self, name, match=None):
        self.list.append(GenreItem(name, match))

    def get_source(self):
        # Список жанров должен иметь как минимум один жанр
        if not self.list:
            raise NameError('Список жанров пуст.')

        source = ''
        for g in self.list:
            source += g.get_source()

        return source