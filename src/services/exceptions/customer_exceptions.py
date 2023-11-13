class EmailAlreadyExist(Exception):
    def __init__(self, message="E-mail already exists"):
        super().__init__(message)