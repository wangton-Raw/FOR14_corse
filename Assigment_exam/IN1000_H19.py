class Rett:
    def __init__(self, navn, pris, innhold):
        self.navn = str(navn)
        self.pris = float(pris)
        self.innhold = innhold

    def __str__(self):
        return f"rett : {self.navn},  pris: {str(self.pris)}, innhold: {str(self.innhold)}"


    def sjekkInnholdOK(self, liste_innhold):
        for i in range(len(liste_innhold)):
            for j in range(len(self.innhold)):
                if liste_innhold[i] == self.innhold[j]:
                    print("JAAAA")
                    return False

        print("hallllaa")
        return True
liste_a = ["a","b", "c"]
liste_b = ["g","h","x","z"]
a = Rett("hei", 30,liste_a)
b = Rett("halo",15, liste_b)
print(a)
liste_2 = ["c"]
a.sjekkInnholdOK(liste_2)

class kategori:
    def __init__(self, katnavn, retter):
        self.katnavn = katnavn
        self.retter = retter
        self.godkjent = []
        print("jipi")

    def hentOkRetter(self, innga_liste):
        for i in range(len(innga_liste)):
            for j in range(len(self.retter)):
                if innga_liste[i] != self.retter[j].innhold:
                    self.godkjent.append(self.retter)
        print(self.godkjent)
    def __str__(self):
        return f"{self.godkjent}"

liste_retter = [a,b]
polse = kategori("pølse", liste_retter)
print(polse.hentOkRetter(["a"]))








