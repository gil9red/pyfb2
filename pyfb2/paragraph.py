__author__ = 'ipetrash'

""""""


class Paragraph:
    """"""

    # Описание
    # Параграф, абзац текста.
    #
    # Атрибуты
    # id (опциональный) - Идентификатор (якорь, метка) для ссылок на данный элемент
    # style (опциональный) - стиль параграфа
    # xml:lang (опциональный) - язык.
    #
    # Подчиненные элементы
    # Содержит текст, а также произвольный набор (в произвольном количестве) из следующих элементов:
    # <strong>;
    # <emphasis>;
    # <style>;
    # <a>;
    # <strikethrough> с версии 2.1;
    # <sub> с версии 2.1;
    # <sup> с версии 2.1;
    # <code> с версии 2.1;
    # <image>;
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <section>;
    # <title>;
    # <epigraph>;
    # <cite>;
    # <annotation>;
    # <history>.
    #
    # Пример использования
    # <p>Вот абзац текста.</p>
    # <p>Еще один абзац текста.</p>

    # TODO: Доделать

    def __init__(self, text=None, id=None, style=None, lang=None):
        self.id = id
        self.style = style
        self.lang = lang

        self.text = text

    def get_source(self):
        if not self.text:
            raise NameError('Параграф <p> пуст (self.text is None).')

        source = '<p'
        if self.id:
            source += ' id="{}"'.format(self.id)

        if self.style:
            source += ' style="{}"'.format(self.style)

        if self.lang:
            source += ' xml:lang="{}"'.format(self.lang)

        source += '>'

        source += self.text

        source += '</p>'
        return source