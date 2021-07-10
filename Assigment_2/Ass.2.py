# Exercise P4.35

def CredCard():
    lst = []
    lst_2 = []
    lst_3 = []
    lst_4 = []
    tot_sum = 0
    tekst =input("Please write your Credit Card Number: ")

    for i in range(len(tekst)):
        lst.append(int(tekst[i]))
        #Double the numbers and append it in lst:2
        lst_2.append(int(tekst[i])*2)

    #sum every other digit. Start from the end of the string
    sum_other = sum(lst[len(lst)::-2])

#43589795

    #Doble the digit from the list "lst"
    # Fetch the numbers that I want from the list
    lst_3 = (lst_2[len(lst) - 2::-2])

    # Split double digit and use sum for each index
    for i in range(len(lst_3)):
        output = sum(map(int, str(lst_3[i])))
        # Append the sum of each index in a new list
        lst_4.append(output)
    # Sum all the indexes in lst_4
    sum_other_2 = sum(lst_4)
    tot_sum = sum_other + sum_other_2

    if tot_sum % 10 == 0:
        print("The credit card number is correct")
    else:
        print("The credit card number si incorrect")


CredCard()