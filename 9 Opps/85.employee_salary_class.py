class Employee():
    
    def __init__(self,id,name,department,salary,leave):
        self.id = id
        self.name = name
        self.department = department
        self.__salary = salary
        self.attendance = 30
        self.leave = leave

    def work_details(self):
        if self.attendance > 0:
            return f"Work in Progress."
        return "Employee On Leave."
    
    def bonus(self):
        if self.attendance == 30:
            self.__salary = self.__salary + (self.__salary)*0.10
            return f"Employee Bonus Salary : {self.__salary}"
        return "Not Eligible for Bonus."
    
    def get_salary_details(self):
        return self.__salary
    
    def emp_leave(self):
        if self.attendance == self.attendance:
            if self.leave > 10:
                return "Only Maximum 10 Day Leave Allowed!"
            else:
                self.attendance = self.attendance - self.leave
                per_day_salary = self.__salary/30
                deducation = per_day_salary*self.leave
                self.__salary = self.__salary - deducation
        return f"""
    === Leave Process ===
    leave Day : {self.leave}
    Deducation : {deducation:.2f}
    Employee Attendance after Leave : {self.attendance}
    Employee Salary after Leave : {self.__salary:.2f}
    """
    
    
    def employee_details(self):
        return f'''
    === EMPLOYEE SETAILS ===
    ID : {self.id} 
    Name : {self.name}
    Department : {self.department}
    Attendance : {self.attendance}
    Salary : {self.__salary}
    '''