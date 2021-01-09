# Fitur .intersection()
'''
Mengembalikan sebuah set yang merupakan intersection dari dua set lainnya.
'''
print(">>> Fitur .intersection()")
parcel_A = {'Anggur', 'Kiwi', 'Apel', 'Jeruk', 'Melon'}
parcel_B = {'Apel', 'Jeruk', 'Semangka', 'Durian', 'Tomat'}
parcel_C = parcel_A.intersection(parcel_B)
print(parcel_C)

'''
dikarenakan 'Apel' dan 'Jeruk' terdapat baik pada set parcel_A dan parcel B
'''
