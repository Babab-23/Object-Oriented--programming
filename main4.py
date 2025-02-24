class Dog:
    # Class variable
    species = "Canine"  # All dogs belong to the canine species
    
    def __init__(self, breed, age):
        # Instance variables
        self.breed = breed
        self.age = age

    def display_details(self):
        print(f"Species: {self.species}")
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age} years")
        print("-" * 30)

# Create objects for two different dog breeds
dog1 = Dog("Golden Retriever", 3)
dog2 = Dog("Bulldog", 5)

# Display details of each dog
dog1.display_details()
dog2.display_details()
