class Item:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price


class Armor(Item):
    def __init__(self, name, size, price, armor_value):
        super().__init__(name, size, price)
        self.armor_value = armor_value

    def __str__(self):
        return f"A {self.size} {self.name}, worth {self.price} gold. Prevents {self.armor_value} damage."


class Weapon(Item):
    def __init__(self, name, size, price, attack_value):
        super().__init__(name, size, price)
        self.attack_value = attack_value

    def __str__(self):
        return f"A {self.size} {self.name}, worth {self.price} gold. Causes {self.attack_value} damage."

    # class Potion(Item):
    #     def __init__(self, name, size, price=1, stat, value =0,duration =0):
    #         super().__init__(name, size, price,duration)
    #         self.stat = stat
    #         self.value = value
    #         self.duration = duration

    # def __str__(self):
    #     description = f"A {self.name} potion, that increases your {self.stat} by {self.value} for {self.duration} rooms. Can be sold for {self.price} gold"

    #     match self.stat:
    #         case "armor":
    #             return description
    #         case "attack":
    #             return description
    #         case "health":
    #             return f"A {self.name} potion. Restores {self.value} {self.stat}. Can be sold for {self.price} gold"


class Character:
    def __init__(self, name, hitpoints):
        self.name = name
        self.hitpoints = hitpoints
        # self.dexterity = dexterity


class Hero(Character):
    def __init__(
        self, name, hitpoints, weapon=[], armor=[], backpack=[], bank_account=0
    ):
        super().__init__(name, hitpoints)
        self.weapon = weapon
        self.armor = armor
        self.backpack = backpack
        self.bank_account = bank_account

    def showBackpack(self):
        for i, item in enumerate(self.backpack):
            print(f"{i}: {item}")

    def showArmor(self):
        print(self.armor)

    def showWeapon(self):
        print(self.weapon)

    def pickUpItems(self, *items):
        for i, item in enumerate(items):
            self.backpack.append(item)
            print(f"You picked up {item}")

    def sellItems(self, *args):
        for i in args:
            item = self.backpack.pop(i)
            self.bank_account += item.price
            print(f"you sold your {item.name} for {item.price}")

        print(f"your have {self.bank_account} gold in your bank account.")


# class Encounter:

# shop // buy or sell weapon, armor or potion
# treasure // find gold, armor or weapon
# enemy: fight or flight


# health_potion = Potion()
# attack_potion =
sword_item = Weapon("mighty one-hand sword", "medium", 7, 3)
axe_item = Weapon("rusty axe", "small", 3, 1)
armor_rags_item = Armor("dirty rags", "too small", 0, 0)
armor_shoes_item = Armor("shoes", "too big", 0, 0)

hero = Hero(
    "myhero",
    12,
    weapon=axe_item,
    backpack=[axe_item, armor_rags_item],
)

hero.pickUpItems(axe_item, armor_shoes_item)
hero.showBackpack()
hero.sellItems(2)
