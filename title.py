__author__ = 'ipetrash'


""""""


from empty_line import Empty_Line


class Title:
    """"""

    # Описание
    # Название книги, главы, стихотворения
    #
    # Атрибуты
    # xml:lang (опциональный) - язык.
    #
    # Подчиненные элементы
    # Может содержать произвольный набор (в произвольном количестве) из следующих элементов:
    # <p>;
    # <empty-line>.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <body> (опциональный);
    # <section> (опциональный);
    # <poem> (опциональный);
    # <stanza> (опциональный).

    # TODO: доделать

    def __init__(self):
        self.lang = None

        # Cписок может содержать параграфы (<p>) и пустые строки (<empty-line>)
        self.row_text = []

    def append_paragraph(self, p):
        self.row_text.append(p)

    def append_empty_line(self):
        self.row_text.append(Empty_Line())

    def get_source(self):
        source = '<title'
        if self.lang:
            source += ' xml:lang="{}"'.format(self.lang)
        source += '>'

        for r in self.row_text:
            source += r.get_source()

        source += '</title>'
        return source