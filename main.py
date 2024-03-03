class Pet:
    def __init__(self, name, species, hunger=100, happiness=100, energy=100):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy

    def feed(self):
        self.hunger += 50
        if self.hunger > 100:
            self.hunger = 100
        self.happiness += 10
        if self.happiness > 100:
            self.happiness = 100
        self.energy -= 10
        if self.energy < 0:
            self.energy = 0

    def play(self):
        self.happiness += 50
        if self.happiness > 100:
            self.happiness = 100
        self.energy -= 10
        if self.energy < 0:
            self.energy = 0

    def sleep(self):
        self.energy += 50
        if self.energy > 100:
            self.energy = 100
        self.happiness -= 10
        if self.happiness < 0:
            self.happiness = 0

    def update_attributes_over_time(self):
        self.hunger -= 5
        self.happiness -= 5
        self.energy -= 5

        if self.hunger < 0:
            self.hunger = 0
        if self.happiness < 0:
            self.happiness = 0
        if self.energy < 0:
            self.energy = 0

    def __str__(self):
        return f"{self.name} the {self.species} is hunger: {self.hunger}, happiness: {self.happiness}, energy: {self.energy}"


class PetOwner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def adopt_pet(self, pet):
        self.pets.append(pet)

    def feed_pet(self, pet_name):
        for pet in self.pets:
            if pet.name == pet_name:
                pet.feed()
                print(f"{pet_name} has been fed.")
                return
        print(f"No pet named {pet_name} found.")

    def play_with_pet(self, pet_name):
        for pet in self.pets:
            if pet.name == pet_name:
                pet.play()
                print(f"You played with {pet_name}.")
                return
        print(f"No pet named {pet_name} found.")

    def put_pet_to_sleep(self, pet_name):
        for pet in self.pets:
            if pet.name == pet_name:
                pet.sleep()
                print(f"{pet_name} has been put to sleep.")
                return
        print(f"No pet named {pet_name} found.")

    def update_pets_over_time(self):
        for pet in self.pets:
            pet.update_attributes_over_time()

    def __str__(self):
        return f"{self.name} owns {len(self.pets)} pets."
# Create pet owner
owner = PetOwner("John")

# Adopt pets
pet1 = Pet("Fluffy", "Dog")
pet2 = Pet("Whiskers", "Cat")
owner.adopt_pet(pet1)
owner.adopt_pet(pet2)

# Interact with pets
owner.feed_pet("Fluffy")
owner.play_with_pet("Whiskers")

# Update pets over time
owner.update_pets_over_time()

# Print pet owner and pet status
print(owner)
for pet in owner.pets:
    print(pet)
