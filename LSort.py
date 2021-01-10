'''
List Manipulation – Part 2
- sort() -> Mengurutkan elemen pada sebuah list, secara default dengan urutan dari kecil ke besar (ascending).
'''
print(">>> fitur sort()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Bakso', 'Siomay', 'Hucap', 'Soto', 'Sate', 'Empal Gentong']
# descending default
list_menu.sort()
print(list_menu)
#with params reverse=True
list_menu.sort(reverse=True)
print(list_menu)