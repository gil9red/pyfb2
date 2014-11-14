__author__ = 'ipetrash'


""""""


class PersonItem:
    """Базовый класс для элементов author и translator."""

    # Подчиненные элементы
    # Содержит в перечисленном порядке следующие элементы:
    # <first-name> - 0..1 (один, обязателен при отсутствии <nickname>, иначе опционально) - имя;
    # <middle-name> - 0..1 (один, опционально) - отчество;
    # <last-name> - 0..1 (один, обязателен при отсутствии <nickname>, иначе опционально) - фамилия;
    # <nickname> - 0..1 (один, обязателен при отсутствии <first-name> и <last-name>, иначе опционально);
    # <home-page> - 0..n (любое число, опционально);
    # <email> - 0..n (любое число, опционально);
    # <id> - 0..1 (один, опционально) с версии 2.2 - идентификатор автора, присваивается библиотекой.

    def __init__(self):
        self.first_name = None
        self.middle_name = None
        self.last_name = None
        self.nickname = None
        self.home_page = []
        self.email = []
        # TODO: 2.2 self.id = None

        self.name_tag = None

    def add_home_page(self, value):
        if value:
            if isinstance(value, list):
                self.home_page.extend(value)
            else:
                self.home_page.append(value)

    def remove_home_page(self, value):
        self.home_page.remove(value)

    def add_email(self, value):
        if value:
            if isinstance(value, list):
                self.email.extend(value)
            else:
                self.email.append(value)

    def remove_email(self, value):
        self.email.remove(value)

    def get_source(self):
        # TODO: проверять наличие элементов

        if not self.name_tag:
            raise NameError('Имя тэга (self.name_tag) не указано.')

        source = '<{}>'.format(self.name_tag)

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

        # TODO: 2.2
        # if self.id:
        #     source += '<id>{}</id>'.format(self.id)

        source += '</{}>'.format(self.name_tag)
        return source


class Person:
    """"""

    # TODO: доделать

    def __init__(self):
        self.list = []
        self.exteption_text_when_empty = None

    def append(self, person):
        self.list.append(person)

    def get_source(self):
        if not self.exteption_text_when_empty:
            raise NameError("Нет текста для исключения при пустом списке.")

        # Список авторов должен иметь как минимум один элемент
        if not self.list:
            raise NameError(self.exteption_text_when_empty)

        source = ''
        for p in self.list:
            source += p.get_source()

        return source