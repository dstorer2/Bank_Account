class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet(name = self.name, type = pet.type, tricks = pet.tricks, health = pet.health, energy = pet.energy, sound = pet.sound)




def ninja_info(self):
    print("Hi my name is ", self.first_name, " and I have a lot of ", self.treats)
    print("I recently purchased ", self.pet.name, "for $1,500. But it was totally worth it because ", self.pet.name, "can ", self.pet.tricks)

    def walk(self):
        print("thius is the walk method from the ninja class :-)")
        self.pet.play()


class Pet:
    def __init__(self, name, type, tricks, health, energy, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.sound = sound



    def sleep(self):
        print(self.name, "'s original energy: ", self.energy)
        self.energy += 25
        print(self.name, "'s energy after sleeping ", self.energy)


    def eat(self):
        print(self.name, "'s original  energy and health: ", self.energy, self.health)
        self.energy += 5
        self.health += 10
        print(self.name, "'s health after sleeping ", self.energy, self.energy)

    def play(self):
        self.health +=5

    def noise(self):
        print("I am ", self.name, "hear me ", self.sound)

chih = Pet("Chichi", "dog", "bark-a-lot", 0, 500, "Yip-Yip-Yip")

kaysee = Ninja("Kaysee", "Webers", "Dry Bones", "Purina", chih)

kaysee.ninja_info()
kaysee.walk()


# sleep(chih)