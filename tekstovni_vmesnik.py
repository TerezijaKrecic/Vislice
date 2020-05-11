import Igra

def izpis_igre(Igra):
    return igra.pravilni_del_gesla

def izpis_zmage(Igra):
    return zmaga

def izpis_poraza(Igra):
    return poraz

def zahtevaj_vnos():
    crka = input('> ')
    return crka

def pozeni_vmesnik():
    Igra()
    while True:
        izpis_igre()
        if zmaga or poraz:
            print('Jeeej')
            break