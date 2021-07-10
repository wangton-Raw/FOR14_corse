class Contact:

    def __init__(self, first_name, last_name, phone_number, address):
        self.first_name = first_name.lower()
        self.last_name = last_name.lower()
        #key value
        self.phone_number = str(phone_number)

        self.address = address.lower()
        self.phone_dic = {}

    def store(self):
        # key (som er et unikt nummer) skal være telefonnummer
        self.phone_dic[self.phone_number] = self.first_name, self.last_name, self.phone_number, self.address
        print(self.phone_dic)

    def add(self,first_name, last_name, phone_number, address):
        self.phone_dic[phone_number] = first_name, last_name,str(phone_number),address
        print(self.phone_dic)

    def delete(self, phonenumber):
        verify = input("are you sure you want to delete this? ").lower()
        if verify == "yes":
            self.phone_dic.pop(str(phonenumber))
            print(self.phone_dic)
        else:
            print("process canceled")

    def find(self, info):
        for key, value in self.phone_dic.items():
            for j in range(len(self.phone_dic[self.phone_number])):
                if info == value[j]:
                    print("Det er riktig")
                else:
                    print("Det er feil")
        print(info)


        """
        for i in range(len(self.phone_dic)):
            for j in range(len(self.phone_dic[self.phone_number])):
                if list(self.phone_dic.items())[i][j] == info:
                    print("RIKTIG!!")
                else:
                    print("Cannot find the person")
        """





