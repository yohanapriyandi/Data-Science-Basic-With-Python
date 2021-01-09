# Fitur .issuperset()
'''
Mengembalikan nilai kebenaran apakah sebuah set merupakan superset dari set lainnya. 
Sebuah set A merupakan superset dari set B jika seluruh elemen dari set B terkandung dalam set A.
'''
print(">>> Fitur .issuperset()")
parcel_A = {'Anggur', 'Apel'}
parcel_B = {'Durian','Semangka','Apel'}
parcel_C = {'Anggur', 'Kiwi', 'Apel', 'Jeruk', 'Melon'}
parcel_C_mengandung_A = parcel_C.issuperset(parcel_A)
parcel_C_mengandung_B = parcel_C.issuperset(parcel_B)
print(parcel_C_mengandung_A)
print(parcel_C_mengandung_B)