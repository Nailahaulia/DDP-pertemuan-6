#Buat program untuk minta input jumlah baris dan buat
#rangkaian berikut ini
# *
# **
# ***
# ****
# Dan seterusnya sejumlah baris yang diinputkan
# Gunakan for loop dengan range

b= int(input('masukan baris'))
for i in range (1,b+1):
    print('*'*i)