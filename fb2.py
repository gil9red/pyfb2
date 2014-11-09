__author__ = 'ipetrash'


"""Модуль для создания документов FictionBook версии 2.0 (fb2)."""


from title_info import Title_Info
from document_info import Document_Info

class Publish_Info:
    """"""

    def __init__(self):
        pass

    def get_source(self):
        pass


class Custom_Info:
    """"""

    def __init__(self):
        pass

    def get_source(self):
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
        source = '<description>'
        source += self.title_info.get_source()
        source += self.document_info.get_source()
        if self.publish_info:
            source += self.publish_info.get_source()
        for ci in self.custom_info:
            source += ci.get_source()
        source += '</description>'
        return source


class Title:
    """"""

    def __init__(self):
        pass

    def get_source(self):
        pass


class Image:
    """"""

    def __init__(self):
        pass

    def get_source(self):
        pass


class Title:
    """"""

    def __init__(self):
        pass

    def get_source(self):
        pass


class Epigraph:
    """"""

    def __init__(self):
        pass

    def get_source(self):
        pass


class Section:
    """"""

    def __init__(self):
        pass

    def get_source(self):
        pass


class Body:
    """"""

    # Атрибуты
    # name - (опционально) - название <body>, устанавливается в "notes" для тела, содержащего сноски.
    # xml:lang - (опционально) - задание языка для <body>
    #
    # Подчиненные элементы
    # Содержит в перечисленном порядке следующие элементаы:
    # <image> - 0..1 (один, опционально) - задается изображение для отображения в начале книги (или конкретного <body>);
    # <title> - 0..1 (один, опционально) - задается заглавие для отображения в начале книги (или конкретного <body>);
    # <epigraph> - 0..n (любое число, опционально) - задаются эпиграфы к книге;
    # <section> - 1..n (любое число, один обязaтелен) - задаются части (главы, прочие структурные единицы) книги;
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <FictionBook> (любое число, один обязaтелен)
    #
    # Описание
    # Здесь собственно и находится текст книги.
    # Хотя формально количество и порядок экземпляров <body> не ограничены, но для
    # совместимости с существующим софтом рекомендуется:
    # Помещать весь основной текст документа в первом <body> (сразу после <description>).
    # При наличии в тексте сносок (<a type="note">) сам текст сносок должен размещаться во
    # втором <body> с атрибутом name="notes".
    # При наличии кроме сносок также комментариев и т.п., что в оригинале размещено в конце
    # книги - создается третье <body> с атрибутом name="comments" или без атрибута name.
    # При отсутствии сносок второе и третье <body> должно отсутствовать, а весь текст размещаться
    # в первом.
    #
    # Пример использования
    # <body name="notes">
    #  <title><p>Примечания</p></title>
    #  <section id="note1">
    #   <title>
    #    <p>1</p>
    #   </title>
    #   <p>Известный английский архитектор XVIII века, испытавший в
    #   своем творчестве сильное влияние античной архитектуры. (Здесь и
    #   далее прим. ред.)</p>
    #  </section>
    #  <section id="note2">
    #   <title>
    #    <p>2</p>
    #   </title>
    #   <p>Американский просветитель, живший в XVIII веке</p>
    #  </section>
    # </body>

    def __init__(self):
        self.name = None
        self.lang = None
        self.image = Image()
        self.title = Title()
        self.epigraph = []
        self.section = [Section()]

    def get_source(self):
        name = ' name="{}"'.format(self.name) if self.name else ''
        lang = ' xml:lang="{}"'.format(self.lang) if self.lang else ''
        source = '<body{}{}>'.format(name, lang)

        if self.image:
            source += self.image.get_source()

        if self.title:
            source += self.title.get_source()

        for e in self.epigraph:
            source += e.get_source()

        for s in self.section:
            source += s.get_source()

        source += '</body>'
        return source


class Binary:
    """"""

    # Не содержит подчиненных элементов.
    # Должен содержать текст, представляющий собой двоичные данные,
    # кодированные методом base64

    # Здесь находятся присоединенные двоичные данные. На данный момент это только изображения,
    # и расширение данного списка не планируется.
    # В файле может содержаться произвольное количество (несколько, один, вовсе отсутсвует)
    # элементов <binary>

    # Атрибуты
    # content-type (обязателен) - MIME-тип данных (картинки). На данный момент
    # поддерживются "image/jpeg" и "image/png".
    # id (обязателен) - Идентификатор ("имя файла", а точнее якорь) для ссылок
    # на данные (картинку).

    # Пример использования
    # <binary id="cover.jpg" content-type="image/jpeg">
    # AQMAEAMDBgkAAA/tAAAe7gAANHz/2wCEAAgGBgYGBggGBggMCAcIDA4KCAgKDhANDQ4NDRAR
    # DA4NDQ4MEQ8SExQTEg8YGBoaGBgjIiIiIycnJycnJycnJycBCQgICQoJCwkJCw4LDQsOEQ4O
    # ...
    # h9x8OJ/B/c+gfbXM/wDQ/qcPZ9HHjqaPi17zZ4+6deEYNxtP+H1v8Opsec//2Q==
    # </binary>

    def __init__(self):
        self.id = None
        self.content_type = None
        self.data = None

    def get_source(self):
        # TODO: проверять значения атрибутов
        source = '<binary id="{}" content-type="{}">'.format(self.id, self.content_type)
        source += self.data
        source += '</binary>'
        return source


class FB2:
    """"""

    # Раздел FictionBook состоит из вложенных подразделов в указанном ниже порядке:
    # <description> - который описывает заголовок документа. Одно и только одно вхождение.
    # (фразы вроде "одно и только одно вхождение" говорят, сколько раз подряд может идти
    # данный тэг в данном месте документа)
    # <body> - описывает тело документа. Одно или более вхождений.
    # <binary> - содержит приложенные к файлу двоичные объекты - картинки и прочее.
    # Любое число вхождений.
    # Иными словами, присутствуют как минимум разделы <description> с <body>, а
    # остальное - по необходимости.

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
        for b in self.body:
            source_fb2 += b.get_source()
        for bi in self.binary:
            source_fb2 += bi.get_source()
        source_fb2 += '</FictionBook>'

        from xml.dom.minidom import parseString
        source_fb2 = parseString(source_fb2).toprettyxml(indent=' ')
        return source_fb2