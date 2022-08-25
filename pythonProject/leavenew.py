class Leave:
   def __init__(self,Employee_id,Name,LeaveBalance):
        self.employee_id=Employee_id
        self.name=Name
        self.leavebalance=LeaveBalance
   def display(self):
       return self.employee_id,self.name,self.leavebalance
