class IncidentNumberNotFound(Exception):
    def __init__(self, msg = 'Incident id Not found or already exist'):
        super().__init__(msg)



