'''
Method/fungsi untuk menghilangkan spasi di awal dan/ atau di akhir
- .strip() -> Menghilangkan kelebihan spasi pada awal dan akhir string.
- lstrip() -> Menghilangkan kelebihan spasi pada awal string.
- rstrip() -> Menghilangkan kelebihan spasi pada akhir string.
'''
print('>>> .strip')
stringspasi1 = '   Halo, ini adalah contoh menghilangkan spasi di awal dan diakhir   '
result1 = stringspasi1.strip()
print(result1)
print('>>> .lstrip')
stringspasi2 = '   Halo, ini adalah contoh menghilangkan spasi di awal dan diakhir   '
result2 = stringspasi2.lstrip()
print(result2)
print('>>> .rstrip')
stringspasi3 = '   Halo, ini adalah contoh menghilangkan spasi di awal dan diakhir   '
result3 = stringspasi3.rstrip()
print(result3)