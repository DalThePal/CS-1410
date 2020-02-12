employees = []
CLASSIFICATIONS = {
    1: "Hourly",
    2: "Salaried",
    3: "Commissioned"
}
PAYMETHODS = {
    1: "Direct Deposit",
    2: "Check"
}

class Employee():
    def __init__(self, emp_id, name, address, city, state, zipcode, classification, paymethod):
        self.emp_id         = emp_id
        self.name           = name
        self.address        = address
        self.city           = city
        self.state          = state
        self.zipcode        = zipcode
        self.classification = classification
        self.paymethod      = paymethod
        
    def changeType(self, newType):
        self.type = newType
        
    def changePayment(self, newPayment):
        self.payment = newPayment
        
        
def load_employees():
    file = open('employees.csv', 'r')
    contents = file.readlines()
    contents.pop(0)
    
    for person in contents:
        global employees
        data = person.split(',')
        print(person)
        print(data)
        employee = Employee(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
        employees.append(employee)
        
    
