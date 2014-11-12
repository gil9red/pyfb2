__author__ = 'ipetrash'


""""""


class Epigraph:
    """"""

    # Описание
    # Эпиграф
    #
    # Атрибуты
    # id (опциональный) - Идентификатор (якорь, метка) для ссылок на данный элемент
    #
    # Подчиненные элементы
    # Содержит в перечисленном порядке элементы:
    # Произвольный набор (в произвольном количестве)
    # <p>;
    # <poem>;
    # <cite>;
    # <empty-line>;
    # <text-author> 0..n (любое число, опционально).
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <body>;
    # <section>;
    # <poem>.
    #
    # Пример использования
    # <epigraph>
    # <p>"The truth is the one thing that nobody will believe."</p>
    # <text-author>GEORGE BERNARD SHAW 1856-1950</text-author>
    # </epigraph>

    # TODO: доделать

    def __init__(self):
        self.id = None
        # TODO: добавить подчиненные элементы

    def get_source(self):
        source = '<epigraph'
        if self.id:
            source += ' id="{}"'.format(self.id)
        source += '>'
        source += '</epigraph>'
        return source