print("kalkolator sederhana")
print("======================")

print("1.perkalian")
print("2.pembagian")
print("3.tambah")
print("4.kurang")
print("5.mudulus")
print("6.pangkat")
rint("7.pembagian bulat")
print()
if pilihan == 1:
    print('hasil dari', num1,'*', num2,'=',round(num1 * num2, 2))
elif pilihan == 2:
    print('hasil dari', num1,'/', num2,'=',round(num1 / num2, 2))
elif pilihan == 3:
    print('hasil dari', num1,'+', num2,'=',round(num1 + num2, 2))
elif pilihan == 4:
    print('hasil dari', num1,'-', num2,'=',round(num1 - num2, 2))
elif pilihan == 5:
    print('hasil dari', num1,'%', num2,'=',round(num1 % num2, 2))
elif pilihan == 6:
    print('hasil dari', num1,'**', num2,'=',round(num1 ** num2, 2))
elif pilihan == 7:
    print('hasil dari', num1,'//', num2,'=',round(num1 // num2, 2))

pilihan = int(input('input operasi : '))
num1 = int(input('angka pertama : '))
num2 = int(input('angka kedua : '))
print()
p

else:
    print("maaf pilihanmu gak tersedia")