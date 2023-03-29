class LoggableList(list, Loggable):
    def append(self, l):
        self.log(l)
        super().append(l)
