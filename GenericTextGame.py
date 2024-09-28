CHARPROFILE = {"NAME":"undefined","RACE":"undefined","CLASS":"undefined","MAXHP":0,"HP":0,"ATK":0,"MAXMANA":0,"MANA":0,"MAXSTAMINA":0,"STAMINA":0,"GOLD":15,}

CHARPROFILE["NAME"] = input("What is your name?\n")

#character race prompt
ElfDesc ="HP:20\nATK:5\nMANA:30\nSTAMINA:10"
HumanDesc ="HP:25\nATK:5\nMANA:20\nSTAMINA:25"
OrcDesc ="HP:25\nATK:8\nMANA:10\nSTAMINA:15"
while True:
    CHARPROFILE["RACE"] = input("Where are you from? (Elf, Human, Orc)(Type 'Desc' for a STAT description!)\n")
    if CHARPROFILE["RACE"] == "Elf":
        print("You are an Elf!\n")
        CHARPROFILE["MAXHP"] = 20
        CHARPROFILE["HP"] = 20
        CHARPROFILE["ATK"] = 5
        CHARPROFILE["MAXMANA"] = 30
        CHARPROFILE["MANA"] = 30
        CHARPROFILE["MAXSTAMINA"] = 15
        CHARPROFILE["STAMINA"] = 15
        break
    if CHARPROFILE["RACE"] == "Human":
        print("You are a Human!\n")
        CHARPROFILE["MAXHP"] = 25
        CHARPROFILE["HP"] = 25
        CHARPROFILE["ATK"] = 5
        CHARPROFILE["MAXMANA"] = 15
        CHARPROFILE["MANA"] = 15
        CHARPROFILE["MAXSTAMINA"] = 25
        CHARPROFILE["STAMINA"] = 25
        break
    if CHARPROFILE["RACE"] == "Orc":
        print("You are an Orc!\n")
        CHARPROFILE["MAXHP"] = 25
        CHARPROFILE["HP"] = 25
        CHARPROFILE["ATK"] = 8
        CHARPROFILE["MAXMANA"] = 10
        CHARPROFILE["MANA"] = 10
        CHARPROFILE["MAXSTAMINA"] = 15
        CHARPROFILE["STAMINA"] = 15
        break
    if CHARPROFILE["RACE"] == "Desc":
        print("Elves have increased MANA.\n",ElfDesc,"\nHumans have high STAMINA.\n",HumanDesc,"\nOrcs have high ATK.\n",OrcDesc)
        continue
    else:
        print("You need to pick from the given options!\n")
        continue

#character class prompt
WarriorDesc = "HP:+20\nATK:+10MANA:-5"
MageDesc = "HP:-10\nMANA:+20"
HunterDesc = "HP:+10\nATK:+5\nMANA:+10\nSTAMINA:+5"
while True:
    CHARPROFILE["CLASS"] = input("What is your background? (Warrior, Mage, Hunter) (Type 'Desc' for a STAT description!)\n")
    if CHARPROFILE["CLASS"] == "Warrior":
        print("You are a Warrior!\n")
        CHARPROFILE["MAXHP"] += 20
        CHARPROFILE["HP"] += 20
        CHARPROFILE["ATK"] += 10
        CHARPROFILE["MAXMANA"] += -5
        CHARPROFILE["MANA"] += -5
        break
    if CHARPROFILE["CLASS"] == "Mage":
        print("You are a Mage!\n")
        CHARPROFILE["MAXHP"] += -10
        CHARPROFILE["HP"] += -10
        CHARPROFILE["MAXMANA"] += 20
        CHARPROFILE["MANA"] += 20
        break
    if CHARPROFILE["CLASS"] == "Hunter":
        print ("You are a Hunter!\n")
        CHARPROFILE["MAXHP"] += 10
        CHARPROFILE["HP"] += 10
        CHARPROFILE["ATK"] += 5
        CHARPROFILE["MAXMANA"] += 10
        CHARPROFILE["MANA"] += 10
        CHARPROFILE["MAXSTAMINA"] += 5
        CHARPROFILE["STAMINA"] += 5
        break
    if CHARPROFILE["CLASS"] == "Desc":
        print("The Warrior has increased HP and ATK!\n",WarriorDesc,"\nThe Mage has increased MANA!\n",MageDesc,"\nThe Hunter has good overall stats!\n",HunterDesc)
        continue
    else:
        print("You need to pick from the given options!\n")
        continue

