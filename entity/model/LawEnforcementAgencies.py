class LawEnforcementAgencies:
    def __init__(self, agencyid, agencyname, jurisdiction, contactinformation):
        self.__AgencyID = agencyid
        self.__AgencyName = agencyname
        self.__Jurisdiction = jurisdiction
        self.__ContactInformation = contactinformation

    # setters
    def set_agencyid(self, agencyid):
        self.__AgencyID = agencyid

    def set_agencyname(self, agencyname):
        self.__AgencyName = agencyname

    def set_jurisdiction(self, jurisdiction):
        self.__Jurisdiction = jurisdiction

    def set_contactinformation(self, contactinformation):
        self.__ContactInformation = contactinformation

    # getters
    def get_agencyid(self):
        return self.__AgencyID

    def get_agencyname(self):
        return self.__AgencyName

    def get_jurisdiction(self):
        return self.__Jurisdiction

    def get_contactinformation(self):
        return self.__ContactInformation
