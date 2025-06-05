
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
