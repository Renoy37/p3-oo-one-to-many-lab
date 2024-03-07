class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=None):
        if pet_type in Pet.PET_TYPES:
            self.name = name
            self.pet_type = pet_type
            self.owner = owner
            Pet.all.append(self)
        else:
            raise Exception("check failed")


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all]

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("The pet must be an instance of the Pet class.")

    def get_sorted_pets(self):
        return sorted(Pet.all, key=lambda pet: pet.name)
