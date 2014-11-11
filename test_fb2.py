import fb2

__author__ = 'ipetrash'

# TODO: xml:lang = http://htmlbook.ru/html/value/lang
# http://www.fictionbook.org/index.php/Пример_документа_в_FB2


if __name__ == '__main__':
    book = fb2.FB2()

    title_info = book.description.title_info
    title_info.book_title.text = "Мое произведение"
    title_info.book_title.lang = "ru"
    title_info.lang.value = "ru"
    title_info.src_lang.value = "en"
    title_info.keywords.add_keywords("книга")
    title_info.keywords.add_keywords("foo")
    title_info.keywords.add_keywords("github")
    title_info.date.set_date(16, 11, 2014)
    title_info.sequence.append("Война и мир", 1)
    title_info.sequence.append("Горящий пукан школоты", 5, "ru")
    title_info.genre.append("adv_western")
    title_info.genre.append("detective", match=20)
    title_info.author.append("Ilya", "Andreevich", "Petrash", "gil9red",
                             home_page=["https://github.com/gil9red", "http://vk.com/ipetrash"],
                             email="ip1992@inbox.ru", id="777")
    title_info.author.append(first_name="Vasya", last_name="Pupkin")

    # + title_info.genre = []  # <genre> - 1..n (любое число, один обязaтелен);
    # + title_info.author = []  # <author> - 1..n (любое число, один обязaтелен);
    # + title_info.book_title = Book_Title()  # <book-title> - 1 (один, обязателен);
    # title_info.annotation = None  # <annotation> - 0..1 (один, опционально);
    # + title_info.keywords = None  # <keywords> - 0..1 (один, опционально);
    # + title_info.date = None  # <date> - 0..1 (один, опционально);
    # title_info.coverpage = None  # <coverpage> - 0..1 (один, опционально);
    # + title_info.lang = Lang()  # <lang> - 1 (один, обязателен);
    # + title_info.src_lang = None  # <src-lang> - 0..1 (один, опционально);
    # title_info.translator = []  # <translator> - 0..n (любое число, опционально);
    # + title_info.sequence = []  # <sequence> - 0..n (любое число, опционально).

    print(book.get_source())