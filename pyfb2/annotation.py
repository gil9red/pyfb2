from pyfb2.cite import Cite
from pyfb2.empty_line import Empty_Line
from pyfb2.paragraph import Paragraph
from pyfb2.poem import Poem
from pyfb2.subtitle import Subtitle

__author__ = 'ipetrash'


class Annotation:
    """"""

    # Описание
    # Аннотация, т.е. краткое описание книги, служащее чтобы составить
    # приблизительное мнение о ней. Может содержать или описание сюжета, не
    # мешающее прочтению книги, т.е. не раскрывающее интриги книги, или небольшую рецензию.
    # Используется в библиотеках и отображается как на странице самой книги, так и
    # в некоторых списках (например списке новинок).
    # По этой причине не рекомендуется писать аннотации больше чем на два-три
    # коротких абзаца (и уж никак не два экрана текста).
    # Также не следует помещать в аннотацию биографию автора - для этого в
    # библиотеках существует страница автора.
    # Может также применяться в секции (<section>), например, как аннотация к
    # отдельному произведению к рамках сборника (хотя сборники лучше обормлять
    # как отдельные произведения), или как аннотации к главе, как развернутые
    # аннотации, присутствовавшие к бумажном издании в рамках книги.
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
    # <title-info> (опционально);
    # <src-title-info> (опционально) с версии 2.1;
    # <section> (опционально).
    #
    # Пример использования
    # <annotation>
    # <p>?Смерть или слава?, ?Черная эстафета?. И теперь наконец - ?Наследие исполинов?!</p>
    # <p>Случайная находка, сделанная землянами в космосе? Непонятный артефакт давно исчезнувшей цивилизации?
    # Или все-таки - генератор нуль-тоннелей, ведущих, согласно легенде, в другую галактику - к сокровищу,
    # открывающему власть над Вселенной?!</p>
    # <p>Чтобы понять - надо ДОБРАТЬСЯ!</p>
    # <p>Охота начинается. Люди и ?чужие? вступают в гонку Победитель ПОЛУЧИТ ВСЕ!</p>
    # <p>Читайте ?Наследие исполинов? - первую книгу нового цикла Владимира Васильева ?Война за мобильность?!</p>
    # </annotation>

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

    def append_subtitle(self, s=None):
        if s:
            self.__list.append(s)
        else:
            s = Subtitle()
            self.__list.append(s)
            return s

    def append_empty_line(self):
        self.__list.append(Empty_Line())

    # TODO: 2.1
    # def append_table(self, t=None):
    #     if t:
    #         self.__list.append(t)
    #     else:
    #         t = Table()
    #         self.__list.append(t)
    #         return t

    def get_source(self):
        if not self.__list:
            raise NameError('Нет содержимого тэга annotation.')

        source = '<annotation'
        if self.id:
            source += ' id="{}"'.format(self.id)

        if self.lang:
            source += ' xml:lang="{}"'.format(self.lang)
        source += '>'

        for i in self.__list:
            source += i.get_source()

        source += '</annotation>'
        return source