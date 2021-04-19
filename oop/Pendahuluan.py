# OOP (objek orientasi programminig)
# strukral = prosedural programmig yaitu di eksekusi secara urutan
# objek - oriented programming yaitu menggunakan tamplate ( class ), kenapa harus pakai objek karea agar mereka ( objek ) bisa saling berinteraksi

#contoh oop sederhana 
class Hero: #tamplate
    pass

hero1 = Hero() #object
hero2 = Hero()
hero3 = Hero()

hero1.name = 'sniper'
hero1.health = 100

hero2.name = 'sven'
hero2.health = 200

hero3.name = 'ucup'
hero3.health = 1000

print(hero1)
print(hero1.__dict__)
print(hero1.name)