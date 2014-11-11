__author__ = 'ipetrash'


""""""


class Image:
    """"""

    # Описание
    # Картинка, иллюстрация в тексте.
    # Определены два типа картинок: обычные (imageType) и внутри текста (inlineImageType).
    #
    # Атрибуты
    # xlink:type (опциональный)
    # xlink:href - ссылка на собственно графические данные, обычно содержащиеся в элементе <binary>;
    # alt (опциональный);
    # title (опциональный, для inline недопустимый) - подпись к картинке;
    # id (опциональный, для inline недопустимый) - для ссылок на картинку.
    #
    # Подчиненные элементы
    # Нет подчиненных элементов, обычно нет закрывающего тэга (пустой элемент).
    #
    # Подчинен
    # Может содержаться в следующих элементах: Для обычных:
    # <body>;
    # <section>.
    #
    # Для inline:
    # <coverpage>;
    # <p>;
    # <v>;
    # <subtitle>;
    # <th> (с версии 2.1);
    # <td> (с версии 2.1);
    # <text-author> (с версии 2.1).
    #
    # Пример использования
    # <p>Абзац текста до картинки.</p>
    # <image xlink:href="#picture.jpg"/>
    # <p>Абзац текста после картинки.</p>

    # TODO: доделать

    def __init__(self):
        self.type = None
        self.href = None
        self.alt = None
        self.title = None
        self.id = None

    def get_source(self):
        if not self.href:
            raise NameError('Не указана ссылка на изображение.')

        source = '<image'
        source += ' xlink:href="#{}"'.format(self.href)

        if self.type:
            source += ' xlink:type="{}"'.format(self.type)

        if self.alt:
            source += ' alt="{}"'.format(self.alt)

        if self.title:
            source += ' title="{}"'.format(self.title)

        if self.id:
            source += ' id="{}"'.format(self.id)

        source += '/>'

        return source