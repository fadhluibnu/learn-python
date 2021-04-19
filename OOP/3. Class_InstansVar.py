class Hero: #tamplate
    #class variabel
    jumlah = 0
    
    def __init__(self, inputName, inputHealth, inputPower, inputArmor): #self adalah hero1 
        # print('Hallo', x)
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print('Membuat Hero dengan nama' + inputName)

# hero1 = Hero(10)
hero1 = Hero('sniper', 100, 10, 4)
print(Hero.jumlah)
hero2 = Hero('mirana', 100, 15, 1)
print(Hero.jumlah)
hero3 = Hero('ucup', 1000, 100, 0)
print(Hero.jumlah)

#variable statik adalah variabelyang ada di dalam (Class)
# print(hero1.__dict__)
# print(hero2.__dict__)
# print(hero3.__dict__)
# print(Hero.__dict__)