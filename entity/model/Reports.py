class Reports:
    def __init__(self, reportid, incidentid, reportingofficer, reportdate, reportdetails):
        self.__ReportID = reportid
        self.__IncidentID = incidentid
        self.__ReportingOfficer = reportingofficer
        self.__ReportDate = reportdate
        self.__ReportDetails = reportdetails

    # setters
    def set_reportid(self, reportid):
        self.__ReportID = reportid

    def set_incidentid(self, incidentid):
        self.__IncidentID = incidentid

    def set_reportingofficer(self, reportingofficer):
        self.__ReportingOfficer = reportingofficer

    def set_reportdate(self, reportdate):
        self.__ReportDate = reportdate

    def set_reportdetails(self, reportdetails):
        self.__ReportDetails = reportdetails

    # getters
    def get_reportid(self):
        return self.__ReportID

    def get_incidentid(self):
        return self.__IncidentID

    def get_reportingofficer(self):
        return self.__ReportingOfficer

    def get_reportdate(self):
        return self.__ReportDate

    def get_reportdetails(self):
        return self.__ReportDetails
