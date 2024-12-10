class Employee:
    def __init__(self,fname:str,sname:str):
        self.__fname = fname
        self.__sname = sname

    def fullname(self):
        return self.__fname + " " + self.__sname
    def email(self):
        return self.__fname + "." + self.__sname + "@company.com"
