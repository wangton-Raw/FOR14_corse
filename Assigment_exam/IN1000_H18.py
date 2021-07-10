class Hytte:
    def __init__(self, navn,ant_senger,pris):
        self.navn = navn
        self.ant_senger =ant_senger
        self.pris = pris

    def hentNavn(self):
        return self.navn

    def totPris(self, antall_pers):
        return antall_pers * self.pris

    def sjekkPlass(self,antall_pers):
        if self.ant_senger >= antall_pers:
            return True

    def __str__(self):
        return self.navn + self.ant_senger + self.pris


class Tur:
    def __init__(self, list_hytte, beskriv):
        self.list_hytte =list_hytte # hente navn fra klassen hytte
        self.beskriv = beskriv #lese tekstfil turer

    def skrivtur(self):
        return self.beskriv # må sjekke om det skrives ut om hver hytte turen går gjennom

    def sjekkPrisPlass(self, antall_pers, maks_belop ):
        if Hytte.sjekkPlass() == True and Hytte.totPris(antall_pers) <= maks_belop:
            return True
        else:
            return False


class Turplanlegger:
    def __init__(self, hytteF, turerF):
        self.hytteF = hytteF
        self.turerF = turerF
        self.a = open(self.hytteF)
        self.b = open(self.turerF)



    def hytterFraFil(self):
        dic = {}
        liste = []
        navn = []
        totpers = []
        pris = []

        liste = []
        for linje in self.a:
            liste.append(linje.rstrip())
        print(liste)

        for linje in liste:
            skille = linje.split(" ")
            navn.append(skille[0]) # hyttenanv
            totpers.append(skille[1]) # antall senger
            pris.append(skille[2]) # pris

        for i in range(len(navn)):
            dic[navn[i]] = Hytte(navn[i],totpers[i], pris[i])
        print(dic)

    def turerFraFil(self):
        count = 0
        beskrivelse = []
        hytter = []

        liste = []
        for linje in self.b:
            liste.append(linje.rstrip())

        for line in liste:
            count += 1
            if count % 2 == 0:  # this is the remainder operator
                hytter.append(line)
            else:
                beskrivelse.append(line)
        print("-------------------------------")
        print(hytter)
        print(beskrivelse)

    def finnturer(self, ant_pers, maksbelop, maks_dager):
        pass














