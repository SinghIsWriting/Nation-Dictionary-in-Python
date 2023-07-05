import colorama   # importing colorama python library for colorful text
from colorama import Fore
colorama.init(autoreset=True)
from countryinfo import CountryInfo   # using countryinfo python library

# take input country name
c = input("Enter country: ").title()

country = CountryInfo(c)

spelling= country.alt_spellings()          # spelling of country name
capital_of_country= country.capital()      # capital of country
capitals_lanlng= country.capital_latlng()  # latitude and longitude of country
callingCode = country.calling_codes()      # calling code of country
areaOfCountry = country.area()             # area of country
populationOfCountry = country.population() # population of country
neighbourCountries = country.borders()     # border countries of this country
currenciesInCountry = country.currencies() # valid currencies in the country
languageInCountry = country.languages()    # languages in the country
residents = country.demonym()              # name natives/residents
nationalFlag = country.flag()              # flag of country
geography = country.geo_json()             # geography of country
isos = country.iso()                       # Iso of country
coordinates = country.latlng()             # latitude and longitude of country
countryName = country.name()               # full name of country
nativeNames = country.native_name()        # name of natives
provincesInCountry = country.provinces()   # list of all provinces of the country
regionOfCountry = country.region()         # region of the country
subregionOfCountry = country.subregion()   # subregion of the country
timezone = country.timezones()             # timezones of the country
topLevelDomain = country.tld()             # Internet country code top-level domain
translation = country.translations()       # translations in country
wikiURL = country.wiki()                   # wikipedia URL of country

print(f"{Fore.GREEN}Speelings:",spelling)
print(f"{Fore.GREEN}Capital:",capital_of_country)
print(f"{Fore.GREEN}Capital's lat,lon:",capitals_lanlng)
print(f"{Fore.GREEN}Calling code:",callingCode)
print(f"{Fore.GREEN}Area:",areaOfCountry)
print(f"{Fore.GREEN}Population:",populationOfCountry)
print(f"{Fore.GREEN}Border counteies:",neighbourCountries)
print(f"{Fore.GREEN}Currencies:",currenciesInCountry)
print(f"{Fore.GREEN}Languages:",languageInCountry)
print(f"{Fore.GREEN}Demonym/Residents:",residents)
print(f"{Fore.GREEN}flag:",nationalFlag)
print(f"{Fore.GREEN}Geograpy:",geography['features'][0]['id'],",",geography['features'][0]['properties']['name'],",",geography['features'][0]['geometry']['type'])
print(f"{Fore.GREEN}Iso:",isos)
print(f"{Fore.GREEN}Latitude, Longitude:",coordinates)
print(f"{Fore.GREEN}Name:",countryName)
print(f"{Fore.GREEN}Native name:",nativeNames)
print(f"{Fore.GREEN}Provinces:",len(provincesInCountry),"\n",provincesInCountry)
print(f"{Fore.GREEN}Region:",regionOfCountry)
print(f"{Fore.GREEN}Sub-region:",subregionOfCountry)
print(f"{Fore.GREEN}Timezone:",timezone)
print(f"{Fore.GREEN}Tld:",topLevelDomain)
print(f"{Fore.GREEN}Translations:",translation)
print(f"{Fore.GREEN}Visit wikipedia:",wikiURL)

