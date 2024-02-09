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

print('\n clear')
daftar_buku.clear()
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen pertama')
daftar_buku = ['Seven Habits','How Influencer people','First Thing First','4DX']
daftar_buku[0] = 'eigth Habits'
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke-2')
buku = daftar_buku.pop(1)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil')
print(buku)

print('\nPop')
daftar_buku.pop()
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop -2')
daftar_buku = ['Seven Habits','How Influencer people','First Thing First','4DX']
daftar_buku.pop(-2)# menghapus elemen kedua dari terakhir
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del')
daftar_buku = ['Seven Habits','How Influencer people','First Thing First','4DX']
del daftar_buku[0]
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nperintah del dengan list comperhensif')
daftar_buku = ['Seven Habits','How Influencer people','First Thing First','4DX']
del daftar_buku[:]
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comperhensif start')
daftar_buku = ['Seven Habits','How Influencer people','First Thing First','4DX']
del daftar_buku[0:1]#start:end
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comperhensif start step')
daftar_buku = ['Seven Habits','How Influencer people','First Thing First','4DX']
del daftar_buku[0::2]#start:end:step
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comperhensif start')
daftar_buku = ['Seven Habits','How Influencer people','First Thing First','4DX']
del daftar_buku[0:1]#start:end
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

