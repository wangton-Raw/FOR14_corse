class Contact:

    def __init__(self,first_name, last_name, phone_number, address):
        self.first_name = first_name.lower()
        self.last_name = last_name.lower()
        self.phone_number = str(phone_number)
        self.address = address.lower()

    def __repr__(self):
        return f"first name :{self.first_name}, last name: {self.last_name}, phone number: {self.phone_number}, adress: {self.address}"

class Phonebook:

    def __init__(self):
        self.phone_list = []
        self.checking_instances = [] # Trenger ikke å være der, brukes kun på checking functionen

    def add(self, new_contact):
        self.phone_list.append(new_contact)

    def delete(self, the_contact):
        print("The delete function:")
        verify = input("Are you sure you want to delete this contact? (Y/N): ")
        if verify == "Y":
            self.phone_list.remove(the_contact)
            print(self.phone_list)
            print("The contact " + str(the_contact) + "has been deleted from the phonebook")

        else:
            print("Could not find the contact when deletion. Please try again")

    def checking(self, inf_contact):
        print("Using checking function:\n")
        for i in range(len(self.phone_list)):
            if (inf_contact == self.phone_list[i].first_name or inf_contact == self.phone_list[i].last_name
                               or inf_contact == self.phone_list[i].phone_number
                               or inf_contact == self.phone_list[i].address):
                self.checking_instances.append(True)
            else:
                self.checking_instances.append(False)

        if True in self.checking_instances:
            index = self.checking_instances.index(True)
            print(f"By searching for {inf_contact} we found first name: {self.phone_list[index].first_name}, "
                    f"last name: {self.phone_list[index].last_name}, phonenumber: {self.phone_list[index].phone_number} "
                    f"and address: {self.phone_list[index].address}")
        else:
            print("Could not find the contact in checking. Please try again")

    def update_phone(self, contact, telephone):
        print("Using update function:")
        if contact in self.phone_list:
            index = self.phone_list.index(contact)
            self.phone_list[index].phone_number = str(telephone)
            print(self.phone_list[index].phone_number)
            print("The telephonenumber has been updated")

        else:
            print("Could not find the contact. Please try again")

    def sort(self, option):
        if option == "first name":
            #import operator
            #a = sorted(self.phone_list, key=operator.attrgetter('first_name'))
            b = sorted(self.phone_list, key=lambda Contact: Contact.first_name)
            print(f"The phone book has been sorted by {option}: ")
            for i in range(len(b)):
                print(b[i])
        elif option == "last name":
            b = sorted(self.phone_list, key=lambda Contact: Contact.last_name)
            #print(a)
            print(f"The phone book has been sorted by {option}: ")
            for i in range(len(b)):
                print(b[i])
        else:
            print("We could not identify the command.Please check for typing error.")



    def check_duplicate(self):
        dup_list = []
        print("Check_duplicate:")
        for i in range(len(self.phone_list)):
            for j in range(len(self.phone_list)):
                if self.phone_list[i].phone_number == self.phone_list[j].phone_number and i != j and j not in dup_list:
                    print(f" {self.phone_list[i].first_name} phonenumber match with {self.phone_list[j].first_name}")
                    dup_list.append(i)

        for i in range(len(dup_list)):
            print(f"Removing {self.phone_list[dup_list[i]].first_name}")
            self.phone_list.pop(dup_list[i])
        if not dup_list:
            print("found no duplicate")




