__author__ = 'ipetrash'

"""Модуль для создания документов FictionBook версии 2.0 (fb2)."""


# <FictionBook xmlns="http://www.gribuser.ru/xml/fictionbook/2.0"
# xmlns:l="http://www.w3.org/1999/xlink">
# <description>
#     ...
#   </description>
#   <body>
#     ...
#   </body>
#   <body name="notes">
#     ...
#   </body>
#   <binary id="cover.jpg" content-type="image/jpeg">/9j/
#     4AAQSkZJRgABAgAAZABkAAD/
#     ...
#   </binary>
# </FictionBook>


class Title_Info:
    # Подчиненные элементы
    # Должен содержать в перечисленном порядке:
    # <genre> - 1..n (любое число, один обязaтелен);
    # <author> - 1..n (любое число, один обязaтелен);
    # <book-title> - 1 (один, обязателен);
    # <annotation> - 0..1 (один, опционально);
    # <keywords> - 0..1 (один, опционально);
    # <date> - 0..1 (один, опционально);
    # <coverpage> - 0..1 (один, опционально);
    # <lang> - 1 (один, обязателен);
    # <src-lang> - 0..1 (один, опционально);
    # <translator> - 0..n (любое число, опционально);
    # <sequence> - 0..n (любое число, опционально).

    def __init__(self):
        self.genre = list()


class Document_Info:
    pass

class Publish_Info:
    pass

class Custom_Info:
    pass

class Description:
    # Поля раздела description:
    # <title-info> - 1 (один, обязателен);
    # <document-info> - 1 (один, обязателен);
    # <publish-info> - 0..1 (один, опционально);
    # <custom-info> - 0..n (любое число, опционально);
    # То есть обязательны разделы <title-info> и <document-info>, а остальные
    # добавляются по необходимости.

    def __init__(self):
        self.title_info = Title_Info()
        self.document_info = Document_Info()
        self.publish_info = None
        self.custom_info = list()

    def get_source(self):
        return '<description>' + '</description>'


class Body:
    pass
    # <image> - 0..1 (один, опционально) - задается изображение
    # для отображения в начале книги (или конкретного <body>);
    # <title> - 0..1 (один, опционально) - задается заглавие
    # для отображения в начале книги (или конкретного <body>);
    # <epigraph> - 0..n (любое число, опционально) - задаются эпиграфы к книге;
    # <section> - 1..n (любое число, один обязaтелен) - задаются
    # части (главы, прочие структурные единицы) книги;


class Binary:
    pass
    # Не содержит подчиненных элементов.
    # Должен содержать текст, представляющий собой двоичные данные,
    # кодированные методом base64


class FB2:
    def __init__(self):
        self.description = Description()  # Одно и только одно вхождение
        self.body = [Body()]  # Одно или более вхождений
        self.binary = list()  # Любое число вхождений

    def add_body(self):
        self.body.append(Body())

    def add_binary(self):
        self.binary.append(Binary())

    def get_source(self):
        source_fb2 = ''
        source_fb2 += ('<FictionBook xmlns="http://www.gribuser.ru/xml/fictionbook/2.0" '
                       'xmlns:l="http://www.w3.org/1999/xlink">')
        source_fb2 += self.description.get_source()
        source_fb2 += '</FictionBook>'

        from xml.dom.minidom import parseString
        source_fb2 = parseString(source_fb2).toprettyxml(indent=' ')
        return source_fb2