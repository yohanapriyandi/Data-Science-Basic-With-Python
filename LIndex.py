'''
List Manipulation – Part 2
- index() -> Mengembalikan indeks dari elemen pertama yang ditemukan dari awal sebuah list
'''

print(">>> Fitur .index()")
list_score = ['Budi','Sud','Budi','Budi','Budi','Sud','Sud']
score_pertama_sud = list_score.index('Sud') + 1
print(score_pertama_sud)