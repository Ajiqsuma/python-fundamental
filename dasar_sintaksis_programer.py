"""
semua sintaksis dasar pemrograman terdiri dari 3:
1.Sekuensial : berurutan
2.Percabangan : langkah melompat jika kondisi terpenuhi
3.perulangan : mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""
# sekuensial
print('Ibu berkata, "Pergi ke toko"')
print('Anak menjawab, "Ok apa yang harus aku lakukan di toko ?"')
print('Ibu berkata, "Beli satu botol susu"')
print("Maka anak pergi berangkat ke toko")
print("Dan mulai berbelanja")

# Percabangan
jumlah_botol_susu =173
jumlah_telur = 10
print(f"jumlah botol susu {jumlah_botol_susu} botol")
print(f"jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("maka Anak mengecek harga,ternyata uangnya cukup")
    if jumlah_telur <= 6:
        print("Anak membeli 1 botol susu")
    else:
        print("Anak membeli 1 botol susu ")
        print("dan 6 butir telur")
else:
    print("Anak tidak jadi membeli satu botol")

print("Anak pulang kerumah")
print("menyampaikan belanjaan ke Ibu")
