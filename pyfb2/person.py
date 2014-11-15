from pyfb2.email import Email
from pyfb2.first_name import First_Name
from pyfb2.home_page import Home_Page
from pyfb2.last_name import Last_Name
from pyfb2.middle_name import Middle_Name
from pyfb2.nickname import Nickname


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
        self.__first_name = None
        self.__middle_name = None
        self.__last_name = None
        self.__nickname = None
        self.home_page = Home_Page()
        self.email = Email()
        # TODO: 2.2 self.id = None

        self.name_tag = None

    def get_first_name(self):
        if not self.__first_name:
            self.__first_name = First_Name()
        return self.__first_name
    first_name = property(get_first_name)

    def get_middle_name(self):
        if not self.__middle_name:
            self.__middle_name = Middle_Name()
        return self.__middle_name
    middle_name = property(get_middle_name)

    def get_last_name(self):
        if not self.__last_name:
            self.__last_name = Last_Name()
        return self.__last_name
    last_name = property(get_last_name)

    def get_nickname(self):
        if not self.__nickname:
            self.__nickname = Nickname()
        return self.__nickname
    nickname = property(get_nickname)

    def get_source(self):
        # TODO: проверять наличие элементов

        if not self.name_tag:
            raise NameError('Имя тэга (self.name_tag) не указано.')

        source = '<{}>'.format(self.name_tag)

        if self.__first_name:
            source += self.__first_name.get_source()

        if self.__middle_name:
            source += self.__middle_name.get_source()

        if self.__last_name:
            source += self.__last_name.get_source()

        if self.__nickname:
            source += self.__nickname.get_source()

        source += self.home_page.get_source()
        source += self.email.get_source()

        # TODO: 2.2
        # if self.id:
        #     source += '<id>{}</id>'.format(self.id)

        source += '</{}>'.format(self.name_tag)
        return source


class Person:
    """"""

    # TODO: доделать

    def __init__(self):
        self._list = []
        self.exteption_text_when_empty = None

    def append(self, person):
        self._list.append(person)

    def get_source(self):
        if not self.exteption_text_when_empty:
            raise NameError("Нет текста для исключения при пустом списке.")

        # Список авторов должен иметь как минимум один элемент
        if not self._list:
            raise NameError(self.exteption_text_when_empty)

        source = ''
        for p in self._list:
            source += p.get_source()

        return source