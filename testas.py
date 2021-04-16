import random
import time
from colorama import *
import math


def pasirinktimas():
    print('|------------------------------------------|')
    print(Fore.RED + '\t|- Ką šiandien nori mokytis? -|')
    koks_veiksmas = input(Fore.GREEN + '\tDaugybą (D), Sudėtį (S) ar Atimtį (A)?- ').lower()
    if koks_veiksmas == 'd':
        return daugyba()
    elif koks_veiksmas == 's':
        return sudetis()
    elif koks_veiksmas == 'a':
        return atimtis()
    else:
        print('\tAtsakymas turi būti: "D", "S" ar "A" raidės')
        pasirinktimas()


def daugyba():
    try:
        print(Fore.RED + '\t|- Daugybos lentelės testas -|')
        bandymai = int(input(Fore.YELLOW + '\tKelis kartus nori spręsti? (25/50)- '))
        if bandymai in [2, 25, 50]:
            print(Style.RESET_ALL)
            pagalba = 1
            spejimai = 0
            atsakyti = []
            testo_pradzia = time.time()
            kartojimas_teigiami = ['t', 'taip', 'teip', 'y', 'yes', 'ok']

            while True:
                x = random.randint(2, 9)
                y = random.randint(2, 9)
                teisingas = x * y
                dabar = time.time()
                uzgaista = math.ceil(dabar - testo_pradzia)
                laiko_vertimas = int(uzgaista)
                minutes = laiko_vertimas // 60
                sekundes = laiko_vertimas % 60

                print('|------------------------------------------|')
                print('\tKiek bus ' + str(x) + ' padauginus iš ' + str(y) + '?')
                atsakimas = int(input(Fore.BLUE + '\tĮrašyk atsakymą ir paspausk ENTER:- '))
                print('|------------------------------------------|')
                if atsakimas == teisingas:
                    bandymai -= 1
                    spejimai += 1
                    atsakyti.append([f'{x} x {y} = {teisingas}'])
                    print(Fore.GREEN + f'\tPuiku! Atsakei i {spejimai} klausymų(-us)')
                    print(f'\tLiko {bandymai} klausimų(-ai)')
                    print(Style.RESET_ALL)
                    if bandymai == 0:
                        print('Testas išspręstas per:' + Fore.RED + f' {minutes} min. {sekundes} sek.')
                        print(Fore.MAGENTA + 'Atsakei teisingai {} kartų(-us) iš eilės.'.format(spejimai))
                        print(Fore.YELLOW + 'Teisingi atsakymai buvo šie:')
                        print(*atsakyti, sep="\n")
                        kartojimas = input(Fore.GREEN + '\nNori bandyti dar kartą? (T/N)- ').lower()
                        if kartojimas in kartojimas_teigiami:
                            daugyba()
                        else:
                            pasirinktimas()
                    else:
                        pass
                else:
                    print('\nNETEISINGAI! ' + Fore.RED +  'Teisingas atsakymas: ' + Fore.GREEN + '{}'.format(teisingas))
                    print(Fore.RED + 'Atsakei teisingai {} kartą(-us) iš eilės.'.format(spejimai))
                    if spejimai > 0:
                        print(Fore.YELLOW + 'Teisingi atsakymai buvo šie:')
                        print(*atsakyti, sep="\n")
                        print('\nTestas neišspręstas. Užtrukai:' + Fore.RED + f' {minutes} min. {sekundes} sek.')
                        print(Style.RESET_ALL)
                    else:
                        pass
                    kartojimas = input(Fore.GREEN + 'Nori bandyti dar kartą? (T/N)- ').lower()
                    if kartojimas in kartojimas_teigiami:
                        daugyba()
                    else:
                        pasirinktimas()
        else:
            print(
                '\tGalima rinktis iš' + Fore.RED + ' 25' + Fore.YELLOW +
                ' arba' + Fore.RED + ' 50' + Fore.YELLOW + ' spėjimų')
            daugyba()
    except ValueError:
        print('Atsakymas negali būti raidė!')
        daugyba()


