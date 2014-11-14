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
        # TODO: добавить подчиненные элементы

    def get_source(self):
        # TODO: доделать
        source = '<section'
        if self.id:
            source += ' id="{}"'.format(self.id)
        if self.lang:
            source += ' xml:lang="{}"'.format(self.lang)
        source += '>'

        source += '</section>'
        return source