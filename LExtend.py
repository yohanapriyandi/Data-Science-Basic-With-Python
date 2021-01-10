'''
List manipulation
- extend() -> Mnggabungkan du buah list seperti penggunaan operator '+'
'''

print(">>> Fitur .extend()")
list_menu = ['Gado-gado','Ayam Goreng','Rendang']
list_minuman = ['Es teh','Es Jeruk','Es Campur']
list_menu.extend(list_minuman)
print(list_menu)