from entity.model.Incidents import *
from entity.model.Reports import *
from entity.model.Case import *
from exception.myexceptions import *
from dao.ICrimeAnalysisService import *
from typing import *
from util.DBConnection import DBConnection



class CrimeAnalysisServiceImpl(ICrimeAnalysisService,Incidents):
    def __init__(self):
        self.connection = DBConnection.getConnection()
        if self.connection is None:
            print('Failed to Establish the connection')

    def create_incident(self, incident:Incidents) -> bool:
        try:
            cursor = self.connection.cursor()

            query = 'Insert into incidents(IncidentID, IncidentType, IncidentDate, Latitudes, Longitudes,Status, VictimID, SuspectID, CaseID) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            values = [
                incident.get_incidentid(), incident.get_incidenttype(), incident.get_incidentdate(),
                incident.get_latitude(), incident.get_longitude(),
                incident.get_status(), incident.get_victimid(), incident.get_suspectid(), incident.get_caseid()
            ]
            cursor.execute(query,values)
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            if e.errno == 1062:
                print("duplicate Incidentid not acceptable insert a unique incidentid")
            else:
                print('Error creating incident',e)
            return False


    def update_incident_status(self, incidentid, status):
        try:
            cursor = self.connection.cursor()
            query = 'update incidents set status = %s where incidentid = %s'
            rowsAffected = cursor.execute(query, (status, incidentid))
            self.connection.commit()
            return True

        except Exception as e:
            print('Error :', e)
            return False
        finally:
            if cursor:
                cursor.close()

    def get_incidents_in_date_range(self, startdate, enddate) -> list[Incidents]:
        try:
            cursor = self.connection.cursor()
            query = 'Select * from incidents where incidentdate between %s and %s'
            cursor.execute(query ,(startdate, enddate))
            rows = cursor.fetchall()
            incidents = []
            for row in rows:
                incident = Incidents(incidentid=row[0], incident_type=row[1], incident_date=row[2], latitude=row[3],
                                     longitude=row[4], status=row[5], victim_id=row[6], suspect_id=row[7],
                                     case_id=row[5])
                incidents.append(incident)
            return incidents
        except IncidentNumberNotFound as e:
            print('Error :', e)
            return None
        finally:
            if cursor:
                cursor.close()

    def search_incidents(self, incidenttype):
        cursor = self.connection.cursor()
        query = 'Select * from incidents where incidenttype = %s'
        cursor.execute(query, (incidenttype,))
        incidents = cursor.fetchall()
        self.connection.commit()
        return incidents

    # having doubt
    def generate_incident_report(self, incidentid) -> list[Reports]:
            cursor = self.connection.cursor()
            query = 'Select * from reports where incidentid = %s'
            value = (incidentid, )
            cursor.execute(query, value)
            rows = cursor.fetchall()
            reports = []
            for row in rows:
                report = Reports(
                    reportid= row[0],
                    incidentid=row[1],
                    reportingofficer=row[2],
                    reportdate = row[3],
                    reportdetails=row[4]
                )
                reports.append(report)
            self.connection.commit()
            return reports


    def create_case(self, case_description: str) -> Case :
        try:
            cursor = self.connection.cursor()

            insert_case_query = "INSERT INTO Cases (CaseDescription) VALUES (%s)"
            cursor.execute(insert_case_query, (case_description,))
            case_id = cursor.lastrowid
            self.connection.commit()
            cursor.close()

            return Case(case_id, case_description, [])
        except Exception as e:
            print(f"Error creating case: {e}")
            return None

    def get_all_cases(self) -> list[Case]:
        #try:
            cursor = self.connection.cursor()
            select_query = "SELECT * FROM Cases"
            cursor.execute(select_query)
            cases_data = cursor.fetchall()

            cases = []
            for case_data in cases_data:
                case_id, case_description = case_data[0], case_data[1]

                select_query = "SELECT * from Incidents WHERE CaseID = %s"
                cursor.execute(select_query, (case_id,))
                incidents_data = cursor.fetchall()

                incidents = [Incidents(* incident_data)for incident_data in incidents_data]
                case_instance = Case(case_id, case_description, incidents)
                cases.append(case_instance)

            cursor.close()
            return cases
        #except Exception as e:
            #print(f"Error getting all cases: {e}")
            #return []

    def get_case_details(self, case_id: int) -> Case:
        try:
            cursor = self.connection.cursor()

            # SQL query to retrieve case details and associated incidents
            select_query = ("SELECT c.CaseID, c.CaseDescription, i.IncidentID, i.IncidentDate, i.IncidentType, i.Latitudes, i.Longitudes, i.Status, i.VictimID, i.SuspectID "
                            "FROM Cases c LEFT JOIN Incidents i ON c.CaseID = i.CaseID WHERE c.CaseID = %s")
            cursor.execute(select_query, (case_id,))
            results = cursor.fetchall()

            if results:
                case_id, case_description = results[0][:2]
                incidents = []

                for row in results:
                    incident_id, incident_date, incident_type, latitude, longitude, status, victim_id, suspect_id = row[
                                                                                                                       2:]
                    incidents.append(
                        Incidents(incident_id, incident_type, incident_date, latitude, longitude, status, victim_id,
                                  suspect_id, case_id))

                cursor.close()
                return Case(case_id, case_description, incidents)
            else:
                cursor.close()
                return None
        except Exception as e:
            print(f"Error getting case details: {e}")
            return None

    def update_case_details(self, case: Case) -> bool:
        try:
            cursor = self.connection.cursor()
            case_id=case.get_case_id()
            in_cases = cursor.execute(('select * from cases where CaseID = %s'),(case_id, ))
            if in_cases:
                update_query = "UPDATE Cases SET CaseDescription = %s WHERE CaseID = %s"
                cursor.execute(update_query, (case.get_description(), case.get_case_id()))
                self.connection.commit()
                cursor.close()
                return True
        except Exception as e:
            print(f"Error updating case details: {e}")
            return False

    def delete_incident(self, incident_id: int) -> bool:
        try:
            cursor = self.connection.cursor()

            # Execute the DELETE query to delete the incident with the given incident_id
            delete_query = "DELETE FROM Incidents WHERE IncidentID = %s"
            cursor.execute(delete_query, (incident_id,))

            # Commit the transaction and close the cursor
            self.connection.commit()
            cursor.close()

            # Return True to indicate successful deletion
            return True
        except Exception as e:
            # Handle any errors that may occur during deletion
            print(f"Error deleting incident: {e}")
            return False

    def show_incidents(self):
        cursor = self.connection.cursor()
        query = 'Select * from incidents'
        cursor.execute(query)
        incidents = cursor.fetchall()
        self.connection.commit()
        for incident in incidents:
            print(incident)