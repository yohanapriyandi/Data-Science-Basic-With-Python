'''
Menentukan Posisi dan Jumlah Sub-string pada String
Pada bagian ini, aku akan mempelajari bagaimana cara menentukan 
posisi awal suatu sub-string dan jumlah kemunculan sub-string tersebut pada suatu string.
Agar lebih memahami bagaimana penerapannya pada Python.
find() -> Mengembalikan posisi dari sebuah teks (sub-string) lainnya dalam sebuah string.
count() -> Menghitung jumlah kemunculan sebuah teks (string) lainnya dalam suatu string (string yang dicari bersifat case sensitive).
'''
print(">>> Fitur .find()")
teks = "Apel malang adalah apel termanis dibanding apel-apel lainnya"
# Fitur .find()
print(teks.find("Apel"))
print(teks.find("malang"))
print(">>> Fitur .count()")
print(teks.count('apel'))