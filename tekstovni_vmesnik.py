import model

def izpis_igre(igra):
    return (
        'Pravilni del gesla: {}\n'.format(igra.pravilni_del_gesla()) +
        'Neuspeli poskusi: {}\n'.format(igra.nepravilni_del_gesla()) +
        'Število preostalih poskusov: {}\n'.format(model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak())
    )
    
def izpis_zmage(igra):
    return (
        'Čestitam, uganili ste geslo {}\n'.format(igra.geslo) +
        'Uspelo ti je v {} poskusih\n'.format(len(igra.crke))
    )

def izpis_poraza(igra):
    return (
        'Porabili ste vse poskuse.\n' +
        'Pravilno geslo je bilo {}\n'.format(igra.geslo)
    )

def zahtevaj_vnos():
    return input('Vnesite črko: ')

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        print(izpis_igre(igra))
        poskus = zahtevaj_vnos()
        stanje = igra.ugibaj(poskus) # dobimo eno od petih konstant
        if stanje == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif stanje == model.PORAZ:
            print(izpis_poraza(igra))
            break

pozeni_vmesnik()