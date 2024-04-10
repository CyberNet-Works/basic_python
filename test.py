# Colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

BoldRED =  "\033[1m\033[31m"
BoldGREEN =  "\033[1m\033[32m"
BoldYELLOW =  "\033[ \033[33m"
BoldBLUE =  "\033[1m\033[34m"
BoldMAGENTA = "\033[1m\033[35m"
BoldCYAN = "\033[1m\033[36m"
BoldWHITE = "\033[1m\033[37m"

RedUnderlined = "\033[4m\033[31m"

REDBLINKING = "\033[31m\033[5m"
BoldRedBlinking = "\033[1m\033[31m\033[5m"

RESET = "\033[0m"


races = ["human", "elf", "tiflin","dragonbourne", "aurakora", "gnome", "dwarf", "halfling"]

race_choice = input(f"{MAGENTA}Pick your race, coward!\n{races}\n{RESET}")
if race_choice.lower() not in races:
    print(f"{RED}You cannot be that!{RESET}")
else:
    print(f"{GREEN}Okay mighty {race_choice}!{RESET}")


human_characteristics = {"str":0, "con":0, "dex":0, "cha":0, "wis":0, "int":0}
elf_characteristics =  {"str":0, "con":0, "dex":0, "cha":0, "wis":0, "int":0}
tiflin_characteristics = {"str":0, "con":0, "dex":0, "cha":0, "wis":0, "int":0}
dragonbourne_characteristics = {"str":0, "con":0, "dex":0, "cha":0, "wis":0, "int":0}
aurakora_characteristics =  {"str":0, "con":0, "dex":0, "cha":0, "wis":0, "int":0}
gnome_characteristics = {"str":0, "con":0, "dex":0, "cha":0, "wis":0, "int":0}
dwarf_characteristics = {"str":0, "con":0, "dex":0, "cha":0, "wis":0, "int":0}
halfling_characteristics =  {"str":0, "con":0, "dex":0, "cha":0, "wis":0, "int":0}

class Character:
    def __init__(self, 
                 name, 
                 experience_value
                 strength, 
                 constitution, 
                 stamina,
                 agiliity,
                 charisma,
                 wisdom, 
                 intelligence, 
                 encumberance, 
                 inventory, 
                 special_abilities,
                 weapon, 
                 armor, 
                 gold, 
                 level = 1, 
                 experience = 0,
                 hunger_state = , 
                 thirst_state = ,                  
                 ):