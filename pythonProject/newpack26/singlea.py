class singleaddress:
    def __init__(self,lastname,firstname, streetaddress,city,state,country,postalcode):
        self.lname = lastname
        self.fname = firstname
        self.stradd = streetaddress
        self.city = city
        self.state = state
        self.country = country
        self.postal = postalcode
    def get_details(self):
        return self.lname,self.fname,self.stradd,self.city,self.state,self.country,self.postal
    def set_details(self,x):
        self.lname=x
s = singleaddress()
s.set_details('nayana')
print(s.get_details())
    def set_details(self,y):
         self.fname=y
         s = singleaddress()
s.set_details('devadula')
print(s.get_details())
    def set_details(z):
          self.stradd=z
s = singleaddress()
s.set_details(343)
print(s.get_details())
    def set_details(a):
        self.city=a
s = singleaddress()
s.set_details('hyd')
print(s.get_details())
      def set_details(b):
          self.state=b
s = singleaddress()
s.set_details('ts')
print(s.get_details())
      def set_details(c):
          self.country=c
s = singleaddress()
s.set_details('india')
print(s.get_details())
      def set_details(d):
          self.postal=d
s = singleaddress()
s.set_details(534001)
print(s.get_details())