#character confirmation display
SPACER = "_________________________________"
print(SPACER)
print("\nYou are",CHARPROFILE["NAME"],", a",CHARPROFILE["RACE"],CHARPROFILE["CLASS"],".")
print("\nYour stats are:\n","HP:",CHARPROFILE["HP"],"\n","ATK:",CHARPROFILE["ATK"],"\n","MAX MANA:",CHARPROFILE["MAXMANA"],"\n","MAX STAMINA:",CHARPROFILE["MAXSTAMINA"])
print(SPACER)

#item data and Shop inventory
WOODENSWORD = {"NAME":'Wooden Sword',"ATK":5,"HP":0,"MANA":0,"PRICE":15,"TYPE":'Weapon'}
LEATHERSWORD = {"NAME":'Leather Sword',"ATK":15,"HP":0,"MANA":0,"PRICE":25,"TYPE":'Armor'}
LEATHERARMOR = {"NAME":'Leather Armor',"ATK":0,"HP":10,"MANA":0,"PRICE":25,"TYPE":'Armor'}
OAKTWIG = {"NAME":'Oak Twig',"ATK":0,"HP":0,"MANA":10,"PRICE":10,"TYPE":'Weapon'}
WEAPON = [WOODENSWORD,OAKTWIG]
ARMOR = [LEATHERARMOR,LEATHERSWORD]
SHOP = [WOODENSWORD,LEATHERARMOR,OAKTWIG,LEATHERSWORD]

#skill data
SWING = {"NAME":'Swing',"ATK":0,"MANACOST":1}
FIREBOLT = {"NAME":'Fire Bolt',"ATK":5,"MANACOST":15}

#enemy data
SLIME = {"NAME":'Slime',"HP":15,"ATK":3,"EXPDROP":1,"GOLDDROP":4}
ENEMY = {"NAME":'',"HP":0,"ATK":0,"EXPDROP":0,"GOLDDROP":0}

#character equipped items and inventory
CHARSKILLS = [SWING,FIREBOLT]
CHARINV = []
CHARHAND = {"NAME":'none',"ATK":0,"HP":0,"MANA":0}
CHARARMOR = {"NAME":'none',"ATK":0,"HP":0,"MANA":0}

#player level and exp
CHARLEVEL = 1
EXP = 0
EXPREQ = 5
STATPOINT = 0

#game start

while True:
#player game interface
    PLAYERCHOICE = input("Where would you like to go? (Shop/Battle/Inn/Inventory/Stats)\n")
#shop interface
    if PLAYERCHOICE == "Shop":
        while PLAYERCHOICE == "Shop":
            print(SPACER,"\n")
            print("GOLD:",CHARPROFILE["GOLD"])
            for x in SHOP:
                print("Price:",x["PRICE"],x["NAME"])
            print(SPACER)
            BUYING = input("'Welcome! What would you like to buy?'(Type Leave to leave shop)\n")
            for x in SHOP:
                if BUYING == x["NAME"]:
                    if CHARPROFILE["GOLD"] >= x["PRICE"]:
                        print("\n","ATK:",x["ATK"],"\n","HP:",x["HP"],"\n","MANA:",x["MANA"])
                        print("Would you like to buy",x["NAME"],"? (Yes/No)")
                        BUY = input("")
                        if BUY == "Yes":
                            print("You bought",x["NAME"],"!\n")
                            CHARPROFILE["GOLD"] += -x["PRICE"]
                            SHOP.remove (x)
                            CHARINV.append (x)
                            continue
                        if BUY == "No":
                            continue
                    if CHARPROFILE["GOLD"] < x["PRICE"]:
                        print("You don't have enough GOLD for that!")
                        continue
            if BUYING == "Leave":
                PLAYERCHOICE = ""
