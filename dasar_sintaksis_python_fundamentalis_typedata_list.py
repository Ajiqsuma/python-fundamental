""""
python fundamental dasar sintaksis type data list
"""

daftar_buku = ['Seven Habits','How Influencer people','First Thing First','4DX']
print('Tampilkan Variable daftar buku')
print(daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku :
    print(buku)

print('\nTampilkan isi daftar_buku pada index tertentu')
print (daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = ('1','Kenji volume 2','-313','3,14')
print('\nTampilkan dengan for in range,dimana type data tiap elemen berbeda')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nTampilkan daftar_buku dari awal')
daftar_buku = ['Seven Habits','How Influencer people','First Thing First','4DX']
print('\nTambahkan satu buku')
daftar_buku.append('Dunia matematik kelas 5')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])
