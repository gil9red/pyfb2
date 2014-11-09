__author__ = 'ipetrash'


class Author:
    """Информация об авторе книги, если элемент используется в <title-info>
    или <src-title-info>; или об авторе документа, если в <document-info>."""

    # Подчиненные элементы
    # Содержит в перечисленном порядке следующие элементы:
    # <first-name> - 0..1 (один, обязателен при отсутствии <nickname>, иначе опционально) - имя;
    # <middle-name> - 0..1 (один, опционально) - отчество;
    # <last-name> - 0..1 (один, обязателен при отсутствии <nickname>, иначе опционально) - фамилия;
    # <nickname> - 0..1 (один, обязателен при отсутствии <first-name> и <last-name>, иначе опционально);
    # <home-page> - 0..n (любое число, опционально);
    # <email> - 0..n (любое число, опционально);
    # <id> - 0..1 (один, опционально) с версии 2.2 - идентификатор автора, присваивается библиотекой.
    #
    # Подчинен
    # Может содержаться в следующих элементах:
    # <title-info> 1..n (любое число, один обязателен);
    # <src-title-info> 1..n (любое число, один обязателен) с версии 2.1;
    # <document-info> 1..n (любое число, один обязателен);
    #
    # Пример использования
    # <author>
    #   <first-name>Борис</first-name>
    #   <last-name>Сергеев</last-name>
    # </author>

    def __init__(self):
        self.first_name = None
        self.middle_name = None
        self.last_name = None
        self.nickname = None
        self.home_page = []
        self.email = []
        self.id = None

    def add_home_page(self, value):
        self.home_page.append(value)

    def remove_home_page(self, value):
        self.home_page.remove(value)

    def add_email(self, value):
        self.email.append(value)

    def remove_email(self, value):
        self.email.remove(value)

    def get_source(self):
        # TODO: проверять наличие элементов
        source = '<author>'

        if self.first_name:
            source += '<first-name>{}</first-name>'.format(self.first_name)

        if self.middle_name:
            source += '<middle-name>{}</middle-name>'.format(self.middle_name)

        if self.last_name:
            source += '<last-name>{}</last-name>'.format(self.last_name)

        if self.nickname:
            source += '<nickname>{}</nickname>'.format(self.nickname)

        for hp in self.home_page:
            source += '<home-page>{}</home-page>'.format(hp)

        for e in self.email:
            source += '<email>{}</email>'.format(e)

        if self.id:
            source += '<id>{}</id>'.format(self.id)

        source += '</author>'
        return source