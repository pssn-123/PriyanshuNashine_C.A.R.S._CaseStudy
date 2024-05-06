from abc import ABC,abstractmethod
class ICrimeAnalysisService(ABC):
    @abstractmethod
    def createIncident(self,incident):
        pass

    @abstractmethod
    def updateIncidentStatus(self, incidentid, status):
        pass

    @abstractmethod
    def getIncidentsInDateRange(self, startdate, enddate):
        pass

    @abstractmethod
    def searchIncidents(self):
        pass

    @abstractmethod
    def generateIncidentReport(self):
        pass

    @abstractmethod
    def createCase(self):
        pass

    @abstractmethod
    def getCaseDetails(self):
        pass

    @abstractmethod
    def updateCaseDetails(self):
        pass

    @abstractmethod
    def getallcases(self):
        pass
