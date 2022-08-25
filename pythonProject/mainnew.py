from leave import Leave
from basketleave import BasketOfLeave
from restrictedleave import RestrictedLeave
r1=RestrictedLeave(22772,"nayana",20,"2001-08-13")
print(r1.display_dob())
b1=BasketOfLeave(22772,"nayana",10,1)
print(b1.display())
print(b1.displayleave())