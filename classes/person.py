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
    
    def showInfo(self):
        return f"INFORMATION \n Name: {self.name} \n Phone: {self.phone} \n Email: {self.email} \n Identification: {self.identification}"
    
    def confirmCreation(self):
        return f"Correctly created {self.name} object person"
                

