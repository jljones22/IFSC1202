class Employee:
    def __init__(self, firstName, lastName, IDNumber, hoursWorked, wage):
        self.firstName = firstName
        self.lastName = lastName
        self.IDNumber = IDNumber
        self.hoursWorked = hoursWorked
        self.wage = wage

    def weeklyPay(self):
        return self.wage * self.hoursWorked if self.hoursWorked < 41.0 else self.wage * self.hoursWorked * 1.5

employee = open("10.06 Payroll.txt", "rt")
line = employee.readline()

print(f"{'First':>8}{'Last':>8}{'ID':>8}{'Hours':>8}{'Hourly':>8}{'Weekly':>8}")
print(f"{'Name':>8}{'Name':>8}{'Number':>8}{'Worked':>8}{'Wage':>8}{'Pay':>8}")

while line != "":
    ls = line.strip().split(',')

    emp = Employee(ls[0], ls[1], ls[2], float(ls[3]), float(ls[4]))
    print(f"{emp.firstName:>8}{emp.lastName:>8}{emp.IDNumber:>8}{emp.hoursWorked:>8}{emp.wage:>8}{emp.weeklyPay():>8}")

    line = employee.readline()

employee.close()