from abc import ABC,abstractmethod
class BankApp(ABC):

    def database(self):
        print('connected to database')

    @abstractmethod
    def security(self):
        pass

class MobileApp(BankApp):
    def mobile_login(self):
        return('login into mobile')

    def security(self):
        print('mobile security')
    
mob = MobileApp() # cannont run without security code
mob.database()
mob.security()