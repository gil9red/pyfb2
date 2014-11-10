import fb2

__author__ = 'ipetrash'

# TODO: xml:lang = http://htmlbook.ru/html/value/lang

if __name__ == '__main__':
    book = fb2.FB2()
    book.description.title_info.book_title.text = "Мое произведение"
    book.description.title_info.book_title.lang = "ru"
    book.description.title_info.lang.value = "ru"
    print(book.get_source())