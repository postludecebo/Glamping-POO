class Person:
    def __init__(self, name, phone, email, identification):
        self.name = name
        self.phone = phone
        self.email = email
        self.identification = identification

class Guest(Person):
    def __init__(self, name, phone, email, identification, birthDate, originCountry, foodPreferences):
        super().__init__(name, phone, email, identification)
        self.birthDate = birthDate
        self.originCountry = originCountry
        self.foodPreferences = foodPreferences

class Employee(Person):
    def __init__(self, name, phone, email, identification, position, wage, entryDate):
        super().__init__(name, phone, email, identification)
        self.position = position
        self.wage = wage
        self.entryDate = entryDate

class Hosting:
    def __init__(self, phone, type, maxCapacity, baseNightPrice, amenities, disponibility):
        self.phone = phone
        self.type = type
        self.maxCapacity = maxCapacity
        self.baseNightPrice = baseNightPrice
        self.amenities = amenities
        self.disponibility = disponibility

class additionalService:
    def __init__(self, name, description, price, duration):
        self.name = name
        self.description = description
        self.price = price
        self.duration = duration


        