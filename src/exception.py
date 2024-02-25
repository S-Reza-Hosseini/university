class NumError(Exception):

    def __init__(self, msg = "The number is higher than the limit"):
        self.message = msg
        super().__init__(self.message)

        def __repr__(self):
            return self.__class__.__name__()



class NameConflict(Exception):

    def __init__(self, name, msg = "This professor has not taken the lesson"):
        self.message = msg
        self.name = name
        super().__init__(self.message)

        def __repr__(self):
            return self.__class__.__name__()
