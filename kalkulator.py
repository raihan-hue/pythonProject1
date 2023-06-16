print("## progeram kalkulator ##")
print("=========================")
print()

print('1. penjumlahan')
print('2. pengurangan')
print('3. perkalian')
print('4. pembagian')
print('5. modulus')
print('6. pangkat')
print('7. pembagian bulat')

Pilihan = int(input('silahkan input pilihan operasi:'))
num1 = int(input('angka pertama:'))
num2 = int(input('angka kedua:'))
print()

if Pilihan == 1:
  print('hasil dari',num1,'+',num2,'=',round(num1+num2,2))
if Pilihan == 2:
  print('hasil dari',num1,'-',num2,'=',round(num1-num2,2))
if Pilihan == 3:
  print('hasil dari',num1,'*',num2,'=',round(num1*num2,2))
if Pilihan == 4:
  print('hasil dari',num1,'/',num2,'=',round(num1/num2,2))
if Pilihan == 5:
  print('hasil dari',num1,'%',num2,'=',round(num1%num2,2))
if Pilihan == 6:
  print('hasil dari',num1,'**',num2,'=',round(num1**num2,2))
if Pilihan == 7:
  print('hasil dari',num1,'//',num2,'=',round(num1//num2,2))