def sudetis():
    try:
        print(Fore.RED + '\t|- Sudėties testas -|')
        bandymai = int(input(Fore.YELLOW + '\tKelis kartus nori spręsti? (25/50)- '))
        if bandymai in [2, 25, 50]:
            print(Style.RESET_ALL)
            spejimai = 0
            atsakyti = []
            testo_pradzia = time.time()
            kartojimas_teigiami = ['t', 'taip', 'teip', 'y', 'yes', 'ok']

            while True:
                x = random.randint(11, 99)
                y = random.randint(11, 99)
                teisingas = x + y
                dabar = time.time()
                uzgaista = math.ceil(dabar - testo_pradzia)
                laiko_vertimas = int(uzgaista)
                minutes = laiko_vertimas // 60
                sekundes = laiko_vertimas % 60

                print('|------------------------------------------|')
                print('\tKiek bus ' + str(x) + ' + ' + str(y) + '?')
                atsakimas = int(input(Fore.BLUE + '\tĮrašyk atsakymą ir paspausk ENTER:- '))
                print('|------------------------------------------|')
                if atsakimas == teisingas:
                    bandymai -= 1
                    spejimai += 1
                    atsakyti.append([f'{x} + {y} = {teisingas}'])
                    print(Fore.GREEN + f'\tPuiku! Atsakei i {spejimai} klausymų(-us)')
                    print(f'\tLiko {bandymai} klausimų(-ai)')
                    print(Style.RESET_ALL)
                    if bandymai == 0:
                        print('Testas išspręstas per:' + Fore.RED + f' {minutes} min. {sekundes} sek.')
                        print(Fore.MAGENTA + 'Atsakei teisingai {} kartų(-us) iš eilės.'.format(spejimai))
                        print(Fore.YELLOW + 'Teisingi atsakymai buvo šie:')
                        print(*atsakyti, sep="\n")
                        kartojimas = input(Fore.GREEN + '\nNori bandyti dar kartą? (T/N)- ').lower()
                        if kartojimas in kartojimas_teigiami:
                            sudetis()
                        else:
                            pasirinktimas()
                    else:
                        pass
                else:
                    print('\nNETEISINGAI! ' + Fore.RED +  'Teisingas atsakymas: ' + Fore.GREEN + '{}'.format(teisingas))
                    print(Fore.RED + 'Atsakei teisingai {} kartą(-us) iš eilės.'.format(spejimai))
                    if spejimai > 0:
                        print(Fore.YELLOW + 'Teisingi atsakymai buvo šie:')
                        print(*atsakyti, sep="\n")
                        print('\nTestas neišspręstas. Užtrukai:' + Fore.RED + f' {minutes} minutes. {sekundes} sek.')
                        print(Style.RESET_ALL)
                    else:
                        pass
                    kartojimas = input(Fore.GREEN + 'Nori bandyti dar kartą? (T/N)- ').lower()
                    if kartojimas in kartojimas_teigiami:
                        sudetis()
                    else:
                        pasirinktimas()
        else:
            print(
                '\tGalima rinktis iš' + Fore.RED + ' 25' + Fore.YELLOW +
                ' arba' + Fore.RED + ' 50' + Fore.YELLOW + ' spėjimų')
            sudetis()
    except ValueError:
        print('Atsakymas negali būti raidė!')
        sudetis()


