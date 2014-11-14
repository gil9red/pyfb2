from pyfb2.date import Date
from pyfb2.title import Title

__author__ = 'ipetrash'


""""""


class Poem:
    """"""

    # Описание
    # Стихотворение
    #
    # Атрибуты
    # id (опциональный) - Идентификатор (якорь, метка) для ссылок на данный элемент
    # xml:lang (опциональный) - язык.
    #
    # Подчиненные элементы
    # Должен содержать последовательность элементов в таком порядке:
    # <title> 0..1 (опционально) - название;
    # <epigraph> 0..n (любое число, опционально) - эпиграф;
    # <stanza> 1..n (любое число, обязательно) - стихотворные строфы;
    # <text-author> 0..n (любое число, опционально) - автор стиха;
    # <date> 0..1 (опционально) - дата написания.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <section>.
    # <cite>.
    # <epigraph>.
    # <annotation>.
    # <history>.
    #
    # Пример использования
    # <poem>
    # <stanza>
    # <v>Когда сгустится тьма вокруг</v>
    # <v>Ты словно раб предназначенья,</v>
    # <v>Начертишь кровью ровный круг,</v>
    # </stanza>
    # <stanza>
    # <v>Отбросишь жалкие сомненья.</v>
    # <v>Войдёшь в него, забыв про страх.</v>
    # <v>Тебя подхватят тьмы теченья.</v>
    # </stanza>
    # <stanza>
    # <v>Отбросишь тело, ? бренный прах.</v>
    # <v>Ты с теми, кто во тьму шагнули!</v>
    # <v>Погасли огоньки в глазах.</v>
    # </stanza>
    # <stanza>
    # <v>А где твой дух, а не в аду ли?</v>
    # </stanza>
    # <text-author>Джейнджер Скауджер Алкариот</text-author>
    # </poem>

    # TODO: доделать

    def __init__(self):
        self.id = None
        self.lang = None

        self.__title = None  # 0..1 (опционально) - название;
        self.epigraph = None  # 0..n (любое число, опционально) - эпиграф;
        self.stanza = None  # 1..n (любое число, обязательно) - стихотворные строфы;
        self.text_author = None  # 0..n (любое число, опционально) - автор стиха;
        self.__date = None  # 0..1 (опционально) - дата написания.

    def get_title(self):
        if not self.__title:
            self.__title = Title()
        return self.__title
    title = property(get_title)

    def get_date(self):
        if not self.__date:
            self.__date = Date()
        return self.__date
    date = property(get_date)

    def get_source(self):
        source = '<poem'
        if self.id:
            source += ' id="{}"'.format(self.id)

        if self.lang:
            source += ' xml:lang="{}"'.format(self.lang)
        source += '>'

        if self.__title:
            source += self.__title.get_source()

        source += self.epigraph.get_source()
        source += self.stanza.get_source()
        source += self.text_author.get_source()

        if self.__date:
            source += self.__date.get_source()

        source += '</poem>'
        return source