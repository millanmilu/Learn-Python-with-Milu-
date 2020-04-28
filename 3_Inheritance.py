class  Employee :
    def __init__(self,id ,name):
        self.id = id
        self.name = name
class PayrollSystem:
    def calculate_payroll(self,employees):
        print("Calculating Payroll")
        for employee in employees:
            print(f'payroll for : {employee.id} - {employee.name}')
            print(employee.calculate_payroll())
            print('')



class SalaryEmployee(Employee):
    def __init__(self,id,name,weekly_salary):
        super().__init__(id,name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self,id,name,Hours_Worked,hour_rate):
        super().__init__(id,name)
        self.Hours_worked =Hours_Worked
        self.hour_rate = hour_rate
    def calculate_payroll(self):
        return self.Hours_worked * self.hour_rate
class CommissionEmployee(SalaryEmployee):
    def __init__(self,id,name,weekly_salary,commission):
        super().__init__(id,name,weekly_salary)
        self.commision = commission
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commision

salary_employee = SalaryEmployee(1,"Milln",1500)
hourly_employee = HourlyEmployee(2,"Millan kumar ",40,15)
commission_employee = CommissionEmployee(3,"Kevin ",1000,250)
pay_roll = PayrollSystem()
pay_roll.calculate_payroll([salary_employee,hourly_employee,commission_employee])