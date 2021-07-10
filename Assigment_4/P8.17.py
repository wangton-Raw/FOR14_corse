import urllib.parse
import urllib.request
import re
dic = {}
tabell = []
"""
with urllib.request.urlopen('https://www.cia.gov/library/publications/resources/the-world-factbook/fields/rawdata_211.txt') as response:
   html = response.read()
   str_convert = html.decode("UTF-8")
"""

url = "https://www.cia.gov/library/publications/resources/the-world-factbook/fields/rawdata_211.txt"
txt = urllib.request.urlopen("https://www.cia.gov/library/publications/resources/the-world-factbook/fields/rawdata_211.txt").read().decode("UTF-8")
print(txt)


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



