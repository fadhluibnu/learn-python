#game sederhana saling serang
#ada hero1 dan hero 2
#hero 1 dan 2 punya (nama, health, attack, deffence)
#hero 1 menyerang hero 2 diserang dan bertahan
#hero 2 menyerang hero 1 diserang dan bertahan
class Hero:
    def __init__(self, name, health, attackPower, armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.attackPower) 

    def diserang(self, lawan , attackPower_lawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = attackPower_lawan/self.armorNumber
        print('serangan terasa : ' + str(attack_diterima))

sniper = Hero('sniper', 100, 10, 5)
rikimaru = Hero('rikimaru', 100, 5, 10)

sniper.serang(rikimaru)
