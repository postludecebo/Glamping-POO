from datetime import datetime
from classes.person import Person

class Employee(Person):
    def __init__(self, person, position, wage, entryDate):
        super().__init__(person.name, person.phone, person.email, person.identification)
        self.__position = position
        self.__wage = None
        self.__entryDate = None

        self.wage = wage
        self.entryDate = entryDate

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, newPosition):
        self.__position = newPosition

    @property
    def wage(self):
        return self.__wage
    
    @wage.setter
    def wage(self, new_wage):
        if isinstance(new_wage, int) and new_wage >= 0:
            self.__wage = new_wage
        else:
            raise ValueError(f"The wage of {self.name} must be a non-negative integer.")

    @property
    def entryDate(self):
        return self.__entryDate
    
    @entryDate.setter
    def entryDate(self, newEntryDate):
        try:
            self.__entryDate = datetime.strptime(newEntryDate, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Entry Date must be in YYYY-MM-DD format.")

    def estimateSeniority(self):
        today = datetime.today().date()
        seniority = today.year - self.entryDate.year 
        if (today.month, today.day) < (self.entryDate.month, self.entryDate.day):
            seniority -= 1
        return f"The seniority of {self.name} is: {seniority}"

    def showInfo(self):
        return f"{super().showInfo()}\nPosition: {self.position}\nWage: {self.wage}"
