from pyfb2.cite import Cite
from pyfb2.empty_line import Empty_Line
from pyfb2.paragraph import Paragraph
from pyfb2.poem import Poem
from pyfb2.text_author import Text_Author


__author__ = 'ipetrash'


""""""


class Epigraph:
    """"""

    # Описание
    # Эпиграф
    #
    # Атрибуты
    # id (опциональный) - Идентификатор (якорь, метка) для ссылок на данный элемент
    #
    # Подчиненные элементы
    # Содержит в перечисленном порядке элементы:
    # 1. Произвольный набор (в произвольном количестве)
    #      <p>;
    #      <poem>;
    #      <cite>;
    #      <empty-line>;
    # 2. <text-author> 0..n (любое число, опционально).
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <body>;
    # <section>;
    # <poem>.
    #
    # Пример использования
    # <epigraph>
    # <p>"The truth is the one thing that nobody will believe."</p>
    # <text-author>GEORGE BERNARD SHAW 1856-1950</text-author>
    # </epigraph>

    # TODO: доделать

    def __init__(self):
        self.id = None

        self.__list = []
        self.__text_authors = []

    def append_paragraph(self, p=None):
        if p:
            self.__list.append(p)
        else:
            p = Paragraph()
            self.__list.append(p)
            return p

    def append_poem(self, p=None):
        if p:
            self.__list.append(p)
        else:
            p = Poem()
            self.__list.append(p)
            return p

    def append_cite(self, c=None):
        if c:
            self.__list.append(c)
        else:
            c = Cite()
            self.__list.append(c)
            return c

    def append_empty_line(self):
        self.__list.append(Empty_Line())

    def append_text_author(self, ta=None):
        if ta:
            self.__text_authors.append(ta)
        else:
            ta = Text_Author()
            self.__text_authors.append(ta)
            return ta

    def get_source(self):
        source = '<epigraph'

        if self.id:
            source += ' id="{}"'.format(self.id)

        source += '>'

        for i in self.__list:
            source += i.get_source()

        for i in self.__text_authors:
            source += i.get_source()

        source += '</epigraph>'
        return source