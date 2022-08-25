from empnew import employee
from addnew import Address
address1=Address("eluru")
address2=Address("hyd")

emp1=employee("nayana","anudeep","guntur")
emp2=employee("nayana","anudeep",[address1,address2])
print(address1.display())
print(address2.display())
print(emp1.display())
print(emp2.display())
