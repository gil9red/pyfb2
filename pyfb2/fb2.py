import os.path

from pyfb2.image import Image
from pyfb2.stylesheet import Stylesheet
from pyfb2.description import Description
from pyfb2.body import Body
from pyfb2.binary import Binary
from xml.dom.minidom import parseString
import zipfile
from zipfile import ZipFile

__author__ = 'ipetrash'

"""Модуль для создания документов FictionBook версии 2.0 (fb2)."""


class FB2:
    """"""

    # Описание
    # Корневой элемент документа.
    #
    # Подчиненные элементы
    # Должен содержать в перечисленном порядке:
    # <stylesheet> - 0..n (любое число, опционально);
    # <description> - 1 (один, обязателен);
    # <body> - 1..n (любое число, один обязaтелен);
    # <binary> - 0..n (любое число, опционально).

    # Раздел FictionBook состоит из вложенных подразделов в указанном ниже порядке:
    # <description> - который описывает заголовок документа. Одно и только одно вхождение.
    # (фразы вроде "одно и только одно вхождение" говорят, сколько раз подряд может идти
    # данный тэг в данном месте документа)
    # <body> - описывает тело документа. Одно или более вхождений.
    # <binary> - содержит приложенные к файлу двоичные объекты - картинки и прочее.
    # Любое число вхождений.
    #
    # Иными словами, присутствуют как минимум разделы <description> с <body>, а
    # остальное - по необходимости.

    def __init__(self):
        self.stylesheet = Stylesheet()  # Любое число, опционально
        self.description = Description()  # Одно и только одно вхождение
        self.body = Body()  # Одно или более вхождений
        self.binary = Binary()  # Любое число вхождений

    def append_image(self, url=None, file_name=None):
        """Создает и возращает объекты Image, связанный с ним объектом binary"""
        im = Image()
        im.url = url
        im.file_name = file_name

        if url:
            im.href = os.path.basename(url)
        elif file_name:
            im.href = os.path.basename(file_name)

        bin = self.binary.append_image(im)
        im.binary = bin
        return im

    def get_source(self):
        source_fb2 = ''
        source_fb2 += ('<FictionBook '
                       'xmlns="http://www.gribuser.ru/xml/fictionbook/2.0" '
                       'xmlns:xlink="http://www.w3.org/1999/xlink">')
        source_fb2 += self.stylesheet.get_source()
        source_fb2 += self.description.get_source()
        source_fb2 += self.body.get_source()
        source_fb2 += self.binary.get_source()
        source_fb2 += '</FictionBook>'

        source_fb2 = parseString(source_fb2).toprettyxml(indent='  ')
        return source_fb2

    def save(self, file_name):
        with open(file_name, mode='w', encoding='utf-8') as f:
            fb2_source = self.get_source()
            f.write(fb2_source)

    def save_to_zip(self, file_name):
        self.save(file_name)

        with ZipFile(file_name + '.zip', mode="w", compression=zipfile.ZIP_DEFLATED) as f:
            f.write(file_name)