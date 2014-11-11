__author__ = 'ipetrash'


"""Модуль для создания документов FictionBook версии 2.0 (fb2)."""


from stylesheet import Stylesheet
from description import Description
from body import Body
from binary import Binary


class FB2:
    """"""

    # Описание
    # Корневой элемент документа.
    #
    # Подчиненные элементы
    # Должен содержать в перечисленном порядке:
    # <stylesheet> - 0..n (любое число, опционально);
    # <description> - 1 (один, обязателен);
    # <body> - 1..n (любое число, один обязaтелен);
    # <binary> - 0..n (любое число, опционально).

    # Раздел FictionBook состоит из вложенных подразделов в указанном ниже порядке:
    # <description> - который описывает заголовок документа. Одно и только одно вхождение.
    # (фразы вроде "одно и только одно вхождение" говорят, сколько раз подряд может идти
    # данный тэг в данном месте документа)
    # <body> - описывает тело документа. Одно или более вхождений.
    # <binary> - содержит приложенные к файлу двоичные объекты - картинки и прочее.
    # Любое число вхождений.
    #
    # Иными словами, присутствуют как минимум разделы <description> с <body>, а
    # остальное - по необходимости.

    def __init__(self):
        self.stylesheet = Stylesheet()  # Любое число, опционально
        self.description = Description()  # Одно и только одно вхождение
        self.body = [Body()]  # Одно или более вхождений
        self.binary = Binary()  # Любое число вхождений

    def add_body(self):
        self.body.append(Body())

    def get_source(self):
        source_fb2 = ''
        source_fb2 += ('<FictionBook '
                       'xmlns="http://www.gribuser.ru/xml/fictionbook/2.0" '
                       'xmlns:xlink="http://www.w3.org/1999/xlink">')
        source_fb2 += self.stylesheet.get_source()
        source_fb2 += self.description.get_source()
        for b in self.body:
            source_fb2 += b.get_source()
        source_fb2 += self.binary.get_source()
        source_fb2 += '</FictionBook>'

        from xml.dom.minidom import parseString
        source_fb2 = parseString(source_fb2).toprettyxml(indent='  ')
        return source_fb2