def atimtis():
    try:
        print(Fore.RED + '\t|- Atimties testas -|')
        bandymai = int(input(Fore.YELLOW + '\tKelis kartus nori spręsti? (25/50)- '))
        if bandymai in [2, 25, 50]:
            print(Style.RESET_ALL)
            spejimai = 0
            atsakyti = []
            testo_pradzia = time.time()
            kartojimas_teigiami = ['t', 'taip', 'teip', 'y', 'yes', 'ok']

            while True:
                x = random.randint(99, 199)
                y = random.randint(11, 99)
                teisingas = x - y
                dabar = time.time()
                uzgaista = math.ceil(dabar - testo_pradzia)
                laiko_vertimas = int(uzgaista)
                minutes = laiko_vertimas // 60
                sekundes = laiko_vertimas % 60

                print('|------------------------------------------|')
                print('\tKiek bus ' + str(x) + ' - ' + str(y) + '?')
                atsakimas = int(input(Fore.BLUE + '\tĮrašyk atsakymą ir paspausk ENTER:- '))
                print('|------------------------------------------|')
                if atsakimas == teisingas:
                    bandymai -= 1
                    spejimai += 1
                    atsakyti.append([f'{x} - {y} = {teisingas}'])
                    print(Fore.GREEN + f'\tPuiku! Atsakei i {spejimai} klausymų(-us)')
                    print(f'\tLiko {bandymai} klausimų(-ai)')
                    print(Style.RESET_ALL)
                    if bandymai == 0:
                        print('Testas išspręstas per:' + Fore.RED + f' {minutes} min. {sekundes} sek.')
                        print(Fore.MAGENTA + 'Atsakei teisingai {} kartų(-us) iš eilės.'.format(spejimai))
                        print(Fore.YELLOW + 'Teisingi atsakymai buvo šie:')
                        print(*atsakyti, sep="\n")
                        kartojimas = input(Fore.GREEN + '\nNori bandyti dar kartą? (T/N)- ').lower()
                        if kartojimas in kartojimas_teigiami:
                            atimtis()
                        else:
                            pasirinktimas()
                    else:
                        pass
                else:
                    print('\nNETEISINGAI! ' + Fore.RED +  'Teisingas atsakymas: ' + Fore.GREEN + '{}'.format(teisingas))
                    print(Fore.RED + 'Atsakei teisingai {} kartą(-us) iš eilės.'.format(spejimai))
                    if spejimai > 0:
                        print(Fore.YELLOW + 'Teisingi atsakymai buvo šie:')
                        print(*atsakyti, sep="\n")
                        print('\nTestas neišspręstas. Užtrukai:' + Fore.RED + f' {minutes} min. {sekundes} sek.')
                        print(Style.RESET_ALL)
                    else:
                        pass
                    kartojimas = input(Fore.GREEN + 'Nori bandyti dar kartą? (T/N)- ').lower()
                    if kartojimas in kartojimas_teigiami:
                        atimtis()
                    else:
                        pasirinktimas()
        else:
            print(
                '\tGalima rinktis iš' + Fore.RED + ' 15' + Fore.YELLOW +
                ' arba' + Fore.RED + ' 50' + Fore.YELLOW + ' spėjimų')
            atimtis()
    except ValueError:
        print('Atsakymas negali būti raidė!')
        atimtis()


def lentele():
    while True:
        kartojimas_teigiami = ['t', 'taip', 'teip', 'y', 'yes', 'ok']
        skaiciai = list(range(1, 10))
        print(Fore.BLUE + '\nPasikartosime daugybos lentelę.')
        skaicius = int(input(Fore.RED + 'Kokio skaičiaus ' + Fore.BLUE + 'daugybos lentelę norėtum pasikartoti?- '))
        multiplied_list = [element * skaicius for element in skaiciai]
        print(Style.RESET_ALL)

        print(f'Daugybos lentelė iš {skaicius}')
        print(f'{skaicius} x {skaiciai[0]} = {multiplied_list[0]}')
        print(f'{skaicius} x {skaiciai[1]} = {multiplied_list[1]}')
        print(f'{skaicius} x {skaiciai[2]} = {multiplied_list[2]}')
        print(f'{skaicius} x {skaiciai[3]} = {multiplied_list[3]}')
        print(f'{skaicius} x {skaiciai[4]} = {multiplied_list[4]}')
        print(f'{skaicius} x {skaiciai[5]} = {multiplied_list[5]}')
        print(f'{skaicius} x {skaiciai[6]} = {multiplied_list[6]}')
        print(f'{skaicius} x {skaiciai[7]} = {multiplied_list[7]}')
        print(f'{skaicius} x {skaiciai[8]} = {multiplied_list[8]}')
        print(f'{skaicius} x {skaiciai[9]} = {multiplied_list[9]}')
        kartojimas = input(Fore.GREEN + 'Nori kartotis kitą skaičių? (T/N)- ').lower()
        if kartojimas in kartojimas_teigiami:
            lentele()
        else:
            pasirinktimas()


pasirinktimas()
