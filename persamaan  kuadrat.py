# menyelesaikan persamaan kuadrat

# mengimpor modul cmath
import cmath

# mengimput angka
a = int(input('tulis a: '))
b = int(input('tulis b: '))
c = int(input('tulis c: '))

# menghitung diskriminan
d = (b**2) - (4*a*c)

# menghitunng x1 dan x2
x1 = (-b-cmath.sqrt(d))/(2*a)
x2 = (-b+cmath.sqrt(d))/(2*a)

#menapilkan hasil x1 dan x2
print('hasill persamaan kuadrat adalah {0} dan {1}'.format(x1,x2))