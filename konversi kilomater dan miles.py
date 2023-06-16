#memginput jarak dalam satuan kiilometet
kilometer = float(input("tuliskan jarak dalam killometer:  "))

# nillaii faktor konverso
faktor_konfersii = 0.621371

#menghitung jarak dalam satuan mil
mil = kilometer * faktor_konfersii

#menampilkan hasil konfersi
print('%0.2f kilometer sama dengan %.100f mil ' %(kilometer, mil))
