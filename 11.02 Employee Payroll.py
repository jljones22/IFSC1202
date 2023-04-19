class Employee:
    def __init__(self, firstName, lastName, IDNumber, wage):
        self.firstName = firstName
        self.lastName = lastName
        self.IDNumber = IDNumber
        self.hoursWorked = 0
        self.wage = wage

    def weeklyPay(self):
        return self.wage * self.hoursWorked if self.hoursWorked < 41.0 else 1.5 * self.wage * self.hoursWorked

def findEmployee(ls, empID):
    for i in range(len(ls)):
        if ls[i].IDNumber.replace(" ", "") == empID:
            return i
    else: return -1

employee = open("11.02 Employees.txt", "rt")
line = employee.readline()

el = []

while line != "":
    ls = line.strip().split(',')

    emp = Employee(ls[0], ls[1], ls[2], float(ls[3]))
    el.append(emp)

    line = employee.readline()

employee.close()

employee = open("11.02 Hours.txt", "rt")
line = employee.readline()

while line != "":
    ls = line.strip().split(',')

    index = findEmployee(el, ls[0])
    if (not index < 0): el[index].hoursWorked = int(ls[1])

    line = employee.readline()

print(f"{'First':>8}{'Last':>8}{'ID':>8}{'Hours':>8}{'Hourly':>8}{'Weekly':>8}")
print(f"{'Name':>8}{'Name':>8}{'Number':>8}{'Worked':>8}{'Wage':>8}{'Pay':>8}")

for i in range(len(el)):
    print(f"{el[i].firstName:>8}{el[i].lastName:>8}{el[i].IDNumber:>8}{el[i].hoursWorked:>8}{el[i].wage:>8}{el[i].weeklyPay():>8}")

# I still don't understand how to calculate weeklypay from your other feedback. 
# Please do an example when you leave feedback using actual numbers. 
# I need to see it to understand it.