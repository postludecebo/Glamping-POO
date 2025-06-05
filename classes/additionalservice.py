class AdditionalService:
    def __init__(self, name, description, price, duration):
        self.__name = name
        self.__description = description
        self.__price = price
        self.__duration = duration

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, newName):
        self.__name = newName

    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, newDescription):
        self.__description = newDescription

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, newPrice):
        if isinstance(newPrice, int) and newPrice >= 0:
            self.__price = newPrice
        else:
            raise ValueError("Price must be a positive number.")

    @property
    def duration(self):
        return self.__duration
    
    @duration.setter
    def duration(self, newDuration):
        if isinstance(newDuration, int) and newDuration > 0:
            self.__duration = newDuration
        else:
            raise ValueError("Duration must be a positive integer.")
    
    def showInfo(self):
        return f"""
        ADDITIONAL SERVICE 
        Name: {self.name}
        Description: {self.description}
        Price: ${self.price:.0f}
        Duration: {self.duration} hours
        """

