# Fitur .difference()
'''
Mengembalikan sebuah set yang berisikan difference dari dua set lainnya. 
Difference dari sebuah set A berdasarkan set B adalah 
setiap elemen yang terdapat di set A tetapi tidak terdapat di set B.
'''
print(">>> Fitur .difference()")
parcel_A = {'Anggur', 'Kiwi', 'Apel', 'Jeruk', 'Melon'}
parcel_B = {'Apel', 'Jeruk', 'Semangka', 'Durian', 'Tomat'}
parcel_C = parcel_A.difference(parcel_B)
print(parcel_C)