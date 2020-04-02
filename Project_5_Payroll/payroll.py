import os
employees = []
PAY_LOGFILE = "payroll.txt"



class Hourly():
    def __init__(self, emp):
        self.hoursWorked = 0
        self.emp = emp

    def issuePayment(self):
        amount = float(self.emp.hourly) * float(self.hoursWorked)
        amount = '{0:.2f}'.format(amount)
        self.hoursWorked = 0
        self.emp.payMethod.logPayment(amount)

    def add_timecard(self, hours):
        self.hoursWorked += float(hours)


class Salaried():
    def __init__(self, emp):
        self.emp = emp

    def issuePayment(self):
        amount = float(self.emp.salary) / 24
        amount = '{0:.2f}'.format(amount)
        self.emp.payMethod.logPayment(amount)


class Commissioned():
    def __init__(self, emp):

        self.emp = emp
        self.sales_made = 0

    def issuePayment(self):
        amount = float(self.emp.salary) / 24
        amount += self.sales_made * float(self.emp.commission)
        amount = '{0:.2f}'.format(amount)
        self.sales_made = 0
        self.emp.payMethod.logPayment(amount)

    def add_receipt(self, sale):
        self.sales_made += float(sale)



class DirectMethod():
    def __init__(self, emp):
        self.emp = emp

    def logPayment(self, amount):
        file = open(PAY_LOGFILE, 'a')
        file.write('Transferred ' + str(amount) + ' for ' + str(self.emp.name) + ' to ' + str(self.emp.account.replace('\n', '')) + ' at ' + str(self.emp.route) + '\n')
        file.close()

class MailMethod():
    def __init__(self, emp):
        self.emp = emp
    
    def logPayment(self, amount):
        file = open(PAY_LOGFILE, 'a')
        file.write('Mailing ' + str(amount) + ' to ' + str(self.emp.name) + ' at ' + str(self.emp.address) + ' ' + str(self.emp.zipCode) + '\n')
        file.close()


class Employee():
    def __init__(self, empID, name, address, city, state, zipCode, classification, payMethod, salary, hourly, commission, route, account):
        self.empID         = empID
        self.name           = name
        self.address        = address
        self.city           = city
        self.state          = state
        self.zipCode        = zipCode
        self.payMethod      = payMethod
        self.route          = route
        self.account        = account
        self.hourly         = hourly
        self.salary         = salary
        self.commission     = commission

        if classification == "1":
            self.classification = Hourly(self)
        elif classification == "2":
            self.classification = Salaried(self)
        elif classification == "3":
            self.classification = Commissioned(self)
        else:
            print('invalid classification')

        if payMethod == '1':
            self.payMethod = DirectMethod(self)
        elif payMethod == '2':
            self.payMethod = MailMethod(self)
        else:
            print('invalid paymethod')
        
    def make_salaried(self, salary):
        self.salary = salary
        self.classification = Salaried(self)

    def make_commissioned(self, salary, commission):
        self.salary = salary
        self.commission = commission
        self.classification = Commissioned(self)

    def make_hourly(self, hourly):
        self.hourly = hourly
        self.classification = Hourly(self)

    def mail_method(self):
        self.payMethod = MailMethod(self)

    def direct_method(self, route, account):
        self.route = route
        self.accoount = account
        self.payMethod = DirectMethod(self)

    def issue_payment(self):
        self.classification.issuePayment()
        
    def __str__(self):
        return str(self.empID)  
      
        

def process_timecards():
    file = open('timecards.txt', 'r')
    content = file.readlines()

    for line in content:
        data = line.split(',')
        empID = data.pop(0)
        employee = find_employee_by_id(empID)
        
        for timecard in data:
            employee.classification.add_timecard(timecard)


def process_receipts():
    file = open('receipts.txt', 'r')
    content = file.readlines()

    for line in content:
        data = line.split(',')
        empID = data.pop(0)
        employee = find_employee_by_id(empID)

        for receipt in data:
            employee.classification.add_receipt(receipt)




def find_employee_by_id(id):
    global employees
    employee = list(filter(lambda x: x.empID == id, employees))[0]
    return employee





def run_payroll():
    if os.path.exists(PAY_LOGFILE):
        os.remove(PAY_LOGFILE)
    for emp in employees:
        emp.classification.issuePayment()







def load_employees():
    file = open('employees.csv', 'r')
    contents = file.readlines()
    contents.pop(0)
    
    for person in contents:
        global employees
        data = person.split(',')
        employee = Employee(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12])
        employees.append(employee)
        
    
