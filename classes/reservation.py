from datetime import datetime
from classes.guest import Guest
from classes.hosting import Hosting
from classes.additionalservice import AdditionalService

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
    
    def showInfo(self):
        return (f"Reservation Code: {self.idReservation} \n Guest: {self.guest.name} \n"
                f"Hosting: {self.hosting.type} - {self.hosting.number if hasattr(self.hosting, 'number') else 'N/A'}\n"
                f"Check-in: {self.dateCheckIn}\n Check-out: {self.dateCheckOut}\n"
                f"Total Price: {self.totalPrice}\n State: {self.state}")

  