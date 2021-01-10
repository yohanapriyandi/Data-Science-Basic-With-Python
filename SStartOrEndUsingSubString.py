'''
Menentukan String Apakah Diawali/Diakhiri oleh Sub-string
Pada bagian ini, aku akan mempelajari 
bagaimana menentukan apakah suatu string diawali atau diakhiri dengan
suatu substring (teks) tertentu.
startswith() -> Mengembalikan nilai kebenaran True ketika sebuah teks (string) diawali dengan sebuah teks lainnya.
endswith() -> Mengembalikan nilai kebenaran True ketika sebuah teks (string) diakhiri dengan sebuah teks lainnya.
'''
print(">>> Fitur .startswith()")
teks = "Apel malang adalah apel termanis dibanding apel-apel lainnya"
print(teks.startswith("Apel"))
print(teks.startswith("apel"))
print(">>> Fitur .endswith()")
print(teks.endswith("lainnya"))
print(teks.endswith("apel"))