#battle interface
    if PLAYERCHOICE == "Battle":
        ENEMY["NAME"] = SLIME["NAME"]
        ENEMY["ATK"] += SLIME["ATK"]
        ENEMY["HP"] += SLIME["HP"]
        ENEMY["EXPDROP"] += SLIME["EXPDROP"]
        ENEMY["GOLDDROP"] += SLIME["GOLDDROP"]
        print("You encounter a",ENEMY["NAME"],"!")
        while PLAYERCHOICE == "Battle":
            print(SPACER,"\n")
            print("\n",CHARPROFILE["NAME"],"\n","HP:",CHARPROFILE["HP"],"MANA:",CHARPROFILE["MANA"],"/",CHARPROFILE["MAXMANA"])
            print("\n",ENEMY["NAME"],"\n","HP:",ENEMY["HP"])
            print("\n",SPACER)
            BATTLE = input("What do you do? (Run/Attack)\n")
            if BATTLE == "Attack":
                print(SPACER,"\n")
                for x in CHARSKILLS:
                    print(x["NAME"],"\n","MANA COST:",x["MANACOST"],"ATK:",CHARPROFILE["ATK"]+x["ATK"])
                print(SPACER)
                ATTACK = input("What will you do?\n")
                for x in CHARSKILLS:
                    if ATTACK == x["NAME"]:
                        if CHARPROFILE["MANA"] < x["MANACOST"]:
                            print("You don't have enough MANA!")
                            continue
                        if CHARPROFILE["MANA"] >= x["MANACOST"]:
                            print("You used",x["NAME"],"!")
                            CHARPROFILE["MANA"] += -x["MANACOST"]
                            ENEMY["HP"] += -CHARPROFILE["ATK"]+-x["ATK"]
                            if ENEMY["HP"] <= 0:
                                print(ENEMY["NAME"],"has been defeated!")
                                print("you gained",ENEMY["EXPDROP"],"EXP and",ENEMY["GOLDDROP"],"GOLD")
                                CHARPROFILE["GOLD"] += ENEMY["GOLDDROP"]
                                EXP += ENEMY["EXPDROP"]
                                if EXP >= EXPREQ:
                                    print("LEVEL UP")
                                    EXP = 0
                                    CHARLEVEL += 1
                                    STATPOINT += 5
                                    EXPREQ = CHARLEVEL*5
                                if STATPOINT > 0:
                                    print("You have unused Stat Points!")
                                ENEMY["NAME"] = ''
                                ENEMY["ATK"] = 0
                                ENEMY["HP"] = 0
                                ENEMY["EXPDROP"] = 0
                                ENEMY["GOLDDROP"] = 0
                                PLAYERCHOICE = ""
                                continue
                            print(ENEMY["NAME"],"attacks!")
                            CHARPROFILE["HP"] += -ENEMY["ATK"]
                            if CHARPROFILE["HP"] <= 0:
                                print("You black out and drop",CHARLEVEL*5,"gold!")
                                ENEMY["NAME"] = ''
                                ENEMY["ATK"] = 0
                                ENEMY["HP"] = 0
                                ENEMY["EXPDROP"] = 0
                                ENEMY["GOLDDROP"] = 0
                                CHARPROFILE["GOLD"] += -CHARLEVEL*5
                                print("You wake up back in town.")
                                CHARPROFILE["HP"] = CHARPROFILE["MAXHP"]
                                CHARPROFILE["MANA"] = CHARPROFILE["MAXMANA"]
                                CHARPROFILE["STAMINA"] = CHARPROFILE["MAXSTAMINA"]
                                PLAYERCHOICE = ""
                                continue
            if BATTLE == "Run":
                print("you run away!")
                ENEMY["NAME"] = ''
                ENEMY["ATK"] = 0
                ENEMY["HP"] = 0
                ENEMY["EXPDROP"] = 0
                ENEMY["GOLDDROP"] = 0
                PLAYERCHOICE = ""
                continue
#inn interface
    if PLAYERCHOICE == "Inn":
        while PLAYERCHOICE == "Inn":
            SLEEP = input("Would you like to rest at the Inn?(5 GOLD) (Yes/No)\n")
            if SLEEP == "Yes":
                if CHARPROFILE["GOLD"] < 5:
                    print("You don't have enough GOLD!")
                    SLEEP = "No"
                if CHARPROFILE["GOLD"] >= 5:
                    CHARPROFILE["GOLD"] += -5
                    CHARPROFILE["HP"] = CHARPROFILE["MAXHP"]
                    CHARPROFILE["MANA"] = CHARPROFILE["MAXMANA"]
                    CHARPROFILE["STAMINA"] = CHARPROFILE["MAXSTAMINA"]
                    print("You have recovered your HP, MANA, and STAMINA!")
                    SLEEP = "No"
            if SLEEP == "No":
                PLAYERCHOICE = ""
