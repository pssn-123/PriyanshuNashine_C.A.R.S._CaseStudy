from abc import ABC
from exception.myexceptions import IncidentNumberNotFound
from dao.CrimeAnalysisServiceImpl import *


class MainModule(CrimeAnalysisServiceImpl, ABC, IncidentNumberNotFound):

    @staticmethod
    def menu():
        print('1. Create a new incident')
        print('2. Update the status of an incident')
        print('3. Get a list of incidents within a date range')
        print('4. Search for incidents based on various criteria')
        print('5. Generate incident reports')
        print('6. Create a new case and associate it with incidents')
        print('7. Get details of a specific case')
        print('8. Update case details')
        print('9. Get a list of all cases')

    @staticmethod
    def main():
        crime_service = CrimeAnalysisServiceImpl()

        while True:
            MainModule.menu()
            choice = input("Enter your choice of operation:\n")

            if choice == '1':
                #Create a new Incident
                incidentid = input('Enter IncidentId: ')
                incidenttype = input('Enter Incident type: ')
                incidentdate = input('Enter the Incident date: ')
                latitude = input('Enter the latitude: ')
                longitude = input('Enter the longitude: ')
                description = input('Enter the description of the Incident: ')
                status = input('Enter the Incident status: ')
                victimid = input('Enter the victimid: ')
                suspectid = input('enter the suspectid: ')

                incident = Incidents(incidentid, incidenttype, incidentdate, latitude, longitude, description, status, victimid, suspectid)
                created = crime_service.createIncident(incident)
                if created:
                    print('Succesfully created new incident')
                else:
                    print('Failed to create a new Incident')

            elif choice == '2':
                #Update incident status
                incidentid = input('Enter the incidentid :')
                status = input('Update incident status :')
                updated = crime_service.updateIncidentStatus(incidentid, status)
                if updated:
                    print('Updated the status successfully')
                else:
                    print('Failed to update incident status')

            elif choice == '3':
                #Get incidents in the date range
                print('Enter the Daterange to find the incidents')
                startdate = input('Enter the Start date :')
                enddate = input('enter the end date :')
                showincidents = crime_service.getIncidentsInDateRange(startdate, enddate)
                for incidents in showincidents:
                    #print(incidents.get_incidentid(), incidents.get_incidenttype(), incidents.get_incidentdate(), incidents.get_latitude(), incidents.get_longitude(), incidents.get_description(), incidents.get_status(), incidents.get_victimid(), incidents.get_suspectid())
                    print("Incident ID:", incidents.get_incidentid())
                    print("Incident Type:", incidents.get_incidenttype())
                    print("Incident Date:", incidents.get_incidentdate())
                    print("Location:", incidents.get_latitude(), incidents.get_longitude())
                    print("Description:", incidents.get_description())
                    print("Status:", incidents.get_status())
                    print("Victim ID:", incidents.get_victimid())
                    print("Suspect ID:", incidents.get_suspectid())
                    print()
                if showincidents:
                    pass
                else:
                    print('No incidents in the given date range')

            elif choice == '4':
                #Seaerch for incidents
                searchincident = crime_service.searchIncidents()

            elif choice == '5':
                incidentid = input('Enter the incidentid : ')
                showreport = crime_service.generateIncidentReport(incidentid)
                for reports in showreport:
                    print("Report ID :",reports.get_reportid())
                    print('IncidentID : ',reports.get_incidentid())
                    print('Reporting Officer : ',reports.get_reportingofficer())
                    print('Report date : ', reports.get_reportdate())
                    print('Report details : ',reports.get_reportdetails())
                if showreport:
                    pass
                else:
                    print('No reports with give incidentid')

if __name__ == "__main__":
    MainModule.main()
