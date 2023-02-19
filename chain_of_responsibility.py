from abc import ABC, abstractmethod

class Logger(ABC):

    __next_logger:"Logger" = None
    
    def set_next(self,next_logger:"Logger"):
        if self.__next_logger:
            self.__next_logger.set_next(next_logger=next_logger)
        else:
            self.__next_logger = next_logger
        return self

    @abstractmethod
    def do_things(self,message):
        pass
    

    #The following method is actually an example of "template method pattern"
    def log(self,message):
        self.do_things(message)
        if self.__next_logger is None:
            return
        self.__next_logger.log(message)


class ConsoleLogger(Logger):
    def do_things(self, message):
        print("**CONSOLE :", message)


class FileLogger(Logger):

    def do_things(self, message):
        print("**FILE: ",message)

class DBLogger(Logger):
    def do_things(self, message):
        print("**DB: ",message)
    



con = ConsoleLogger().set_next(FileLogger()).set_next(DBLogger())


con.log("Test")
