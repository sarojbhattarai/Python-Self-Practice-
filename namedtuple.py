import collections
# Sale = collections.namedtuple("Sale", "price quantity")
# sales= Sale(10,20)
# # total = Sa.price * Sale.quantity
# print(sales.price)

College = collections.namedtuple("College","Location Name Dlass")
Dlass = collections.namedtuple("Class","classteacher rollno")
#VERY BAD PRACTICE TO NAME CLASS

college_information = College("Baruwagaun","Gorkha", Dlass("Loke",39))
# print(college_information.Location)
# print(college_information.Name)
# print(college_information.Dlass.classteacher)
print("Location is {}. School name is {}. Class Teacher is {}".format(college_information.Location,college_information.Name,college_information.Dlass.classteacher))
# print("{0.Location}".format(college_information))
# print("{Name}".format(**college_information._asdict()))