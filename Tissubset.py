# Fitur .issubset()
'''
Mengembalikan nilai kebenaran apakah sebuah set merupakan subset dari set lainnya. 
Sebuah set A merupakan subset dari set B jika seluruh elemen dari set A merupakan bagian dari set B.
'''
print(">>> Fitur .issubset()")
parcel_A = {'Anggur', 'Apel'}
parcel_B = {'Durian','Semangka','Apel'}
parcel_C = {'Anggur', 'Kiwi', 'Apel', 'Jeruk', 'Melon'}
parcel_A_dalam_C = parcel_A.issubset(parcel_C)
parcel_B_dalam_C = parcel_B.issubset(parcel_C)
print(parcel_A_dalam_C)
print(parcel_B_dalam_C)