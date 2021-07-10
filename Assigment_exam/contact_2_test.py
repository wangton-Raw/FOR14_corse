from contact_2 import Contact
from contact_2 import Phonebook


#Hovedprogram

per_1 = Contact("per", "Vu","9999", "fsahashas")
per_2 = Contact("borat", "ss","1111", "ahahha")
per_3 = Contact("Gard", "IDk", "111","10 min unna")
per_4 = Contact("Mats", "IDk", "000000","7 timer unna")
per_5 = Contact("Vegard", "IDk", "000000","7 timer unna")


# Creating a phone book
telephonebook = Phonebook()
# Adding references of the object in phone book
telephonebook.add(per_1)
telephonebook.add(per_2)
telephonebook.add(per_3)
telephonebook.add(per_4)
telephonebook.add(per_5)

#Could be any of the four instances
# Checking any of the four instances
# to see which contact the information belongs to
telephonebook.checking("anton")

# Do not implement a string!!!
# Updating the phonenumber to a referense
#telephonebook.update_phone(per_1,"888")

telephonebook.sort("first name")
telephonebook.check_duplicate()

"""
print(telephonebook.phone_list[0].first_name)
print(telephonebook.phone_list[0].last_name)
print(telephonebook.phone_list[0].phone_number)
"""