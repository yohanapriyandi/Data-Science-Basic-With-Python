print(">>> Belajar List dan Tuple")
bulan_pembelian = ('Januari', 'Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember')
print(bulan_pembelian[-1])
print(bulan_pembelian[-5])

#slicing list / tuple dengan menggunakan rentangan nilai index (range of index)
#Untuk menampilkan output bulan_pembelian Mei, Juni, Juli, Agustus, aku dapat menggunakan syntax di bawah untuk mengambil index 4 - 7.
print(bulan_pembelian[4:8])
#Untuk menampilkan output bulan_pembelian Januari, Februari, Maret, April, Mei aku dapat menggunakan syntax di bawah untuk mengambil index 0 - 4.
print(bulan_pembelian[:5])
#Untuk menampilkan output September, Oktober, November, Desember. Aku dapat menggunakan syntax di bawah untuk mengambil index 8 - elemen terakhir.
print(bulan_pembelian[8:])
#untuk mendapatkan output September, Oktober, November aku bisa menggunakan syntax di bawah:
print(bulan_pembelian[-4:-1])