class IncidentNumberNotFound(Exception):
    def __init__(self, msg = 'Incident id Not found or already exist'):
        super().__init__(msg)

class null_description_not_acceptable(Exception):
    def __init__(self, msg = 'Description field left empty and cannot be continued further'):
        super().__init__(msg)

class case_id_not_found(Exception):
    def __init__(self, msg = 'Case ID not present in cases table'):
        super().__init__(msg)