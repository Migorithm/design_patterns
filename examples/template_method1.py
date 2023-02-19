#Problem
class SalesReport:
    def __init__(self,company,sales):
        self.company = company
        self.sales = sales
    def make_report(self):
        print("\n** REPORT HEAD **")
        print("Company: "+self.company)
        print("***********************")
        print("Sales: " +str(self.sales))


class CostsReport:
    def __init__(self,company,costs):
        self.company = company
        self.costs = costs
    def make_report(self):
        print("\n** REPORT HEAD **")
        print("Company: "+self.company)
        print("***********************")
        print("Costs: " +str(self.costs))

sales_report = SalesReport("Google", 20000)
sales_report.make_report()
costs_report = CostsReport("Amazon", 50000)
costs_report.make_report()



# Problem - code duplication
class Report:
    def make_report(self):
        print("\n** REPORT HEAD **")
        print("Company: "+self.company)
        print("***********************")


class ImprovedSalesReport(Report):
    def __init__(self,company,sales):
        self.company = company
        self.sales = sales
    def make_report(self):
        super().make_report()
        print("Sales: " +str(self.sales))


class ImprovedCostsReport(Report):
    def __init__(self,company,costs):
        self.company = company
        self.costs = costs
    def make_report(self):
        super().make_report()
        print("Costs: " +str(self.costs))


sales_report = ImprovedSalesReport("Google", 20000)
sales_report.make_report()
costs_report = ImprovedCostsReport("Amazon", 50000)
costs_report.make_report()

# Problem - call super antipattern
# There is nothing wrong with a derived class method using a base class method
# BUT *requiring is an anti-pattern, as it will not be enforced by a language feature,
# allowing mistakes to occur.


# Solution - template method
from abc import ABC,abstractmethod

class ReportTemplate(ABC):

    @abstractmethod
    def make_report_body(self):
        pass
    
    def make_report(self):
        print("\n** REPORT HEAD **")
        print("Company: "+self.company)
        print("***********************")
        self.make_report_body()
    
class MoreImprovedSalesReport(ReportTemplate):
    def __init__(self,company,sales):
        self.company = company
        self.sales = sales

    def make_report_body(self):
        print("Sales: " +str(self.sales))

class ImprovedCostsReport(ReportTemplate):
    def __init__(self,company,costs):
        self.company = company
        self.costs = costs

    def make_report_body(self):
        print("Costs: " +str(self.costs))


cost_report = ImprovedCostsReport("Amazon", 50000)

cost_report.make_report()