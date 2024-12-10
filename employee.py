class Employee:
    def __init__(self,fname:str,sname:str):
        self.__fname = fname
        self.__sname = sname
        fullname = self.__fname + " " + self.__sname
        email = self.__fname + "." + self.__sname + "@company.com"
        firstname = self.__fname