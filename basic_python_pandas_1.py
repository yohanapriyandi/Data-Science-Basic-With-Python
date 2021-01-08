import pandas as pd

csv_data = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/shopping_data.csv")

'''
Untuk meminimalisir hal tersebut dan memfilter hanya data numerical saja, digunakan  exclude=[‘O’], 
dimana fungsi itu akan mengabaikan data yang non-numerical untuk diproses.
apabila menggunakan exclude=['All'], maka semua nilai akan ditampilkan termasuk nilai NaN
'''
print(csv_data.describe(exclude=['O']))