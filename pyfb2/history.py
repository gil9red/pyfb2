from pyfb2.cite import Cite
from pyfb2.empty_line import Empty_Line
from pyfb2.paragraph import Paragraph
from pyfb2.poem import Poem
from pyfb2.subtitle import Subtitle


__author__ = 'ipetrash'

""""""


class History:
    """"""

    # Описание
    # История изменении данного FB2 документа.
    # Рекомендуется к заполнению ответственным за документ.
    #
    # Поддерживается
    # Рядом ориентированных на FB2 ?читалок?.
    # Хоть и не отображается в библиотеках, доступно для просмотра (и редактирования)
    # в любом (в том числе и ориентированном на FB2) редакторе.
    #
    # Атрибуты
    # id (опционально) - Идентификатор (якорь, метка) для ссылок на данный элемент.
    # xml:lang (опционально) - язык.
    #
    # Подчиненные элементы
    # Может содержать произвольный набор (в произвольном количестве) из следующих элементов:
    # <p>;
    # <poem>;
    # <cite>;
    # <subtitle>;
    # <empty-line>;
    # <table> (с версии 2.1).
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <document-info> - 0..1 (один, опционально).
    #
    # Смотри также
    # <annotation>, как аналогичный по структуре, но не по смыслу элемент.

    # TODO: доделать

    def __init__(self):
        self.id = None  # (опционально)
        self.lang = None  # (опционально)

        self.__list = []

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

    def append_subtitle(self, st=None):
        if st:
            self.__list.append(st)
        else:
            st = Subtitle()
            self.__list.append(st)
            return st

    def append_empty_line(self):
        self.__list.append(Empty_Line())

    # # TODO: 2.1
    # def append_table(self):
    # pass

    def get_source(self):
        if not self.__list:
            raise NameError('Нет содержимого тэга history.')

        source = '<history'

        if self.id:
            source += ' id="{}"'.format(self.id)

        if self.lang:
            source += ' xml:lang="{}"'.format(self.lang)

        source += '>'

        for i in self.__list:
            source += i.get_source()

        source += '</history>'
        return source