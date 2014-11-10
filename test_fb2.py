import fb2

__author__ = 'ipetrash'

# TODO: xml:lang = http://htmlbook.ru/html/value/lang

if __name__ == '__main__':
    book = fb2.FB2()
    print(book.get_source())