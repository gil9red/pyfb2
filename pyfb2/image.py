import codecs

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
    # xlink:href - ссылка на собственно графические данные, обычно содержащиеся в
    # элементе <binary>;
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

        # Ссылка на объект BinaryItem, связанный с данным изображением
        self.binary = None

        # Одновременно может быть только один инициализирован
        self.url = None
        self.file_name = None

    def set_image_from_url(self, url):
        self.url = url

    def set_image_from_file(self, file_name):
        self.file_name = file_name

    def get_content_type(self):
        path = None

        if self.url:
            path = self.url
        elif self.file_name:
            path = self.file_name
        else:
            raise NameError('Не указан url или путь к файлу изображения.')

        import os

        # Попытаемся определить content_type по суффиксу пути к картинке
        suffix = os.path.splitext(path)[1][1:]

        if suffix == 'jpeg':
            suffix = 'jpg'

        if suffix != "png" and suffix != "jpg":
            raise NameError('Content-type может быть или png, или jpg: suffix={}'.format(suffix))

        return 'image/' + suffix

    def get_base64_source(self):
        """Функция возвращает base64 изображения."""

        import base64

        im_source = None

        if self.url:
            from urllib.request import urlopen

            with urlopen(self.url) as f:
                im_source = f.read()

        elif self.file_name:
            with codecs.open(self.file_name, 'rb') as f:
                im_source = f.read()
        else:
            raise NameError('Не указан url или путь к файлу изображения.')

        return base64.b64encode(im_source).decode("utf-8")

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