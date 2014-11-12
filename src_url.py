__author__ = 'ipetrash'


""""""


class Src_Url:
    """"""

    # Описание
    # Откуда взят оригинальный документ, доступный в online
    #
    # Атрибуты
    # Нет атрибутов.
    #
    # Подчиненные элементы
    # Нет дочерних элементов, содержит текст - адрес источника.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <document-info> (любое число, опциональный).
    #
    # Пример использования
    # <src-url>http://4pda.ru/mag.php</src-url>

    def __init__(self):
        self.list = []

    def append(self, url):
        # TODO: дубликат кода есть в program_used
        if isinstance(url, list):
            for p in url:
                self.append(p)
        else:
            # Добавим url, если ее нет в списке:
            if not url in self.list and url:
                self.list.append(url)
            else:
                print('Элемент "{}" уже есть в списке.'.format(url))

    def get_source(self):
        source = ''

        for u in self.list:
            source += '<src-url>{}</src-url>'.format(u)

        return source