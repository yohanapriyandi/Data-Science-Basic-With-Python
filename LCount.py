'''
List manipulation
- count() -> Mengembalikan jumlah kemunculan suatu elemen dalam sebuah list
'''
print(">>> Fitur .count()")
list_score = ['Budi', 'Sud', 'Budi', 'Budi', 'Budi', 'Sud', 'Sud', 'Budi', 'Budi','Budi']
score_budi = list_score.count('Budi')
score_sud = list_score.count('Sud')
print(score_budi)
print(score_sud)