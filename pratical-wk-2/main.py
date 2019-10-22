from Owner import Owner
from Phone import Phone

newowner = Owner("john")
newowner.set_email("john@mail.com")
newphone = Phone('12345678',newowner)
print(newphone.get_number())
print(newphone.get_owner())