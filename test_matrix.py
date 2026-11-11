import unittest
from matrix import Matrix


class TestContohSoal(unittest.TestCase):
    def test_satu_elemen(self):
        self.assertEqual(Matrix("1").row(1), [1])

    def test_row_2x2(self):
        self.assertEqual(Matrix("1 2\n3 4").row(2), [3, 4])

    def test_row_dua_digit(self):
        self.assertEqual(Matrix("1 2\n10 20").row(2), [10, 20])

    def test_row_4_baris(self):
        self.assertEqual(Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6").row(4), [8, 7, 6])

    def test_column_3(self):
        self.assertEqual(Matrix("1 2 3\n4 5 6\n7 8 9").column(3), [3, 6, 9])

    def test_column_4(self):
        self.assertEqual(Matrix("1 2 3 4\n5 6 7 8\n9 8 7 6").column(4), [4, 8, 6])

    def test_column_angka_besar(self):
        self.assertEqual(Matrix("89 1903 3\n18 3 1\n9 4 800").column(2), [1903, 3, 4])


class TestBuatanKelompok(unittest.TestCase):
    def test_indeks_nol_dan_negatif(self):
        m = Matrix("1 2\n3 4")
        with self.assertRaises(IndexError):
            m.row(0)
        with self.assertRaises(IndexError):
            m.column(-1)

    def test_baris_kosong_di_akhir(self):
        self.assertEqual(Matrix("1 2\n3 4\n").row(2), [3, 4])

    def test_spasi_ganda(self):
        self.assertEqual(Matrix("1  2\n3  4").column(2), [2, 4])


class TestJumlah(unittest.TestCase):
    def test_row_sum(self):
        self.assertEqual(Matrix("1 2 3\n4 5 6").row_sum(2), 15)

    def test_column_sum(self):
        self.assertEqual(Matrix("1 2 3\n4 5 6").column_sum(3), 9)


if __name__ == "__main__":
    unittest.main()