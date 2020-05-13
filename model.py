import random

STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'    # vrednosti teh konstant niso prav nič pomembne, le da so različne!
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZMAGA = 'W'
PORAZ = 'X'

class Igra:
    def __init__(self, geslo, crke=None): # NE crke=[] (ce imamo vec Iger ...)
        self.geslo = geslo.upper() # beseda, ki jo igralec poskuša uganiti
        self.crke = [] if crke is None else [crka.upper() for crka in crke] # dosedanji poskusi igralca; crke so seznam nizov z enim znakom
                        # temu se reče pogojni izraz (vse v eni vrsti, brez dvopičja)

    def napacne_crke(self): # vrne seznam nepravilnih ugibanj igralca
        return [crka for crka in self.crke if crka not in self.geslo]
    
    def pravilne_crke(self): # vrne seznam pravilnih ugibanj igralca
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self): # izracuna št. napačnih ugibov je igralec že naredil
        return len(self.napacne_crke())

    def zmaga(self): # ali trenutno stanje določa zmago
        return set(self.pravilne_crke()) == set(self.geslo)
        # return all(crka in self.crke for crka in self.geslo)
    
    def poraz(self): # ali trenutno stanje določa poraz
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK
    
    def pravilni_del_gesla(self): # vrne niz z že uganjenim delom gesla s podčrtaji
        uganjen_del = ''
        for crka in self.geslo:
            uganjen_del += crka if crka in self.crke else '_'
        return uganjen_del

    def nepravilni_del_gesla(self): # vrne niz s presledkom ločene nepravilne ugibe igralca
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):  # sprejme crko in vrne primernego konstanto
        ugibana_crka = crka.upper()
        if ugibana_crka in self.crke:
            return PONOVLJENA_CRKA
        self.crke.append(ugibana_crka)
        if ugibana_crka in self.geslo:
            if self.zmaga():
                return ZMAGA
            return PRAVILNA_CRKA
        elif self.poraz():
            return PORAZ
        else:
            return NAPACNA_CRKA


with open('besede.txt', encoding='utf-8') as besede:
    bazen_besed = [beseda.strip().upper() for beseda in besede]

def nova_igra():
    beseda = random.choice(bazen_besed)
    Igra(beseda)