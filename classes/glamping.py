from classes import reservation
from classes import employee
from classes import hosting
from classes import guest
from classes import additionalservice

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
    def additionalService(self, newAdditionalService):
        if isinstance(newAdditionalService, additionalservice):
            self.__additionalServices.append(newAdditionalService)
        else:
            raise ValueError(f"The additional service {newAdditionalService} is not a valid additional service, must be a AdditionalService Class Object.")
        
    # Métodos de glamping


    def addHostings(self, newHosting):
        if isinstance(newHosting, hosting):
            self.__hostings.append(newHosting)
        else:
            raise ValueError(f"The hosting {newHosting} is not a valid hosting, must be a Hosting Class Object.")
    
    def registerGuests(self, newGuest):
        if isinstance(newGuest, guest):
            self.__guests.append(newGuest)
        else:
            raise ValueError(f"The guest {newGuest} is not a valid guest, must be a Guest Class Object.")
        
    def hireEmployees(self, newEmployee):
        if isinstance(newEmployee, employee):
            self.__employees.append(newEmployee)
        else:
            raise ValueError(f"The employeee {newEmployee} is not a valid employee, must be a Employee Class Object")
    
    def createReservation(self, guestId, hostingNum, checkIn, checkOut):
        guest = next((g for g in self.__guests if g.id == guestId), None)
        hosting = next((h for h in self.__hostings if h.number == hostingNum), None)

        if guest and hosting:
            new_reservation = reservation(guest, hosting, checkIn, checkOut)
            self.__reservations.append(new_reservation)
        else:
            raise ValueError("Invalid Guest ID or Hosting Number.")
        
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


    


