#menginput angka
angka = int(input("menampilkan tabel perkaliian dari: "))


#menghitung 10 kali dari kisaran 1 sampai 10
for i in range(1, angka + 1):
    #menampikan tabel perkalian
    print(angka, 'x', i, '=', angka * i)