from entity.model.Incidents import *
from entity.model.Reports import *
from dao.ICrimeAnalysisService import *
from util.DBConnection import DBConnection


class CrimeAnalysisServiceImpl(ICrimeAnalysisService,Incidents):
    def __init__(self):
        self.connection = DBConnection.getConnection()
        if self.connection is None:
            print('Failed to Establish the connection')

    def createIncident(self, incident:Incidents) -> bool:
        try:
            cursor = self.connection.cursor()
            query = 'Insert into incidents(IncidentID, IncidentType, IncidentDate, Latitudes, Longitudes, Description, Status, VictimID, SuspectID) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            values = (incident.get_incidentid(), incident.get_incidenttype(), incident.get_incidentdate(), incident.get_latitude(), incident.get_longitude(), incident.get_description(), incident.get_status(), incident.get_victimid(), incident.get_suspectid())
            cursor.execute(query,values)
            self.connection.commit()
            return True
        except Exception as e:
            print("Error :", e)
            return False
        finally:
            if cursor:
                cursor.close()


    def updateIncidentStatus(self, incidentid, status):
        try:
            cursor = self.connection.cursor()
            query = 'update incidents set status = %s where incidentid = %s'
            cursor.execute(query, (status, incidentid))
            self.connection.commit()
            return True
        except Exception as e:
            print('Error :',e)
            return False
        finally:
            if cursor:
                cursor.close()

    def getIncidentsInDateRange(self, startdate, enddate) -> list[Incidents]:
        try:
            cursor = self.connection.cursor()
            query = 'Select * from incidents where incidentdate between %s and %s'
            cursor.execute(query ,(startdate, enddate))
            rows = cursor.fetchall()
            incidents = []
            for row in rows:
                incident = Incidents(
                    incidentid=row[0],
                    incidenttype=row[1],
                    incidentdate=row[2],
                    latitude = row[3],
                    longitude=row[4],
                    description=row[5],
                    status=row[6],
                    victimid=row[7],
                    suspectid=row[8]
                )
                incidents.append(incident)
            return incidents

        except Exception as e:
            print('Error :', e)
            return None

    def searchIncidents(self, incidenttype):
        cursor = self.connection.cursor()
        query = 'Select * from incidents where incidenttype = %s'
        cursor.execute(query, (incidenttype))
        self.connection.commit()

    # having doubt
    def generateIncidentReport(self, incidentid) -> list[Reports]:
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


    def createCase(self):
        cursor = self.connection.cursor()
        query = ('Insert into ')
        self.connection.commit()

    def getCaseDetails(self):
        self.connection.commit()

    def updateCaseDetails(self):

        self.connection.commit()

    def getallcases(self:list)->list:
        cursor = self.connection.cursor()
        cursor.execute('Select * from incidents')
        cases = cursor.fetchall()
        self.connection.commit()

