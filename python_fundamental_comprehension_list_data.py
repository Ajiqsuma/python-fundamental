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

print('\nMembuat list baru ')
daftar_buku = ['1 Seven Habits','2 How Influencer people','3 First Thing First','4 4DX']
daftar_buku_baru = daftar_buku[:]
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
del daftar_buku [:]
for i in range (0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension  ganjil ')
daftar_buku = ['1 Seven Habits','2 How Influencer people','3 First Thing First','4 4DX']
daftar_buku_baru = daftar_buku[0::2]
for i in range (0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])


print('\nMembuat list baru dengan comprehension  genap ')
daftar_buku = ['1 Seven Habits','2 How Influencer people','3 First Thing First','4 4DX']
daftar_buku_baru = daftar_buku[1::2]
for i in range (0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])


print('\nMembuat list baru dengan comprehension  ')
daftar_buku = ['1 Seven Habits','2 How Influencer people','3 First Thing First','4 4DX']
print( daftar_buku[1::2])


