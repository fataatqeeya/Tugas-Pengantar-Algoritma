from matrix import Matrix

data_kelompok = """
2 3 1 5 3
1 2 2 1 2
3 0 2 6 1
4 2 1 2 2
2 1 3 3 3
5 4 4 7 4
3 3 2 1 5
"""

m_data = Matrix(data_kelompok)
hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
anggota = ["fata", "atha", "ghafthan", "akmal", "El"]

print("--- Total Jam Belajar per Hari ---")
for i in range(1, 8):
    print(f"{hari[i-1]}: {m_data.row_sum(i)} jam")

print("\n--- Total Jam Belajar per Anggota ---")
for i in range(1, len(anggota) + 1):
    print(f"{anggota[i-1]}: {m_data.column_sum(i)} jam")