__author__ = 'ipetrash'


class Genre:
    """Описывает жанровую принадлежность книги. Используется для помещения
    книги в рубрикатор библиотеки, по этой причине список возможных жанров
    жестко задается. Допускается указание нескольких жанров."""

    # Атрибуты
    # match (опциональный, значение по умолчанию "100") ? число от "1" до "100",
    # задающее субъективное процентное соответствие данному жанру.
    #
    # Содержит текст - обозначение жанра из списка жанров.
    # http://www.fictionbook.org/index.php/%D0%96%D0%B0%D0%BD%D1%80%D1%8B_FictionBook_2.1

    # Пример:
    # Вестерн с элементами детектива можно описать следующим образом:
    # <genre>adv_western</genre>
    # <genre match="20">detective</genre>

    def __init__(self):
        self.text = None
        self.match = None

    def get_source(self):
        if not self.text:
            raise NameError('Не определен жанр (self.text is None).')

        if self.match:
            return '<genre match="{}">{}</genre>'.format(self.match, self.text)
        else:
            return '<genre>{}</genre>'.format(self.text)