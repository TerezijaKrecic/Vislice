stevilo_dovoljenih_napak = 10
pravilna_crka = '+'
ponovljena_crka = 'o'
napacna_crka = '-'
zmaga = 'W'
poraz = 'X'


class Igra:
    def __init__(self, geslo):
        self.geslo = geslo # beseda, ki jo igralec poskuša uganiti
        self.crke = [] # dosedanji poskusi igralca
    
    def napacne_crke(self):
        return 0
    
    def pravilne_crke(self):
        return 0

    def stevilo_napak(self):
        return 0

    def zmaga(self):
        return pravilne_crke == geslo
    
    def poraz(self):
        return stevilo_napak == stevilo_dovoljenih_napak + 1
    
    def pravilni_del_gesla(self):
        return geslo

    def nepravilni_del_gesla(self):
        return 0

    def ugibaj(self, crka):
        velika_crka = crka.upper()
        return pravilna_crka

with open('besede.txt') as besede:
    bazen_besed = [beseda for beseda in besede]

import random

def nova_igra():
    Igra(random.choice(bazen_besed))