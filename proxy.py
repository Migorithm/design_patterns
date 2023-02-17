"""
Proxy pattern is basically to control an access to a certain object.
It suggests that you craete a new proxy class with the same 'interface' as an
original service object. Then you update your app so that it passes the proxy 
object to all of the original object's clients.

Unlike Facade, Proxy has the same interface as its service object, 
which makes them interchangeable.
"""



from abc import ABC,abstractmethod


class IPerson(ABC):
    """
    Interface for Person class
    """
    @abstractmethod
    def do_something(self):
        """
        Interface for do_something method
        """


class Person(IPerson):
    """
    Concrete class for Person Object
    """

    def do_something(self):
        print("Do Something from person")


class PersonProxy(IPerson):
    """
    Proxy Person Class For 'Encapsulating the behaviour' of Person
    """

    def __init__(self):
        self.person = Person()

    def do_something(self):
        print("Do Something from proxy")
        self.person.do_something()
        print("Things done from proxy")


p = PersonProxy()
p.do_something()


### Real world analogy - Credit card(Proxy for a bank account)

class ITransaction(ABC):

    @abstractmethod
    def append_transaction(self,amount):
        pass

class Transaction(ITransaction):
    def __init__(self):
        self.balance =0 

    def append_transaction(self,amount):
        self.balance += amount
    
class PTransaction(ITransaction):
    def __init__(self):
        self.transaction = Transaction()

    def append_transaction(self, amount):
        self._validate_transaction_request(amount)
        print(f"{amount} added...")
        self.transaction.append_transaction(amount)
    
    def _validate_transaction_request(self,amount):
        if self.transaction.balance + amount < 0 :
            raise Exception

trx = PTransaction()

trx.append_transaction(100)
trx.append_transaction(200)
try:
    trx.append_transaction(-400)
except Exception:
    print("Exception Caught")
        

    
