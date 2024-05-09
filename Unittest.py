import unittest
from datetime import date
from dao.CrimeAnalysisServiceImpl import *


class MyTestCase(unittest.TestCase, CrimeAnalysisServiceImpl):
    def setUp(self):
        self.crime_service = CrimeAnalysisServiceImpl()

    def test_createIncident(self):
        incident = Incidents(incidentid=78, incident_type="Theft", incident_date=date.today(), latitude=20.0225,
                             longitude=12.5223, status="Open", victim_id=1, suspect_id=2, case_id=1)
        result = self.crime_service.create_incident(incident)
        self.assertEqual(result, True)

    def test_updateIncident(self):
        incidentid = 1
        update = self.crime_service.update_incident_status(incidentid, status='Closed')
        self.assertEqual(True, update)

if __name__ == '__main__':
    unittest.main()
