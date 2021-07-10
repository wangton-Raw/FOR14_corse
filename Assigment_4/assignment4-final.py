#r6.18----------
wack=[2, -2, -2, 3]
def byeNegativ(liste):
    for i in range(len(liste)):
        if liste[i] <0: #if the indexed value is lower than zero
            liste.remove(liste[i]) #remove the value from the list, thus preserving the order
            #end if
        
    print(liste) #This pseudocode does not compute, "list index out of range"
        
                  
def byeN2(liste):
    poslist=[] #Create a new list
    for i in range(len(liste)): #for each value in the the list
        if liste[i] >=0: #if value isn't negativ then
            poslist.append(liste[i]) #add to poslist
            #end if

    print(poslist)#print list to show results
    
#byeN2(wack)
   
#r6.25---------------- 
"""
head < - 0
count_heads < - 0
taile < - 1
count_tailes < - 0
values_list < - list containing a sequence of values

for elements in values_list do:
    if the list contains a head do:
        count_heads
        increase
        by
        one
    endif
    if the list contains a taile do:
        count_tailes
        increase
        by
        one
    endif

if count_heads > count_tailes:
    output
    count_heads
endif
if count_heads == count_tailes:
output both count_heads and count_tailes
endif
else:
output
count_tailes
"""

#p6.21----------------
def drawsquare(row1,row2,row3,row4): #function just to drawt the square
    print("Here is the current square: ")
    print(row1)
    print(row2)
    print(row3)
    print(row4)
    
def testmagic(row1, row2, row3, row4): #function to test if it's a magic box
    
    xrow1=sum(row1) #Finding the sum for each row
    xrow2=sum(row2)
    xrow3=sum(row3)
    xrow4=sum(row4)

    col1=row1[0]+row2[0]+row3[0]+row4[0] #finding the sum for each column
    col2=row1[1]+row2[1]+row3[1]+row4[1]
    col3=row1[2]+row2[2]+row3[2]+row4[2]
    col4=row1[3]+row2[3]+row3[3]+row4[3]
    
    dia1=row1[0]+row2[1]+row3[2]+row4[3] #finding the sum for each diagonal 
    dia2=row1[3]+row2[2]+row3[1]+row4[0]
    
    if xrow1 == xrow2 == xrow3 == xrow4 == col1 == col2 == col3 == col4 == dia1 == dia2:
        print("We have a magic box!!! ")
        print("The magic number was: ", xrow1)
    else:
        print("This isn't very magical...")
    
    
def magicsquares(): 
    row1=[' ',' ',' ',' '] #Empty listes for the rows
    row2=[' ',' ',' ',' ']
    row3=[' ',' ',' ',' ']
    row4=[' ',' ',' ',' ']
    
    
    for i in range (0, len(row1)):   #User input for each row, where the for-loop picks up each value untill max range is reached
        x=int(input("Type in the values for row1 magic box: "))
        row1[i]=x
        
    
    for i in range (0, len(row2)):
        x=int(input("Type in the values for row2 magic box: "))
        row2[i]=x
    
    for i in range (0, len(row3)):
        x=int(input("Type in the values for row3 magic box: "))
        row3[i]=x
       
    for i in range (0, len(row4)):
        x=int(input("Type in the values for row4 magic box: "))
        row4[i]=x
    
       
    drawsquare(row1,row2,row3,row4)
    testmagic(row1,row2,row3,row4)
    
#magicsquares() I have written a program that lets the user input all 16 slots and the magic number from the task is 34.

#p6.22-----------------
def createmagic(n):
    row = n - 1
    col = n // 2

    matrix = []
    for row in range(0, n) :
       matrix.append([None] * n)
       #filling up a mtarix with the size of n
       
       
    
    for k in range(1, n**2):
        matrix[row][col] = k
        row_x = row
        col_x = col
        #increment row and column:
        row += 1
        col += 1
        #if the row or coloumn is n then, replace it with 0
        if row == n:
            row = 0
        if col == n:
            col = 0
            
        #If the box is filled, use their previous values 
        if matrix[row][col] != None:
          row = row_x
          col = col_x
          row = row - 1 #Decrement row
        
#r6.32------------------        
def sumlist(liste): #made a function that would sum up elements in a list
    x=0
    for i in range(len(liste)):
        x+=liste[i]
    return x


#if they buy a pet and at least five other items => discount 20% on other items, but not on the pets
       
