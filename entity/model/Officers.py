class Officers:
    def __init__(self, officerid, firstname, lastname, badgenumber, rank, address, phonenumber, agencyid):
        self.__OfficerID = officerid
        self.__FirstName = firstname
        self.__LastName = lastname
        self.__BadgeNumber = badgenumber
        self.__Rank = rank
        self.__address = address
        self.__phonenumber = phonenumber
        self.__AgencyID = agencyid

    # setters
    def set_officerid(self, officerid):
        self.__OfficerID = officerid

    def set_firstname(self, firstname):
        self.__FirstName = firstname

    def set_lastname(self, lastname):
        self.__LastName = lastname

    def set_badgenumber(self, badgenumber):
        self.__BadgeNumber = badgenumber

    def set_rank(self, rank):
        self.__Rank = rank

    def set_address(self, address):
        self.__address = address

    def set_phonenumber(self, phonenumber):
        self.__phonenumber = phonenumber

    def set_agencyid(self, agencyid):
        self.__AgencyID = agencyid

    # getters
    def get_officerid(self):
        return self.__OfficerID

    def get_firstname(self):
        return self.__FirstName

    def get_lastname(self):
        return self.__LastName

    def get_badgenumber(self):
        return self.__BadgeNumber

    def get_rank(self):
        return self.__Rank

    def get_address(self):
        return self.__address

    def get_phonenumber(self):
        return self.__phonenumber

    def get_agencyid(self):
        return self.__AgencyID
