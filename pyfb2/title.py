from pyfb2.empty_line import Empty_Line
from pyfb2.paragraph import Paragraph


__author__ = 'ipetrash'


""""""


class Title:
    """"""

    # Описание
    # Название книги, главы, стихотворения
    #
    # Атрибуты
    # xml:lang (опциональный) - язык.
    #
    # Подчиненные элементы
    # Может содержать произвольный набор (в произвольном количестве) из следующих элементов:
    # <p>;
    # <empty-line>.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <body> (опциональный);
    # <section> (опциональный);
    # <poem> (опциональный);
    # <stanza> (опциональный).

    # TODO: доделать

    def __init__(self):
        self.lang = None

        # Cписок может содержать параграфы (<p>) и пустые строки (<empty-line>)
        self.__row_text = []

    def append_paragraph(self, p=None):
        if p:
            self.__row_text.append(p)
        else:
            p = Paragraph()
            self.__row_text.append(p)
            return p

    def append_empty_line(self):
        self.__row_text.append(Empty_Line())

    def get_source(self):
        source = '<title'

        if self.lang:
            source += ' xml:lang="{}"'.format(self.lang)

        source += '>'

        for r in self.__row_text:
            source += r.get_source()

        source += '</title>'
        return source