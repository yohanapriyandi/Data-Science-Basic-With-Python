'''
Pemecahan, Penggabungan, dan Penggantian String
ada bagian ini, aku akan mempelajari bagaimana cara memecah suatu string dengan kondisi tertentu 
sehingga menghasilkan list of string. Kemudian, akan dipelajari bagaimana cara menggabungkan 
beberapa list of string menjadi string saja. Akhirnya, 
aku akan mengganti sub-string tertentu dengan sub-string lainnya sehingga merubah string awalnya.
'''
print(">>> Fitur .split()")
bilangan = "ani dan budi dan wati dan johan"
karakter = bilangan.split('dan')
print(karakter)
kata = bilangan.split()
print(kata)
print(">>> Fitur .join()")
pemisah = " dan "
karakter = ["Ricky", "Peter", "Jordan"]
kalimat = pemisah.join(karakter)
print(kalimat)
kalimat = "  ".join(karakter)
print(kalimat)
print(">>> Fitur .replace()")
kalimat = "apel malang apel yang paling segar, apel sehat, apel nikmat"
change = kalimat.replace('apel', 'zaitun')
print(change)
