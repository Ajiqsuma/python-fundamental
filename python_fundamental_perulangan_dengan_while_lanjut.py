"""
program perulangan baca buku dengan while sampai paham
"""
book_count = 10
print('Ibu berkata,"Baca semua bukumu sampai paham')
read_count = 0

understood_count = 0
print(f'jumlah buku yang sudah dibaca dan dipahami {understood_count}')

while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f"BUku ke {understood_count} belum paham")
    else:
        understood_count = understood_count + 1
        print(f"Buku ke {understood_count} sudah di baca dan dipahami")

print(f'jumlah buku yang sudah dibaca dan dipahami {understood_count}')
if understood_count == book_count:
    print('"Bu, Semua buku sudah dibaca dan dipahami')
else:
    print(f'"Bu tidak semua buku bisa dipahami, '
          f'Budi hanya bisa memahami {understood_count} buku ')
