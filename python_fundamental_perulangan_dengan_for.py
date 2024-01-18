"""
sintaksis perulangan dengan for
"""
# perulangan dengan for

jumlah_buku = 10
print('Ibu berkata,"Baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca = 0
print(f'jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')

print("dengan for")
for jumlah_buku_yang_sudah_dibaca in range(1, jumlah_buku +1):
    print(f'buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca ')

print(f'jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')

#tanpa for
print("tanpa for")
print("ketik manual")
print("membaca buku yang ke 1")
print("membaca buku yang ke 2")
print("membaca buku yang ke 3")
print("membaca buku yang ke 4")
print("membaca buku yang ke 5")
print("membaca buku yang ke 6")
print("membaca buku yang ke 7")

