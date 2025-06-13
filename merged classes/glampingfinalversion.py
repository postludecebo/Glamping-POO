from datetime import datetime 

class Person:
    def __init__(self, name, phone, email, identification):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__identification = identification
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, newName):
        if isinstance(newName, str) and newName.strip():
            self.__name = newName
        else:
            raise ValueError(f"Name has to be a valid text and cannot be empty.")
        
    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, newPhone):
        if isinstance(newPhone, int) and len(newPhone) == 10:
            self.__phone = newPhone
        else:
            raise ValueError(f"Phone has to be a valid number and has to be a 10 digits number.")

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, newEmail):
        self.__email = newEmail

    @property
    def identification(self):
        return self.__identification
    
    @identification.setter
    def identification(self, newIdentification):
        self.__identification = newIdentification
    
    def show_info(self):
        return f"INFORMATION \n Name: {self.name} \n Phone: {self.phone} \n Email: {self.email} \n Identification: {self.identification}"
                


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
        return f"{super().show_info()} \n Birth Date: {self.birthDate} \n Origin Country: {self.originCountry} \n Food Preferences: {self.foodPreferences}"


class Employee(Person):
    def __init__(self, name, phone, email, identification, position, wage, entryDate):
        super().__init__(name, phone, email, identification)
        self.__position = position
        self.__wage = wage
        self.__entryDate = entryDate

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
            raise ValueError(f"The wage of {self.name} needs to be greater than 0 and a integer number.")
        
    @property
    def entryDate(self):
        return self.__entryDate
    
    @entryDate.setter
    def entryDate(self, newEntryDate):
        try:
            self.__entryDate = datetime.strptime(newEntryDate, "%Y-%m-%d").date()  # Guarda como date
        except ValueError:
            raise ValueError("Entry Date must be in YYYY-MM-DD format.")



    def estimateSeniority(self):
        today = datetime.today().date()
        seniority = today.year - self.entryDate.year 

        if (today.month, today.day) < (self.entryDate.month, self.entryDate.day):
            seniority -= 1
        return f"The seniority of {self.name} is: {seniority}"

    
    def show_info(self):
        return f"{super().show_info()} \n Position: {self.position} \n Wage: {self.wage}"
                    
        
class Hosting:
    SEASON_MULTIPLIERS = {
        "high": 1.2,
        "mid": 1.0,
        "low": 0.85,
    }
    VALID_TYPES = {"shack", "dome", "luxury"}
    VALID_AMENITIES = {"wifi", "jacuzzi", "chimney", "pool", "air conditioner"}
    def __init__(self, phone, type, maxCapacity, baseNightPrice, amenities, disponibility, season):
        self.__phone = phone
        self.__type = None
        self.type = type
        self.__maxCapacity = maxCapacity
        self.__baseNightPrice = baseNightPrice
        self.__amenities = []
        self.amenities = amenities
        self.__disponibility = None
        self.disponibility = disponibility
        self.__season = None
        self.season = season
        
    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, newPhone):
        self.__phone = newPhone

    @property
    def type(self):
        return self.__type 
    
    @type.setter
    def type(self, new_type):
        if new_type in self.VALID_TYPES:
            self.__type = new_type
        else:
            raise ValueError(f"Type '{new_type} is not a valid option. Options: {self.VALID_TYPES}'")

    @property
    def maxCapacity(self):
        return self.__maxCapacity
    
    @maxCapacity.setter
    def maxCapacity(self, newMaxCapacity):
        self.__maxCapacity = newMaxCapacity

    @property
    def baseNightPrice(self):
        return self.__baseNightPrice
    
    @baseNightPrice.setter
    def baseNightPrice(self, newBaseNightPrice):
        self.__baseNightPrice = newBaseNightPrice
    
    @property
    def amenities(self):
        return self.__amenities
    
    @amenities.setter
    def amenities(self, new_list):
        if all(amenity in self.VALID_AMENITIES for amenity in new_list):
            self.__amenities = new_list
        else:
            raise ValueError(f"Invalid amenities. Options: {self.VALID_AMENITIES}")
        
    @property
    def disponibility(self):
        return self.__disponibility

    @disponibility.setter
    def disponibility(self, state):
        if isinstance(state, bool):
            self.__disponibility = state
        else:
            raise ValueError("Disponibility atribute can only be 'True' or 'False'")
    
    @property
    def season(self):
        return self.__season
    
    @season.setter
    def season(self, newSeason):
        if newSeason in self.SEASON_MULTIPLIERS:
            self.__season = newSeason
        else:
            raise ValueError(f"{newSeason} season is not a valid season. Options: {list(self.SEASON_MULTIPLIERS.keys())}")

    def SeasonPrice(self):
        return self.baseNightPrice * self.SEASON_MULTIPLIERS[self.season]
        
    def book(self):
        if not self.disponibility:  
            self.disponibility = True
        else:
            raise ValueError("Hosting is already booked.")

    def setFree(self):
        if self.disponibility: 
            self.disponibility = False
        else:
            raise ValueError("Hosting is already available.")

    def showInfo(self):
        return f"HOSTING INFO \n Phone: {self.phone} \n Type: {self.type} \n Max capacity: {self.maxCapacity} \n Base night price: {self.baseNightPrice} \n Amenities: {self.amenities} \n Disponibility: {self.disponibility}"

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



