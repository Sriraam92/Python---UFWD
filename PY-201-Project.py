import requests
from colorama import Fore

poke_name = input("Enter the Pokemon Name: ")
poke = poke_name.lower()
req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke}")

if req.status_code == 200:
    data = req.json()
    stat = data['stats']
    print(Fore.GREEN+f"\n{poke.upper()} INFO\n")
    print(Fore.RED+f"experience : "+Fore.CYAN+f"{data['base_experience']}")
    for item in stat:
        val = item['base_stat']
        stat_name = item['stat']['name']
        print(Fore.RED+f"{stat_name} : "+Fore.CYAN+f"{val}"+Fore.WHITE)
    print("")
else:
    print(Fore.RED+"\nInvalid Pokemon Entered\n"+Fore.WHITE)

