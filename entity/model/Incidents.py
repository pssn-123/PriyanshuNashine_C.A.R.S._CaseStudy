class Incidents:
    def __init__(self, incidentid, incident_type, incident_date, latitude, longitude, status, victim_id, suspect_id, case_id):
        self.__IncidentID = incidentid
        self.__IncidentType = incident_type
        self.__IncidentDate = incident_date
        self.__Latitude = latitude
        self.__Longitude = longitude
        self.__Status = status
        self.__VictimID = victim_id
        self.__SuspectID = suspect_id
        self.__CaseID = case_id

    # setters
    def set_incidentid(self, incidentid):
        self.__IncidentID = incidentid

    def set_incidenttype(self, incidenttype):
        self.__IncidentType = incidenttype

    def set_incidentdate(self, incidentdate):
        self.__IncidentDate = incidentdate

    def set_location(self, latitude):
        self.__Latitude = latitude

    def set_location(self, longitude):
        self.__Longitude = longitude

    def set_status(self, status):
        self.__Status = status

    def set_victimid(self, victimid):
        self.__VictimID = victimid

    def set_suspectid(self, suspectid):
        self.__SuspectID = suspectid

    def set_caseid(self, caseid):
        self.__CaseID = caseid

    # getters
    def get_incidentid(self):
        return self.__IncidentID

    def get_incidenttype(self):
        return self.__IncidentType

    def get_incidentdate(self):
        return self.__IncidentDate

    def get_latitude(self):
        return self.__Latitude

    def get_longitude(self):
        return self.__Longitude

    def get_status(self):
        return self.__Status

    def get_victimid(self):
        return self.__VictimID

    def get_suspectid(self):
        return self.__SuspectID

    def get_caseid(self):
        return self.__CaseID