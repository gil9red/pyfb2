__author__ = 'ipetrash'


from genre import Genre
from author import Author
from book_title import Book_Title
from lang import Lang


class Title_Info:
    """"""


    # Описание информации о произведении (с учетом перевода, но без учета издания).


    def __init__(self):
        self.genre = [Genre()]  # <genre> - 1..n (любое число, один обязaтелен);
        self.author = [Author()]  # <author> - 1..n (любое число, один обязaтелен);
        self.book_title = [Book_Title()]  # <book-title> - 1 (один, обязателен);
        self.annotation = None  # <annotation> - 0..1 (один, опционально);
        self.keywords = None  # <keywords> - 0..1 (один, опционально);
        self.date = None  # <date> - 0..1 (один, опционально);
        self.coverpage = None  # <coverpage> - 0..1 (один, опционально);
        self.lang = Lang()  # <lang> - 1 (один, обязателен);
        self.src_lang = None  # <src-lang> - 0..1 (один, опционально);
        self.translator = []  # <translator> - 0..n (любое число, опционально);
        self.sequence = []  # <sequence> - 0..n (любое число, опционально).

    def get_source(self):
        # TODO: доделать
        source = '<title-info>'
        source += '</title-info>'
        return source