import datetime
from classes.person import Person

class Guest(Person):
    def __init__(self, name, phone, email, identification, birthDate, originCountry, foodPreferences):
        super().__init__(name, phone, email, identification)
        self.__birthDate = birthDate
        self.__originCountry = originCountry
        self.__foodPreferences = foodPreferences

    @property
    def birthDate(self):
        return self.__birthDate
    
    @birthDate.setter
    def birthDate(self, newBirthDate):
        self.__birthDate = newBirthDate

    @property
    def originCountry(self):
        return self.__originCountry
    
    @originCountry.setter
    def originCountry(self, newOriginCountry):
        self.__originCountry = newOriginCountry
    
    @property
    def foodPreferences(self):
        return self.__foodPreferences
    
    @foodPreferences.setter
    def foodPreferences(self, newFoodPreferences):
        self.__foodPreferences = newFoodPreferences
    
    def estimate_age(self):
        birthDate = datetime.strptime(self.birthDate, "%Y-%m-%d").date()
        today = datetime.today().date()
        age = today.year - birthDate.year 

        if (today.month, today.day) < (birthDate.month, birthDate.day):
            age -= 1
        return f"Age is: {age}"

    def show_info(self):
        return f"{super().showInfo()} \n Birth Date: {self.birthDate} \n Origin Country: {self.originCountry} \n Food Preferences: {self.foodPreferences}"

