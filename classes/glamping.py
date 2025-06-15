from classes.reservation import Reservation
from classes.employee import Employee
from classes.hosting import Hosting
from classes.guest import Guest
from classes.additionalservice import AdditionalService

class Glamping:
    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        self.__hostings = []
        self.__guests = []
        self.__employees = []
        self.__reservations = []
        self.__additionalServices = []

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, newName):
        if isinstance(newName, str) and newName != "":
            self.__name = newName
        else:
            raise ValueError("The name of the glamping cannot be empty and must be a text.")
        
    @property
    def location(self):
        return self.__location
    
    @location.setter
    def location(self, new_location):
        self.__location = new_location
    
    @property
    def hostings(self):
        return self.__hostings[:]
    

    @property 
    def guests(self):
        return self.__guests[:]
    

    @property
    def employees(self):
        return self.__employees[:]

        
    @property
    def reservations(self):
        return self.__reservations[:]
    
        
    @property
    def additionalServices(self):
        return self.__additionalServices[:]
    
    @additionalServices.setter
    def additionalServices(self, newAdditionalService):
        if isinstance(newAdditionalService, AdditionalService):
            self.__additionalServices.append(newAdditionalService)
        else:
            raise ValueError(f"The additional service {newAdditionalService} is not a valid additional service, must be a AdditionalService Class Object.")
        
    # Métodos de glamping


    def addHostings(self, newHosting):
        if isinstance(newHosting, Hosting):
            self.__hostings.append(newHosting)
        else:
            raise ValueError(f"The hosting {newHosting} is not a valid hosting, must be a Hosting Class Object.")
    
    def registerGuests(self, newGuest):
        if isinstance(newGuest, Guest):
            self.__guests.append(newGuest)
        else:
            raise ValueError(f"The guest {newGuest} is not a valid guest, must be a Guest Class Object.")
        
    def hireEmployees(self, newEmployee):
        if isinstance(newEmployee, Employee):
            self.__employees.append(newEmployee)
        else:
            raise ValueError(f"The employeee {newEmployee} is not a valid employee, must be a Employee Class Object")


    def registerReservation(self, newReservation):
        if isinstance(newReservation, Reservation):
            self.__reservations.append(newReservation)

        
    def findAvailableHostings(self, type, checkIn, checkOut):
        return [h for h in self.__hostings if h.type == type and h.is_available(checkIn, checkOut)]
    
    def estimateCurrentOccupancy(self):
        activeReservations = [r for r in self.__reservations if r.status == "in progress"]
        return len(activeReservations) / len(self.__hostings) * 100  
 
    def listActiveReservations(self):
        return [r for r in self.__reservations if r.status in ["confirmed", "in progress"]]
    
    def generateIncomeReport(self, month, year):
        completedReservations = [
            r for r in self.__reservations if r.state == "finished" and 
            r.dateCheckOut.month == month and r.dateCheckOut.year == year
        ]
        total_income = sum(r.estimateTotalPrice() for r in completedReservations)
        return f"Total income for {month}/{year}: ${total_income:.0f}"


    


