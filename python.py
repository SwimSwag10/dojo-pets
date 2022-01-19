
class Ninja:
  # implement __init__( first_name , last_name , treats , pet_food , pet )
  def __init__(self, first_name, last_name, treats, pet_food, pet, ):
    self.first_name = first_name
    self.last_name = last_name
    self.trests = treats
    self.pet_food = pet_food
    self.pet = pet
    self.my_pet = Pet("Puppers", "big", "roll over")

  # implement the following methods:
  # walk() - walks the ninja's pet invoking the pet play() method
  def walk(self):
    self.my_pet.play()
    return self
    
  # feed() - feeds the ninja's pet invoking the pet eat() method
  def feed(self):
    self.my_pet.eat()
    return self

  # bathe() - cleans the ninja's pet invoking the pet noise() method
  def bathe(self):
    self.my_pet.noise()
    return self

class Pet:
  # implement __init__( name , type , tricks ):
  def __init__(self, name, type, tricks, ):
    self.name = name
    self.type = type
    self.tricks = tricks
    self.energy = 0
    self.health = 100
    self.sound = "bark"
  
  # implement the following methods:
  # sleep() - increases the pets energy by 25
  def sleep(self):
    self.energy += 25
    return self

  # eat() - increases the pet's energy by 5 & health by 10
  def eat(self):
    self.energy += 5
    self.health += 10
    return self

  # play() - increases the pet's health by 5
  def play(self):
    self.health += 5
    return self

  # noise() - prints out the pet's sound
  def noise(self):
    print(self.sound)
    return self

ninja = Ninja("Hikaru", "Monsanto", 6, "bones", "Puppers")

print(ninja.my_pet.energy, ninja.my_pet.health)
ninja.feed().walk().bathe()
print(f"Health: '{ninja.my_pet.health}' Energy: '{ninja.my_pet.energy}' Tricks learned: '{ninja.my_pet.tricks}' Dog type: '{ninja.my_pet.type}'")