#set / himpunan
# cara pertama
superhero = {'wiro sableng',
             'si buta',
             'saras 008',
             'gundala',
             'gatotkaca'}

superhero.add('mak lampir')
superhero.add('gundala')
print(superhero)

#cara kedua
superhero2 = set()
superhero2.add('wiro sableng')
superhero2.add('gundala')
superhero2.add('saras 008')
superhero2.add(212)

#print(sorted(superhero2))
print(superhero2)

gajil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7}

print(gajil.union(genap)) #union untuk menambahkan
print(gajil.intersection(prima))
