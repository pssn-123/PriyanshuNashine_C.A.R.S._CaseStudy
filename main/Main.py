from dao.CrimeAnalysisServiceImpl import *


class MainModule(CrimeAnalysisServiceImpl):

    @staticmethod
    def menu():
        print('Crime Analysis and Reporting System')
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
        print('Welcome to Crime Analysis and Reporting System')

        while not input("Enter to continue\nor press any key to Exit"):
            MainModule.menu()
            choice = input("Enter your choice of operation:\n")

            #Operation to see the list of incidents not included into the menu of operations
            if choice == 'showincidents':
                crime_service.show_incidents()

            if choice == '1':
                #Create a new Incident
                incidentid = input('Enter IncidentId: ')
                incidenttype = input('Enter Incident type: ')
                incidentdate = input('Enter the Incident date: ')
                latitude = input('Enter the latitude: ')
                longitude = input('Enter the longitude: ')
                status = input('Enter the Incident status: ')
                victimid = input('Enter the victimid: ')
                suspectid = input('enter the suspectid: ')
                caseid = input('enter case id:')

                incident = Incidents(incidentid, incidenttype, incidentdate, latitude, longitude, status, victimid,
                                     suspectid, caseid)
                created = crime_service.create_incident(incident)
                if created:
                    print('Succesfully created new incident')
                    crime_service.show_incidents()

                else:
                    print('Failed to create a new Incident')

            elif choice == '2':
                #Update incident status
                incidentid = input('Enter the incidentid :')
                status = input('Update incident status :')
                updated = crime_service.update_incident_status(incidentid, status)
                if updated:
                    print('Updated the status successfully')
                    crime_service.show_incidents()
                else:
                    print('Failed to update incident status')

            elif choice == '3':
                #Get incidents in the date range
                print('Enter the Daterange to find the incidents')
                startdate = input('Enter the Start date :')
                enddate = input('enter the end date :')
                showincidents = crime_service.get_incidents_in_date_range(startdate, enddate)
                for incidents in showincidents:
                    #print(incidents.get_incidentid(), incidents.get_incidenttype(), incidents.get_incidentdate(), incidents.get_latitude(), incidents.get_longitude(), incidents.get_status(), incidents.get_victimid(), incidents.get_suspectid(), incidents.get_caseid())
                    print("Incident ID:", incidents.get_incidentid())
                    print("Incident Type:", incidents.get_incidenttype())
                    print("Incident Date:", incidents.get_incidentdate())
                    print("Location:", incidents.get_latitude(), incidents.get_longitude())
                    print("Description:", incidents.get_description())
                    print("Status:", incidents.get_status())
                    print("Victim ID:", incidents.get_victimid())
                    print("Suspect ID:", incidents.get_suspectid())
                    print("Case ID:",incidents.get_caseid())
                if showincidents:
                    pass
                else:
                    print('No incidents in the given date range')

            elif choice == '4':
                #Search for incidents
                incidenttype = input('Enter the incidenttype : ')
                searchincident = crime_service.search_incidents(incidenttype)
                for incident in searchincident:
                    print(incident)

            elif choice == '5':
                #Generate Incident Reports
                incidentid = input('Enter the incidentid : ')
                showreport = crime_service.generate_incident_report()
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

            elif choice == "6":
                #create new case and associate with incidents
                case_description = input("Enter Case Description: ")
                new_case = crime_service.create_case(case_description)

                if new_case:
                    print(
                        f"Case created successfully!\nCase ID: {new_case.get_case_id()}, Description: {new_case.get_description()}")
                else:
                    print("Failed to create case.")

            elif choice == "7":
                case_id_to_fetch = int(input("Enter Case ID to fetch details: "))
                fetched_case = crime_service.get_case_details(case_id_to_fetch)

                if fetched_case:
                    print(f"Case Details:\nCase ID: {fetched_case.get_case_id()}, Description: {fetched_case.get_description()}")
                    print("Incidents in the case:")
                    for incident in fetched_case.get_incidents():
                        print(
                            f"Incident ID: {incident.get_incidentid()}, Type: {incident.get_incidenttype()}, Date: {incident.get_incidentdate()}")
                else:
                    print(f"No case found with ID {case_id_to_fetch}.")

            elif choice == "8":
                #try:
                    case_id = int(input("Enter Case ID to update details: "))
                    fetched_case = crime_service.get_case_details(case_id)

                    if fetched_case:
                        new_description = input("Enter updated Case Description: ")
                        fetched_case.set_description(new_description)
                        updated_case = crime_service.update_case_details(fetched_case)
                        if updated_case:
                            print("Case details updated successfully!")
                        else:
                            print("Failed to update case details.")
                    else:
                        print(f"No case found with ID {case_id}.")

                #except ValueError:
                    #print("Invalid input. Please enter a valid Case ID.")

            elif choice == "9":
                all_cases = crime_service.get_all_cases()
                if all_cases:
                    print("All Cases:")
                    for case in all_cases:
                        print(f"Case ID: {case.get_case_id()}, Description: {case.get_description()}")

                else:
                    print("No cases found.")

            elif choice == '10':
                incidentid = input('Insert the incident id to Delete the incident')
                deleted_incidents = crime_service.delete_incident(incidentid)
                if deleted_incidents:
                    print(f"successfully deleted incident with id{incidentid}")
            elif choice == '0':
                break

            else:
                print("Invalid choice. Please enter a number between 0 and 9.")



if __name__ == "__main__":
    MainModule.main()
