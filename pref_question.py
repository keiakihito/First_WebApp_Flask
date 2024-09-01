import random
from typing import Dict, List, Tuple


def pref_location() -> Tuple[str, str, str]:
    pref_city_dict: Dict[str, str] ={}
    pref_url_dict: Dict[str, str]={}

    with open("prefectural_office_location.txt", encoding="utf-8") as f:
        for i in f:
            txt_lines = i.rstrip().split(",")


            pref: str = txt_lines[0]
            city: str = txt_lines[1]
            url: str = txt_lines[2]

            #Create a dictionary which is the different name of capital prefecture with prefecture name
            if pref not in pref_city_dict:
                pref_city_dict[pref]=city

            #Make a dictionary to create a dictionary
            #Key: prefecture, Value: url
            if url not in pref_url_dict:
                pref_url_dict[pref]=url

    # Create a list of prefecture names for random selection
    pref_name: List[str] = list(pref_city_dict.keys())

    #Get a city name and url which are chosen in the list
    random_pref: str = random.choice(pref_name)

    city_name: str = pref_city_dict[random_pref]
    pref_url: str = pref_url_dict[random_pref]

    return random_pref, city_name, pref_url

if __name__ == "__main__":
    p, c, u = pref_location()
    print(p, c, u)




