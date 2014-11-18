from pyfb2.annotation import Annotation
from pyfb2.cite import Cite
from pyfb2.empty_line import Empty_Line
from pyfb2.epigraph import Epigraph
from pyfb2.image import Image
from pyfb2.paragraph import Paragraph
from pyfb2.poem import Poem
from pyfb2.source_text import SourceText
from pyfb2.subtitle import Subtitle
from pyfb2.title import Title

__author__ = 'ipetrash'

""""""


class SectionItem:
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
    # 1. <title> 0..1 (опционально);
    # 2. <epigraph> 0..n (любое число, опционально);
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

    # TODO: доделать

    def __init__(self):
        self.id = None
        self.lang = None

        self.__title = None  # 0..1 (опционально);
        self.epigraph = Epigraph()  # 0..n (любое число, опционально);
        self.__image = None  # 0..1 (опционально);
        self.__annotation = None  # 0..1 (опционально);

        self.__sub_sections = []  # список вложенных секций (5.1)
        self.__sub_elements = []  # список элементов: p, image, poem и т.п. (5.2)

    def get_title(self):
        if not self.__title:
            self.__title = Title()
        return self.__title

    title = property(get_title)

    def get_image(self):
        if not self.__image:
            self.__image = Image()
        return self.__image

    image = property(get_image)

    def get_annotation(self):
        if not self.__annotation:
            self.__annotation = Annotation()
        return self.__annotation

    annotation = property(get_annotation)

    def append_sub_section(self, s=None):
        if s:
            self.__sub_sections.append(s)
        else:
            s = SectionItem()
            self.__sub_sections.append(s)
            return s

    def append_paragraph(self, p=None):
        if p:
            self.__sub_elements.append(p)
        else:
            p = Paragraph()
            self.__sub_elements.append(p)
            return p

    def append_image(self, im):
        # TODO: автоматизировать: сразу добавлять в binary, если im не указан
        self.__sub_elements.append(im)

    def append_poem(self, p=None):
        if p:
            self.__sub_elements.append(p)
        else:
            p = Poem()
            self.__sub_elements.append(p)
            return p

    def append_subtitle(self, s=None):
        if s:
            self.__sub_elements.append(s)
        else:
            s = Subtitle()
            self.__sub_elements.append(s)
            return s

    def append_cite(self, c=None):
        if c:
            self.__sub_elements.append(c)
        else:
            c = Cite()
            self.__sub_elements.append(c)
            return c

    def append_empty_line(self):
        self.__sub_elements.append(Empty_Line())

    def append_source_text(self, st=None):
        if st:
            self.__sub_elements.append(st)
        else:
            st = SourceText()
            self.__sub_elements.append(st)
            return st

    # # TODO: 2.1
    # def append_table(self, t=None):
    #     if t:
    #         self.__sub_elements.append(t)
    #     else:
    #         t = Table()
    #         self.__sub_elements.append(t)
    #         return t

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


class Section:
    """"""

    # TODO: доделать

    def __init__(self):
        self.__list = []

    def append(self, s=None):
        if s:
            self.__list.append(s)
        else:
            s = SectionItem()
            self.__list.append(s)
            return s

    def get_source(self):
        source = ''

        for i in self.__list:
            source += i.get_source()

        return source