class Reservation:
    VALID_STATES = {"confirmed", "in progress", "finished", "canceled"}
    def __init__(self, idReservation, guest, hosting, dateCheckIn, dateCheckOut, additionalServices, totalPrice, state):
        self.__idReservation = idReservation
        self.__guest = guest
        self.__hosting = hosting
        self.__dateCheckIn = datetime.strptime(dateCheckIn, "%Y-%m-%d").date()
        self.__dateCheckOut = datetime.strptime(dateCheckOut, "%Y-%m-%d").date()
        self.__additionalServices = []
        self.__totalPrice = totalPrice
        self.__state = state

    @property
    def idReservation(self):
        return self.__idReservation
    
    @idReservation.setter
    def idReservation(self, newIdReservation):
        self.__idReservation = newIdReservation

    @property
    def guest(self):
        return self.__guest
    
    @guest.setter
    def guest(self, new_guest):
        if isinstance(new_guest, Guest):
            self.__guest = new_guest
        else:
            raise ValueError(f"{new_guest} needs to be an object from 'Guest' Class.")
        
    @property
    def hosting(self):
        return self.__hosting
    
    @hosting.setter
    def hosting(self, new_hosting):
        if isinstance(new_hosting, Hosting):
            self.__hosting = new_hosting
        else:
            raise ValueError(f"{new_hosting} needs to be an object from 'Hosting' Class.")
    
    @property
    def dateCheckIn(self):
        return self.__dateCheckIn
    
    @dateCheckIn.setter
    def dateCheckIn(self, newDateCheckIn):
        self.__dateCheckIn = newDateCheckIn
    
    @property
    def dateCheckOut(self):
        return self.__dateCheckOut
    
    @dateCheckOut.setter
    def dateCheckOut(self, newDateCheckOut):
        self.__dateCheckOut = newDateCheckOut

    @property
    def additionalServices(self):
        return self.__additionalServices
    
    @additionalServices.setter
    def additionalServices(self, newAdditionalServices):
        self.__additionalServices = newAdditionalServices
    
    @property
    def totalPrice(self):
        return self.__totalPrice
    
    @totalPrice.setter
    def totalPrice(self, newTotalPrice):
        self.__totalPrice = newTotalPrice

    @property
    def state(self):
        return self.__state
    
    @state.setter
    def state(self, new_state):
        if new_state in self.VALID_STATES:
            self.__state = new_state
        else:
            raise ValueError(f"{new_state} is not a valid state. Options: {self.VALID_STATES}")
        
    def estimateNights(self):
        return (self.__dateCheckOut - self.__dateCheckIn).days
        
    
    def addService(self, service):
        if isinstance(service, AdditionalService):
            self.__additionalServices.append(service)
        else:
            raise ValueError(f"The added service ({service}) is not an available Additional Service")
    
    def estimateTotalPrice(self):
        hostingPrice = self.__hosting.SeasonPrice()
        additionalService = sum(service.price for service in self.additionalServices)

        self.__totalPrice = (self.estimateNights() * hostingPrice) + additionalService
        return f"Total price for reservation: {self.__totalPrice:.0f}"
    
    def show_info(self):
        return (f"Reservation Code: {self.idReservation} \n Guest: {self.guest.name} \n"
                f"Hosting: {self.hosting.type} - {self.hosting.number if hasattr(self.hosting, 'number') else 'N/A'}\n"
                f"Check-in: {self.dateCheckIn}\n Check-out: {self.dateCheckOut}\n"
                f"Total Price: {self.totalPrice}\n State: {self.state}")

    

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
    
    def createReservation(self, guestId, hostingNum, checkIn, checkOut):
        guest = next((g for g in self.__guests if g.id == guestId), None)
        hosting = next((h for h in self.__hostings if h.number == hostingNum), None)

        if guest and hosting:
            new_reservation = Reservation(guest, hosting, checkIn, checkOut)
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


    


