from entity.model.Case import *
from abc import ABC, abstractmethod


class ICrimeAnalysisService(ABC):
    @abstractmethod
    def create_incident(self, incident):
        pass

    @abstractmethod
    def update_incident_status(self, incidentid, status):
        pass

    @abstractmethod
    def get_incidents_in_date_range(self, startdate, enddate):
        pass

    @abstractmethod
    def search_incidents(self, incidenttype):
        pass

    @abstractmethod
    def generate_incident_report(self, incidentid):
        pass

    @abstractmethod
    def create_case(self):
        pass

    @abstractmethod
    def update_case_details(self, case_id: Case) -> bool:
        pass

    @abstractmethod
    def get_all_cases(self):
        pass

    @abstractmethod
    def get_case_details(self, case_id: int) -> Case:
        pass

    @abstractmethod
    def delete_incident(self, incident_id: int) -> bool:
        pass

    @abstractmethod
    def show_incidents(self):
        pass