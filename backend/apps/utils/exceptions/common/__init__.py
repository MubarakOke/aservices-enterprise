class QuerySetException(Exception):
    def __init__(self, errors, message):
        self.errors= errors
        self.message = message