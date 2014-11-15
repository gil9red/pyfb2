from pyfb2.epigraph import Epigraph

__author__ = 'ipetrash'


""""""


class Section:
    """"""

    # Описание
    # Секция, основной структурный блок книги
    #
    # Атрибуты
    # id (опциональный) - Идентификатор (якорь, метка) для ссылок на данный элемент
    # xml:lang (опциональный) - язык.
    #
    # Подчиненные элементы
    # Должен содержать последовательность элементов в таком порядке:
    #   1. <title> 0..1 (опционально);
    #   2. <epigraph> 0..n (любое число, опционально);
    #   3. <image> 0..1 (опционально);
    #   4. <annotation> 0..1 (опционально);
    #   5. Один из вариантов,
    #     5.1. либо вложенные секции:
    #       5.1.1 <section> - (любое число, обязательно);
    #     5.2. либо произвольный набор (в произвольном количестве) из следующих элементов:
    #       5.2.1 <p>;
    #       5.2.2 <image>;
    #       5.2.3 <poem>;
    #       5.2.4 <subtitle>;
    #       5.2.5 <cite>;
    #       5.2.6 <empty-line>;
    #       5.2.7 <table>.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    #   <body>;
    #   <section>.

    def __init__(self):
        self.id = None
        self.lang = None

        self.__title = None  # 0..1 (опционально);
        self.epigraph = Epigraph()  # 0..n (любое число, опционально);
        self.__image = None  # 0..1 (опционально);
        self.__annotation = None  # 0..1 (опционально);

        self.__sub_sections = []  # список вложенных секций (5.1)
        self.__sub_elements = []  # список элементов: p, image, poem и т.п. (5.2)

        # Должен содержать последовательность элементов в таком порядке:
        #   1. <title> 0..1 (опционально);
        #   2. <epigraph> 0..n (любое число, опционально);
        #   3. <image> 0..1 (опционально);
        #   4. <annotation> 0..1 (опционально);
        #   5. Один из вариантов,
        #     5.1. либо вложенные секции:
        #       5.1.1 <section> - (любое число, обязательно);
        #     5.2. либо произвольный набор (в произвольном количестве) из следующих элементов:
        #       5.2.1 <p>;
        #       5.2.2 <image>;
        #       5.2.3 <poem>;
        #       5.2.4 <subtitle>;
        #       5.2.5 <cite>;
        #       5.2.6 <empty-line>;
        #       5.2.7 <table>.

        # TODO: добавить подчиненные элементы

    def append_sub_section(self, s=None):
        if s:
            self.__sub_sections.append(s)
        else:
            s = Section()
            self.__sub_sections.append(s)
            return s


    def get_source(self):
        # TODO: доделать
        source = '<section'
        if self.id:
            source += ' id="{}"'.format(self.id)

        if self.lang:
            source += ' xml:lang="{}"'.format(self.lang)

        source += '>'

        if self.__title:
            source += self.__title.get_source()

        source += self.epigraph.get_source()

        if self.__image:
            source += self.__image.get_source()

        if self.__annotation:
            source += self.__annotation.get_source()

        # if not self.__sub_sections and not self.__sub_elements:
        #     raise NameError('Содержимое секции пусто.')

        if self.__sub_sections and self.__sub_elements:
            raise NameError('Одновременно существуют вложенные секции и список из элементов.')

        for i in self.__sub_sections:
            source += i.get_source()

        for i in self.__sub_elements:
            source += i.get_source()

        source += '</section>'
        return source