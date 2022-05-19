from itertools import chain

import xlrd

from .viewport import Viewport


class Spreadsheet:

    viewport = Viewport('A1:H42')

    def __init__(self, sheet, viewport=None):
        self.sheet = sheet

        if viewport:
            self.viewport = viewport

    @classmethod
    def from_xls(cls, file_contents, viewport=None):
        book = xlrd.open_workbook(
            file_contents=file_contents, formatting_info=True)
        sheet = book.sheet_by_index(0)

        return cls(sheet, viewport)

    @property
    def data(self):
        return [[self.sheet.cell_value(i, j) for i in self.viewport.row_indexes] for j in self.viewport.col_indexes]

    def __iter__(self):
        return chain(self.data)

    def __str__(self):

        return '\n'.join(','.join(map(str, row)) for row in zip(*self))
