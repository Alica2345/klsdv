class Character:
    def __init__(self, name, health, attack_power,weapon):
        self.name = "Max"
        self.health = 234
        self.attack_power = 40
        self.weapon = 12


class Hero(Character):


    def attack(self):
        return f"{self.name}  {self.weapon}  {self.attack_power} {self.health}"


class Enemy(Character):
    def __init__(self, name, damage):

        self.attack_power = damage
        self.damage = damage

    def attack(self):
        return f"{self.name}  {self.damage} {self.health}"


hero = Hero("Лицар", 500, "меч")
enemy = Enemy("Гоблін", 300, 20)

print(hero.attack())
print(enemy.attack())