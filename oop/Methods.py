#contoh method adalah tombol
class Hero:
    #class varibale
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    #methods tidak mengmbalikan sebuah nilai, kalau di perograman lain disebut VOID
    #methods tampa return
    def siapa(self):
        print('namaku adalah' + self.name)

    #methods dengan argumen
    def healthUp(self, up):
        self.health += up

    #methods dengan return
    def getHealth(self):
        return self.health


hero1 = Hero('sniper', 100, 10, 5)
Hero2 = Hero('ucup', 96, 5, 10)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())