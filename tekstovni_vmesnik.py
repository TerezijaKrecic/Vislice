import model

def izpis_igre(igra):
    return (
        'Pravilni del gesla: {}\n'.format(igra.pravilni_del_gesla()) +
        'Neuspeli poskusi: {}\n'.format(igra.nepravilni_del_gesla()) +
        'Število preostalih poskusov: {}\n'.format(model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()) +
        'V slikici:\n{}\n'.format(igra.slika())
    )
    
def izpis_zmage(igra):
    return (
        'Čestitam, uganili ste geslo {}\n'.format(igra.geslo) +
        'Uspelo ti je v {} poskusih\n'.format(len(igra.crke))
    )

def izpis_poraza(igra):
    return (
        'Porabili ste vse poskuse.\n{}\n'.format(igra.slika()) +
        'Pravilno geslo je bilo {}\n'.format(igra.geslo)
    )

def zahtevaj_vnos():
    crka = input('Vnesite črko: ')
    if len(crka) != 1 or not crka.isalpha():
        print('Neveljaven vnos. Poskusite še enkrat.')
        return zahtevaj_vnos()
    else:
        return crka

def pozeni_vmesnik():    # Ko je igra zaključena, naj vmesnik igralcu ponudi ponoven zagon igre.
    igra = model.nova_igra()
    print('Pozdravljeni, pred vami so vislice, ki jih seveda že poznate.\nKar začnimo.\n')
    while True:
        print('========================================')
        print(izpis_igre(igra))
        poskus = zahtevaj_vnos()
        stanje = igra.ugibaj(poskus) # dobimo eno od petih konstant
        if stanje == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif stanje == model.PORAZ:
            print(izpis_poraza(igra))
            break
        elif stanje == model.PONOVLJENA_CRKA:
            print('To črko ste že uporabili. Poskusite še enkrat.\n========================================')

    ponovitev = input("Ali želite ponovno poskusiti? Vpišite 'DA' oz. 'NE': ")
    while ponovitev.upper() not in ['DA', 'NE']:
        ponovitev = input("Neveljaven vnos. Vnesite 'DA' ali 'NE': ")
    if ponovitev.upper() == 'DA':
        pozeni_vmesnik()
    elif ponovitev.upper() == 'NE':
        print('Nasvidenje!')

pozeni_vmesnik()