def discount(prices, isPet, nItems): #Function will display the dicount 
    #prices[i] is the price before the discount (an empty list for my use, and not necessary as a parameter to the function) 
    #isPet[i] is true if the item is a pet 
    #nItems is the amount of items bought
    
    discount_p=[] #An empty list for the prices if a discount is valid
    
    for i in range(nItems):
        x=int(input("What is the price of the item? "))
        c=input("Is this item a pet or another item? [Y]=Pet, [N]=Item ")
        prices.append(x)    
        
        if c.upper() == "Y": #With a pet, there isn't a discount 
            discount_p.append(x)
            isPet.append(c.upper()) #This will tell us futher on if a pet as been bought or not
        
        elif c.upper() == "N" and nItems >= 5:
            d=x*0.80 #discount for 20% 
            discount_p.append(d)
        
        elif c.upper() == "N" and nItems < 5:
            continue #We already know that this customer isn't eligible for a discount
                    #The non-discounted price is already put in prices[]
        
    if nItems >= 5 and "Y" in isPet:  #This prints out information regarding the discount 
        print("Your orginal price is: ", sumlist(prices))
        print("Your discounted price is: ", sumlist(discount_p))
        print("The discount you got was: ", sumlist(prices) - sumlist(discount_p))
        
    
    else: #This prints out the oringal sum, if you don't qualify for a discount
        print("You do not qualify for a discount ")
        print("Your price is: ", sumlist(prices))
            
q=[]
w=[]
#discount(q,w,5)

#r8.1-------------------------------------------------------------------------------
"""
For a school database for blocked websites, they should use dictionaries. The URL-link could be the "key" and if the
key is found in for example banned{...}, then it can return "false" hwich can be used to block access. If the key isn't
found in banned{...}, then the website is all good.

You could do what i just described for lists and sets as well, by finding the url-link through for example banned[...], but this
it makes the editing process for banned sites less streamlined (need to use more lines of codes to go through a list
to find the index of the banned web-site in the list. With a dictionary you could search and edit the key and value directly
"""
                  
   
#p8.4-------------------------------------------------------------------------------
def isnr_prime(num):
    if num > 1:
   # check for factors
        for i in range(2,num):
            if (num % i) == 0:
               #print(num,"is not a prime number")
               return False
               break
              
        else:
            #print(num,"is a prime number")
            return True
            
    else:
        #print(num, "is not a prime number")
        return False
            
                
            
def Eratosthenes(n): 
    nr_set=set()
    prime_set={1,2} #We already know that 1 and 2 will always be prime
    
    for i in range(1,n+1): #puting in each number up to n in the regular set
        nr_set.add(i)
    
    for j in range(2, n+1): #puting each prime in prime_set
        if isnr_prime(j) is True:
            prime_set.add(j)
        else:
            continue
    
    primes=nr_set.intersection(prime_set) #Cross analysis of both sets
        
    print(primes)
            
    
#Eratosthenes(100)        
#isnr_prime(15)      
    
    
#P8.17 and 18------------------------------------------------
import urllib.parse
import urllib.request
import re
def country_GDPP(): 
    dic = {}
    tabell = []
    """
    with urllib.request.urlopen('https://www.cia.gov/library/publications/resources/the-world-factbook/fields/rawdata_211.txt') as response:
       html = response.read()
       str_convert = html.decode("UTF-8")
    """

    url = "https://www.cia.gov/library/publications/resources/the-world-factbook/fields/rawdata_211.txt"
    txt = urllib.request.urlopen("https://www.cia.gov/library/publications/resources/the-world-factbook/fields/rawdata_211.txt").read().decode("UTF-8")
    #print(txt)
    url = 'https://www.cia.gov/library/publications/resources/the-world-factbook/fields/rawdata_211.txt'
    req = urllib.request.Request(url)

    # En generator som gir deg et element/linje
    response = urllib.request.urlopen(req)

    ordbok = {}

    # Konverterer fra generator til liste
    # Slider fra index 2 til slutten
    for line in list(response)[2:]:
        # rstrip() fjerner new lines bak, strip() fjernr white spaces (mellomrom) foran og bak
        string = line.decode('utf-8').rstrip()
        #Regex - Dersom vi har mer en 2 spaces, så vil den splitte mellom Land og GDP
        string = re.split(r" {2,}", string)
        ordbok[string[1]] = string[2]

    print(ordbok)

    letter  = "L"
    for country in ordbok.keys():
        if country[0] == letter:
            print(country)

    snakke = input("Skriv inn land: ")
    while snakke != "stopp":
        if snakke in ordbok.keys():
            print(ordbok[snakke])
        else:
            print("Skriv på nytt")
        snakke = input("Skriv inn land: ")
        
        

