from pyfb2.empty_line import Empty_Line
from pyfb2.paragraph import Paragraph
from pyfb2.text_author import Text_Author

__author__ = 'ipetrash'


""""""


class Cite:
    """"""

    # Описание
    # Предназначен для оформления цитат в тексте книги.
    #
    # Атрибуты
    # id (опциональный) - Идентификатор (якорь, метка) для ссылок на данный элемент
    # xml:lang (опциональный) - язык.
    #
    # Подчиненные элементы
    # Содержит в указанном порядке следующие элементы:
    #     1. Произвольный набор (в произвольном количестве):
    #           <p>;
    #           <subtitle>;
    #           <empty-line/>;
    #           <poem>;
    #           <table> (с версии 2.1);
    #     2. <text-author> 0..n (любое число, опционально) - подпись, автор цитируемого текста.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <annotation>;
    # <epigraph>;
    # <history>;
    # <section>.

    # TODO: доделать

    def __init__(self):
        self.id = None
        self.lang = None

        self.__list = []
        self.__text_authors = []

    def append_paragraph(self):
        p = Paragraph()
        self.__list.append(p)
        return p

    def append_subtitle(self):
        pass
        # s = Subtitle()
        # self.__list.append(s)
        # return s

    def append_empty_line(self):
        self.__list.append(Empty_Line())

    def append_poem(self):
        pass
        # TODO: добавить
        # p = Poem()
        # self.__list.append(p)
        # return p

    def append_table(self):
        pass
        # TODO: добавить
        # t = Table()
        # self.__list.append(t)
        # return t

    def append_text_author(self):
        ta = Text_Author()
        self.__text_authors.append(ta)
        return ta

    def get_source(self):
        source = '<cite'
        if self.id:
            source += ' id="{}"'.format(self.id)
        if self.lang:
            source += ' xml:lang="{}"'.format(self.lang)
        source += '>'

        for i in self.__list:
            source += i.get_source()

        for ta in self.__text_authors:
            source += ta.get_source()

        source += '</cite>'
        return source