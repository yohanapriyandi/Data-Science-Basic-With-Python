"""
Menentukan String Apakah Diawali/Diakhiri oleh Sub-string
Pada bagian ini, aku akan mempelajari
bagaimana menentukan apakah suatu string diawali atau diakhiri dengan
suatu substring (teks) tertentu.
startswith() -> Mengembalikan nilai kebenaran True ketika sebuah teks (string) diawali dengan sebuah teks lainnya.
endswith() -> Mengembalikan nilai kebenaran True ketika sebuah teks (string) diakhiri dengan sebuah teks lainnya.
"""
print(">>> Fitur .startswith()")
txt = "Apel malang adalah apel termanis dibanding apel-apel lainnya"
print(txt.startswith("Apel"))
print(txt.startswith("apel"))
print(">>> Feature .endswith()")
print(txt.endswith("lainnya"))
print(txt.endswith("apel"))