#inventory interface
    if PLAYERCHOICE == "Inventory":
        while PLAYERCHOICE == "Inventory":
            INVENTORY = input("What are you checking? (Equipped Items/All Items/Leave)\n")
            if INVENTORY == "All Items":
                print(SPACER)
                for x in CHARINV:
                    print(x["NAME"])
                print(SPACER)
                continue
            if INVENTORY == "Equipped Items":
                print("Current Weapon:",CHARHAND["NAME"])
                print("Current Armor:",CHARARMOR["NAME"])
                EQUIP = input("What would you like to change? (Weapon/Armor/Go Back)\n")
                if EQUIP == "Weapon":
                    for x in CHARINV:
                        if x["TYPE"] == "Weapon":
                            print(x["NAME"])
                            print("ATK:",x["ATK"])
                    EQUIPPING = input("Which weapon will you equip?\n")
                    for x in CHARINV:
                        if x["TYPE"] == "Weapon":
                            if x["NAME"] == EQUIPPING:
                                print("You equip",x["NAME"],".")
                                CHARINV.remove (x)
                                CHARPROFILE["HP"] += -CHARHAND["HP"]
                                CHARPROFILE["MAXHP"] += -CHARHAND["HP"]
                                CHARPROFILE["ATK"] += -CHARHAND["ATK"]
                                CHARPROFILE["MANA"] += -CHARHAND["MANA"]
                                CHARPROFILE["MAXMANA"] += -CHARHAND["MANA"]
                                for y in WEAPON:
                                    if y["NAME"] == CHARHAND["NAME"]:
                                        CHARINV.append (y)
                                CHARHAND["NAME"] = x["NAME"]
                                CHARHAND["ATK"] = x["ATK"]
                                CHARHAND["HP"] = x["HP"]
                                CHARHAND["MANA"] = x["MANA"]
                                CHARPROFILE["HP"] += CHARHAND["HP"]
                                CHARPROFILE["MAXHP"] += CHARHAND["HP"]
                                CHARPROFILE["ATK"] += CHARHAND["ATK"]
                                CHARPROFILE["MANA"] += CHARHAND["MANA"]
                                CHARPROFILE["MAXMANA"] += CHARHAND["MANA"]
                                PLAYERCHOICE = ""
                                continue
                if EQUIP == "Armor":
                    for x in CHARINV:
                        if x["TYPE"] == "Armor":
                            print(x["NAME"])
                            print("HP:",x["HP"])
                    EQUIPPING = input("Which armor will you equip?\n")
                    for x in CHARINV:
                        if x["TYPE"] == "Armor":
                            if x["NAME"] == EQUIPPING:
                                print("You equip",x["NAME"],".")
                                CHARINV.remove (x)
                                CHARPROFILE["HP"] += -CHARARMOR["HP"]
                                CHARPROFILE["MAXHP"] += -CHARARMOR["HP"]
                                CHARPROFILE["ATK"] += -CHARARMOR["ATK"]
                                CHARPROFILE["MANA"] += -CHARARMOR["MANA"]
                                CHARPROFILE["MAXMANA"] += -CHARARMOR["MANA"]
                                for y in ARMOR:
                                    if y["NAME"] == CHARARMOR["NAME"]:
                                        CHARINV.append(y)
                                CHARARMOR["NAME"] = x["NAME"]
                                CHARARMOR["ATK"] = x["ATK"]
                                CHARARMOR["HP"] = x["HP"]
                                CHARARMOR["MANA"] = x["MANA"]
                                CHARPROFILE["HP"] += CHARARMOR["HP"]
                                CHARPROFILE["MAXHP"] += CHARARMOR["HP"]
                                CHARPROFILE["ATK"] += CHARARMOR["ATK"]
                                CHARPROFILE["MANA"] += CHARARMOR["MANA"]
                                CHARPROFILE["MAXMANA"] += CHARARMOR["MANA"]
                                PLAYERCHOICE = ""
                                continue
                if EQUIP == "Go Back":
                    continue
            if INVENTORY == "Leave":
                PLAYERCHOICE = ""
                continue
