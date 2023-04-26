import random
import pycountry


def getNumerics():
    idCountries = []
    j = 0
    for i in pycountry.countries:
        a = list(pycountry.countries)[j]
        idCountries.append(a.numeric)
        j += 1
    return idCountries

def getCountry():
    numCountry = getNumerics()
    numCountry = random.choice(numCountry)
    selectedCountry = pycountry.countries.get(numeric=numCountry)
    selectedCountry = selectedCountry.name
    from deep_translator import GoogleTranslator
    selectedCountry = GoogleTranslator(source='auto', target='pt').translate(selectedCountry)
    return selectedCountry

def printTitle(x):
    print('-' * len(x) + 3 * '-')
    print(x)
    print('-' * len(x) + 3 * '-')
    print()

def mainMenu():
    options = 'login', 'countryRand', 'placar'
    
