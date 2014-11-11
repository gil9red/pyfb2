__author__ = 'ipetrash'


""""""


# # TODO: может, список возможных жанров в перечислении описать?
# # http://www.fictionbook.org/index.php/Жанры_FictionBook_2.1
# # http://www.fictionbook.org/index.php/Eng:FictionBook_2.1_genres
# from enum import Enum
# class Genres(Enum):
#     sf_history = "sf_history"
#     sf_action = "sf_action"
#     sf_epic = "sf_epic"
#
# print(Genres.sf_history.value)
# print(type(Genres.sf_history.value))


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

    # TODO: доделать

    def __init__(self, name=None, match=None):
        # TODO: проверять значение match: 0 <= match <= 100

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