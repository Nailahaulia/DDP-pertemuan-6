#Buat lah output dari menggunakan bahasa pemprograman python dengan : 

#secara tidak manual
jumlah = 0
string =""
for i in range(1,20,2):
    jumlah += i
    string += f"{i}"
    if i == 19 :
        string += '+'
    else : 
        string += '+'
print(f"{string} {jumlah}")

#secara manual
jumlah = 0
for i in range (1,20,2):
    jumlah += f"{i}"
    if i == 19:
print (f"1 + 3 + 5 + 7 +9 +11 +13 + 15 +17 +19 = {jumlah}")
