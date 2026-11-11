>>> class Matrix:
...     def __init__(self, matrix_string):
...         lines = [line for line in matrix_string.split('\n') if line.strip()]
...         self._rows = [[int(x) for x in line.split()] for line in lines]
...
...     def _cek_indeks(self, index, batas, nama):
...         if index < 1 or index > batas:
...             raise IndexError(f"{nama} {index} di luar jangkauan (1..{batas})")
...
...     def row(self, index):
...         self._cek_indeks(index, len(self._rows), "Baris")
...         return self._rows[index - 1][:]
...
...     def column(self, index):
...         self._cek_indeks(index, len(self._rows[0]), "Kolom")
...         return [baris[index - 1] for baris in self._rows]
...
...     def row_sum(self, index):
...         return sum(self.row(index))
...
...     def column_sum(self, index):
...         return sum(self.column(index))
