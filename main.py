from matrix import Matrix

data_kelompok = "2 3 2 5 3\n1 2 3 1 2\n3 0 5 6 1\n4 2 5 2 2\n2 1 6 3 3\n5 4 6 7 4\n3 3 7 1 5"

m_data = Matrix(data_kelompok)
hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
anggota = ["fata", "atha", "ghafthan", "akmal", "El"]

print("--- Total Jam Belajar per Hari ---")
for i in range(1, 8):
    print(f"{hari[i-1]}: {m_data.row_sum(i)} jam")

print("\n--- Total Jam Belajar per Anggota ---")
for i in range(1, len(anggota) + 1):
    print(f"{anggota[i-1]}: {m_data.column_sum(i)} jam")
