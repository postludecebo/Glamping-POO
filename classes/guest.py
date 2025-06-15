from datetime import datetime
from classes.person import Person

class Guest(Person):
    def __init__(self, person, birthDate, originCountry, foodPreferences):
        super().__init__(person.name, person.phone, person.email, person.identification)
        self.__birthDate = None
        self.__originCountry = None
        self.__foodPreferences = None

        self.birthDate = birthDate
        self.originCountry = originCountry
        self.foodPreferences = foodPreferences

    @property
    def birthDate(self):
        return self.__birthDate
    
    @birthDate.setter
    def birthDate(self, newBirthDate):
        try:
            self.__birthDate = datetime.strptime(newBirthDate, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Birth Date must be in YYYY-MM-DD format.")

    @property
    def originCountry(self):
        return self.__originCountry
    
    @originCountry.setter
    def originCountry(self, newOriginCountry):
        if not newOriginCountry:
            raise ValueError("Origin country cannot be empty.")
        self.__originCountry = newOriginCountry
    
    @property
    def foodPreferences(self):
        return self.__foodPreferences
    
    @foodPreferences.setter
    def foodPreferences(self, newFoodPreferences):
        self.__foodPreferences = newFoodPreferences if newFoodPreferences else "None"

    def estimate_age(self):
        today = datetime.today().date()
        age = today.year - self.birthDate.year 
        if (today.month, today.day) < (self.birthDate.month, self.birthDate.day):
            age -= 1
        return f"The age of {self.name} is: {age}"

    def show_info(self):
        return (
            f"{super().showInfo()}\n"
            f"Birth Date: {self.birthDate}\n"
            f"Origin Country: {self.originCountry}\n"
            f"Food Preferences: {self.foodPreferences}"
        )
