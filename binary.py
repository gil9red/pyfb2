from image import Image

__author__ = 'ipetrash'


""""""


class BinaryItem:
    """"""

    # Не содержит подчиненных элементов.
    # Должен содержать текст, представляющий собой двоичные данные,
    # кодированные методом base64

    # Здесь находятся присоединенные двоичные данные. На данный момент это только изображения,
    # и расширение данного списка не планируется.
    # В файле может содержаться произвольное количество (несколько, один, вовсе отсутсвует)
    # элементов <binary>

    # Атрибуты
    # content-type (обязателен) - MIME-тип данных (картинки). На данный момент
    # поддерживются "image/jpeg" и "image/png".
    # id (обязателен) - Идентификатор ("имя файла", а точнее якорь) для ссылок
    # на данные (картинку).

    # Пример использования
    # <binary id="cover.jpg" content-type="image/jpeg">
    # AQMAEAMDBgkAAA/tAAAe7gAANHz/2wCEAAgGBgYGBggGBggMCAcIDA4KCAgKDhANDQ4NDRAR
    # DA4NDQ4MEQ8SExQTEg8YGBoaGBgjIiIiIycnJycnJycnJycBCQgICQoJCwkJCw4LDQsOEQ4O
    # ...
    # h9x8OJ/B/c+gfbXM/wDQ/qcPZ9HHjqaPi17zZ4+6deEYNxtP+H1v8Opsec//2Q==
    # </binary>

    def __init__(self):
        self.id = None
        self.content_type = None
        self.data = None

        # Ссылка на объект Image, связанный с данными бинарными данными
        self.image = None

    def get_source(self):
        # TODO: проверять значения атрибутов

        source = '<binary id="{}" content-type="{}">'.format(self.id, self.content_type)
        source += self.data
        source += '</binary>'
        return source


class Binary:
    """"""

    # TODO: доделать

    def __init__(self):
        self.__list = []

    def append(self, id_bin, content_type_bin, data_bin):
        bin = BinaryItem()
        bin.id = id_bin
        bin.content_type = content_type_bin
        bin.data = data_bin

        self.__list.append(bin)
        return bin

    def append_image(self, im, content_type=None):
        # Если не указан, определять вручную
        if not content_type:
            content_type = im.get_content_type()

        # bin_id = 'im_{}'.format(len(self.__list))
        if not im.href:
            im.href = 'im_{}'.format(len(self.__list))

        bin_id = im.href

        # TODO: проверять bin_id

        bin = self.append(bin_id, content_type, im.get_base64_source())
        if bin.image:
            print('У объекта binary={}, уже есть связанный с ним '
                  'элемент image={}.'.format(bin, bin.image))
        bin.image = im
        return bin

    def get_source(self):
        source = ''
        for b in self.__list:
            source += b.get_source()

        return source