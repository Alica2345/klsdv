class Character:


    def __init__(self, name: str, health: int, energy: int, weapon: str):


        self.name ='Max'
        self.__health = 200
        self.__energy = 100
        self.__weapon = "меч"

    def attack(self):


        if self.__energy >= 10:
            self.__energy -= 10  # Decrease energy by 10
            print(f"{self.name} attacks with {self.__weapon}. Energy left: {self.__energy}.")
        else:
            print("Недостаточно энергии для атаки")

    def take_damage(self, damage: int):

        self.__health -= damage
        if self.__health <= 0:
            print(f"Персонаж {self.name} погиб")

    def equip_weapon(self, weapon: str):

        self.__weapon = weapon  # Change the character's weapon
        print(f"{self.name} сменил оружие на {self.__weapon}.")
    def get_status(self) -> str:


        return f"Имя: {self.name}, Здоровье: {self.__health}, Энергия: {self.__energy}, Оружие: {self.__weapon}"

hero = Character()

print(hero.get_status())

hero.attack()

# Taking damage
hero.take_damage(20)

print(hero.get_status())

hero.equip_weapon("Лук")

print(hero.get_status())

for _ in range(6):
    hero.attack()