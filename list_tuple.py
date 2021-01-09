# Belajar mengakses list dan tuple, dimana index dimulai dari 0
bulan_pembelian = ('Januari', 'Februari','Maret','April','Mei','Juni','Juli','Agustud','September','Oktober','November','Desember')
print(bulan_pembelian[0])
print(bulan_pembelian[5])

print("====================================================================================================================")

# Belajar mengakses list dan tuple, apabila ungin mengakses dari belakang gunakan nilai - (negatif)

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
# menggabungkan  2 atau lebih list/tuple
print("====================================================================================================================")
list_makanan = ['Gado-gado','Ayam Goreng','Rendang']
list_minuman = ['Es teh','Es Jeruk','Es Campur']
list_menu = list_makanan + list_minuman
print(list_menu)

print("====================================================================================================================")
'''
List manipulation
Untuk memanipulasi data list kita bisa menggunakan fungsi yang sudah tersedia pada python
yang tediri dari
- append() -> menambahkan data
- clear() -> menghapus seluruh element dalam sebuah list
- copy() -> Mengemablikan kopi dar setiap elemen dalam sebuah list
- count() -> Mengembalikan jumlah kemunculan suatu elemen dalam sebuah list
- extend() -> Mnggabungkan du buah list seperti penggunaan operator '+'
'''
#append()
list_makanan.append('Ketoprak')
print(list_makanan)
print("====================================================================================================================")
# clear()
list_makanan.clear()
print(list_makanan)
print("====================================================================================================================")
# copy()
list_makanan1 = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_makanan2 = list_makanan1.copy()
list_makanan3 = list_makanan1
list_makanan2.append('Opor')
list_makanan3.append('Ketoprak')
print(list_makanan2)
print("====================================================================================================================")
# count
list_score = ['Budi', 'Sud', 'Budi', 'Budi', 'Budi', 'Sud', 'Sud', 'Budi', 'Budi','Budi']
score_budi = list_score.count('Budi')
score_sud = list_score.count('Sud')
print(score_budi)
print(score_sud)
print("====================================================================================================================")
#extend()
list_menu = ['Gado-gado','Ayam Goreng','Rendang']
list_menu.extend(list_minuman)
print(list_menu)
print("====================================================================================================================")
'''
List Manipulation – Part 2
Selanjutnya aku akan mempelajari fitur 
- index() -> Mengembalikan indeks dari elemen pertama yang ditemukan dari awal sebuah list
- insert() -> Menyisipkan elemen pada indeks yang dispesifikasikan
- pop() -> Menghilangkan elemen pada posisi tertentu
- remove() -> Menghilangkan elemen dengan nilai tertentu
- reverse() -> Membalik urutan elemen dari sebuah list
- sort() -> Mengurutkan elemen pada sebuah list, secara default dengan urutan dari kecil ke besar (ascending).
untuk melakukan manipulasi.
'''
print(">>> fitur index()")
#index
score_pertama_sud = list_score.index('Sud') + 1
print(score_pertama_sud)
print(">>> fitur insert()")
#insert
list_score.insert(3,'Sud')
print(list_score)
print(">>> fitur pop()")
#pop
list_menu.pop(1)
print(list_menu)
print(">>> fitur remove()")
#remove
list_menu.remove("Es Campur")
print(list_menu)
print(">>> fitur reverse()")
#reverse
list_menu.reverse()
print(list_menu)
print(">>> fitur sort()")
#sort
# descending default
list_menu.sort()
print(list_menu)
#with params reverse=True
list_menu.sort(reverse=True)
print(list_menu)















