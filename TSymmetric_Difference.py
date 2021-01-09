# Fitur .symmetric_difference()
'''
Mengembalikan sebuah set yang berisikan symmetric difference dari dua set lainnya. 
Symmetric difference dari sebuah set A dan B 
adalah setiap elemen dari set A yang tidak terdapat di set B digabungkan
dengan (union) setiap elemen dari set B yang tidak terdapat di set A.
'''
print(">>> Fitur .symmetric_difference()")
parcel_A = {'Anggur', 'Apel', 'Jeruk', 'Melon'}
parcel_B = {'Apel','Jeruk','Semangka','Leci'}
parcel_C = parcel_A.symmetric_difference(parcel_B)
print(parcel_C)