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
        self.list = []

    def append(self, id_bin, content_type_bin, data_bin):
        bin = BinaryItem()
        bin.id = id_bin
        bin.content_type = content_type_bin
        bin.data = data_bin

        self.list.append(bin)

    def get_source(self):
        source = ''
        for b in self.list:
            source += b.get_source()

        return source