#stat interface (reworking)
    if PLAYERCHOICE == "Stats":
        while PLAYERCHOICE == "Stats":
            STATS = input("Would you like to display your Stats or allocate Stat Points? (Display/Allocate/Leave)\n")
            if STATS == "Display":
                print(SPACER)
                print("\n",CHARPROFILE["NAME"])
                print("",CHARPROFILE["RACE"],CHARPROFILE["CLASS"])
                print("\n","Level:",CHARLEVEL,"\n EXP:",EXP,"/",EXPREQ,"\n Stat Points:",STATPOINT)
                print("\n","GOLD:",CHARPROFILE["GOLD"],"\n","Current Weapon:",CHARHAND["NAME"],"\n","Current Armor:",CHARARMOR["NAME"])
                print("\n","HP:",CHARPROFILE["HP"],"/",CHARPROFILE["MAXHP"],"\n","ATK:",CHARPROFILE["ATK"],"\n","MANA:",CHARPROFILE["MANA"],"/",CHARPROFILE["MAXMANA"],"\n","STAMINA:",CHARPROFILE["STAMINA"],"/",CHARPROFILE["MAXSTAMINA"])
                print(SPACER,"\n")
                PLAYERCHOICE = ""
                continue
            if STATS == "Allocate":
                while STATS == "Allocate":
                    print(SPACER,"\n")
                    print("Stat Points:",STATPOINT)
                    print("HP:",CHARPROFILE["MAXHP"])
                    print("ATK:",CHARPROFILE["ATK"])
                    print("MANA:",CHARPROFILE["MAXMANA"])
                    print("STAMINA:",CHARPROFILE["MAXSTAMINA"])
                    print(SPACER)
                    ALLOCATEABLE = ("HP","ATK","MANA","STAMINA","Leave")
                    ALLOCATE = input("What Stat would you like to improve? (HP/ATK/MANA/STAMINA/Leave)\n")
                    if ALLOCATE in ALLOCATEABLE:
                        if ALLOCATE == "HP":
                            print("Stat Points:",STATPOINT)
                            print("How many Stat Points will go into",ALLOCATE,"?")
                            ALLOCATING = input("")
                            try:
                                ALLOCATING = int(ALLOCATING)
                            except ValueError:
                                print("Please use a valid number!")
                                continue
                            if STATPOINT < ALLOCATING:
                                print("You don't have enough Stat Points!")
                                continue
                            if STATPOINT >= ALLOCATING:
                                print("You increased",ALLOCATE,"by",ALLOCATING,"!")
                                STATPOINT += -ALLOCATING
                                CHARPROFILE["HP"] += ALLOCATING
                                CHARPROFILE["MAXHP"] += ALLOCATING
                                continue
                        if ALLOCATE == "ATK":
                            print("Stat Points:",STATPOINT)
                            print("How many Stat Points will go into",ALLOCATE,"?")
                            ALLOCATING = input("")
                            try:
                                ALLOCATING = int(ALLOCATING)
                            except ValueError:
                                print("Please use a valid number!")
                                continue
                            if STATPOINT < ALLOCATING:
                                print("You don't have enough Stat Points!")
                                continue
                            if STATPOINT >= ALLOCATING:
                                print("You increased",ALLOCATE,"by",ALLOCATING,"!")
                                STATPOINT += -ALLOCATING
                                CHARPROFILE["ATK"] += ALLOCATING
                                continue
                        if ALLOCATE == "MANA":
                            print("Stat Points:",STATPOINT)
                            print("How many Stat Points will go into",ALLOCATE,"?")
                            ALLOCATING = input("")
                            try:
                                ALLOCATING = int(ALLOCATING)
                            except ValueError:
                                print("Please use a valid number!")
                                continue
                            if STATPOINT < ALLOCATING:
                                print("You don't have enough Stat Points!")
                                continue
                            if STATPOINT >= ALLOCATING:
                                print("You increased",ALLOCATE,"by",ALLOCATING,"!")
                                STATPOINT += -ALLOCATING
                                CHARPROFILE["MANA"] += ALLOCATING
                                CHARPROFILE["MAXMANA"] += ALLOCATING
                                continue
                        if ALLOCATE == "STAMINA":
                            print("Stat Points:",STATPOINT)
                            print("How many Stat Points will go into",ALLOCATE,"?")
                            ALLOCATING = input("")
                            try:
                                ALLOCATING = int(ALLOCATING)
                            except ValueError:
                                print("Please use a valid number!")
                                continue
                            if STATPOINT < ALLOCATING:
                                print("You don't have enough Stat Points!")
                                continue
                            if STATPOINT >= ALLOCATING:
                                print("You increased",ALLOCATE,"by",ALLOCATING,"!")
                                STATPOINT += -ALLOCATING
                                CHARPROFILE["STAMINA"] += ALLOCATING
                                CHARPROFILE["MAXSTAMINA"] += ALLOCATING
                                continue
                        if ALLOCATE == "Leave":
                            STATS = ""
                            PLAYERCHOICE = ""
                            continue
                    else:
                        continue
            if STATS == "Leave":
                PLAYERCHOICE = ""
                continue
#emergency break
    if PLAYERCHOICE == "Break":
        break
