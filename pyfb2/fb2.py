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


class Book_Title:
    def __init__(self):
        pass

class Author:
    """Информация об авторе книги, если элемент используется в <title-info>
    или <src-title-info>; или об авторе документа, если в <document-info>."""

    # Подчиненные элементы
    # Содержит в перечисленном порядке следующие элементы:
    # <first-name> - 0..1 (один, обязателен при отсутствии <nickname>, иначе опционально) - имя;
    # <middle-name> - 0..1 (один, опционально) - отчество;
    # <last-name> - 0..1 (один, обязателен при отсутствии <nickname>, иначе опционально) - фамилия;
    # <nickname> - 0..1 (один, обязателен при отсутствии <first-name> и <last-name>, иначе опционально);
    # <home-page> - 0..n (любое число, опционально);
    # <email> - 0..n (любое число, опционально);
    # <id> - 0..1 (один, опционально) с версии 2.2 - идентификатор автора, присваивается библиотекой.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <title-info> 1..n (любое число, один обязателен);
    # <src-title-info> 1..n (любое число, один обязателен) с версии 2.1;
    # <document-info> 1..n (любое число, один обязателен);
    #
    # Пример использования
    # <author>
    #   <first-name>Борис</first-name>
    #   <last-name>Сергеев</last-name>
    # </author>

    def __init__(self):
        self.first_name = None
        self.middle_name = None
        self.last_name = None
        self.nickname = None
        self.home_page = []
        self.email = []
        self.id = None

    def add_home_page(self, value):
        self.home_page.append(value)

    def remove_home_page(self, value):
        self.home_page.remove(value)

    def add_email(self, value):
        self.email.append(value)

    def remove_email(self, value):
        self.email.remove(value)

    def get_source(self):
        # TODO: проверять наличие элементов
        source = '<author>'

        if self.first_name:
            source += '<first-name>{}</first-name>'.format(self.first_name)

        if self.middle_name:
            source += '<middle-name>{}</middle-name>'.format(self.middle_name)

        if self.last_name:
            source += '<last-name>{}</last-name>'.format(self.last_name)

        if self.nickname:
            source += '<nickname>{}</nickname>'.format(self.nickname)

        for hp in self.home_page:
            source += '<home-page>{}</home-page>'.format(hp)

        for e in self.email:
            source += '<email>{}</email>'.format(e)

        if self.id:
            source += '<id>{}</id>'.format(self.id)

        source += '</author>'
        return source


class Lang:
    def __init__(self):
        pass


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
        self.genre = [Genre()]
        self.author = [Author()]
        self.book_title = [Book_Title()]
        self.annotation = None
        self.keywords = None
        self.date = None
        self.coverpage = None
        self.lang = Lang()
        self.src_lang = None
        self.translator = []
        self.sequence = []


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
        self.custom_info = []

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
        self.binary = []  # Любое число вхождений

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