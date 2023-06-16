#mengimpor modul calendar
import calendar


#menginput tahun dan bulan

yy = int(input("masukkan tahun:"))
mm = int(input("masukkan bulan:"))


#menampilkan kalender bulanan
print(calendar.month(yy, mm))