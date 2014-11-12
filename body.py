__author__ = 'ipetrash'


from image import Image
from title import Title
from section import Section
from epigraph import Epigraph


class BodyItem:
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

    # TODO: доделать

    def __init__(self):
        self.name = None
        self.lang = None
        self.__image = None  # 0..1 (один, опционально)
        self.__title = None  # 0..1 (один, опционально)
        self.epigraph = Epigraph()  # 0..n (любое число, опционально) # TODO: доделать
        self.section = Section()  # 1..n (любое число, один обязaтелен) # TODO: доделать

    def get_image(self):
        if not self.__image:
            self.__image = Image()
        return self.__image
    image = property(get_image)

    def get_title(self):
        if not self.__title:
            self.__title = Title()
        return self.__title
    title = property(get_title)

    def get_source(self):
        source = '<body'
        if self.name:
            source += ' name="{}"'.format(self.name)
        if self.lang:
            source += ' xml:lang="{}"'.format(self.lang)
        source += '>'

        if self.__image:
            source += self.__image.get_source()

        if self.__title:
            source += self.__title.get_source()

        source += self.epigraph.get_source()
        source += self.section.get_source()
        source += '</body>'
        return source


class Body:
    """"""

    # TODO: доделать

    def __init__(self):
        self.list = []

    def append(self):
        item = BodyItem()
        self.list.append(item)

    def get_source(self):
        # TODO: проверять на пустоту список body
        # как минимум одно тело должно быть

        source = ''
        for b in self.list:
            source += b.get_source()

        return source