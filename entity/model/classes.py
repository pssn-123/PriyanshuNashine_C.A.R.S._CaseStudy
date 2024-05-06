# incident class
class Incidents:
    def __init__(self, incidentid, incidenttype, incidentdate, location, description, status, victimid, suspectid):
        self.__IncidentID = incidentid
        self.__IncidentType = incidenttype
        self.__IncidentDate = incidentdate
        self.__Location = location
        self.__Description = description
        self.__Status = status
        self.__VictimID = victimid
        self.__SuspectID = suspectid

    # setters
    def set_incidentid(self, incidentid):
        self.__IncidentID = incidentid

    def set_incidenttype(self, incidenttype):
        self.__IncidentType = incidenttype

    def incidentdate(self, incidentdate):
        self.__IncidentDate = incidentdate

    def set_location(self, location):
        self.__Location = location

    def set_description(self, description):
        self.__Description = description

    def set_status(self, status):
        self.__Status = status

    def set_victimid(self, victimid):
        self.__VictimID = victimid

    def set_suspectid(self, suspectid):
        self.__SuspectID = suspectid

    # getters
    def get_incidentid(self):
        return self.__IncidentID

    def get_incidenttype(self):
        return self.__IncidentType

    def get_incidentdate(self):
        return self.__IncidentDate

    def get_location(self):
        return self.__Location

    def get_description(self):
        return self.__Description

    def get_status(self):
        return self.__Status

    def get_victimid(self):
        return self.__VictimID

    def get_suspectid(self):
        return self.__SuspectID