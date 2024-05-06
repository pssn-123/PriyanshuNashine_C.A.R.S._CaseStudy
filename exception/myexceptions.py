class IncidentNumberNotFound(Exception):
    def __init__(self, msg):
        super().__init__(msg)


try:
    raise IncidentNumberNotFound('Incident number not found')

except IncidentNumberNotFound as e:
    print(e)

