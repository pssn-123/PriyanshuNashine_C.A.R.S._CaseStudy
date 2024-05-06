class Suspect:
    def __init__(self, suspectid, firstname, lastname, dateofbirth, gender, address, phonenumber):
        self.__SuspectID = suspectid
        self.__FirstName = firstname
        self.__LastName = lastname
        self.__dateofbirth = dateofbirth
        self.__gender = gender
        self.__address = address
        self.__phonenumber = phonenumber

    # setters
    def set_suspectid(self, suspectid):
        self.__SuspectID = suspectid

    def set_firstname(self, firstname):
        self.__FirstName = firstname

    def set_lastname(self, lastname):
        self.__LastName = lastname

    def set_dateofbirth(self, dateofbirth):
        self.__dateofbirth = dateofbirth

    def set_gender(self, gender):
        self.__gender = gender

    def set_address(self, address):
        self.__address = address

    def set_phonenumber(self, phonenumber):
        self.__phonenumber = phonenumber

    # getters
    def get_suspectid(self):
        return self.__SuspectID

    def get_firstname(self):
        return self.__FirstName

    def get_lastname(self):
        return self.__LastName

    def get_dateofbirth(self):
        return self.__dateofbirth

    def get_gender(self):
        return self.__gender

    def get_address(self):
        return self.__address

    def get_phonenumber(self):
        return self.__phonenumber
