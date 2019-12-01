#   superHero_Record.py
#   Author:         Naphatsakorn Khotsombat
#   Description:    this program will give the user option to add hero into the record and an option to view the record.

programOn = True
numHeroDC = 0
numHeroMC = 0
totalNumHero = 0
heroName = " "
longestName = " "
shortestName = " "

while programOn:
    heroFileDC = open("dc_comics.txt", 'w')
    heroFileMC = open("marvel_comics.txt", 'w')
    try:
        while True:
            try:
                mainChoice = int(input("\n1: Add a new Hero"
                                       "\n2: View details of a hero"
                                       "\n3: Quit"
                                       "\n>>>"))
                break
            except ValueError:
                print("Must be a number!")
        if mainChoice == 1:
            heroName = input("What is your hero name?\t")
            if len(longestName) < len(heroName):
                longestName = longestName + heroName
            if len(shortestName) > len(heroName):
                shortestName = shortestName + heroName
            heroAlias = input("Also known as?\t")
            heroPower = input("Describe your power?\t")
            while True:
                heroFrom = 0
                try:
                    heroFrom = int(input('Are you'
                                         '\n1: form Earth'
                                         '\n2: not from Earth'
                                         '\n>>>'))
                    if heroFrom == 1:
                        heroIcon = "Human"
                        break
                    elif heroFrom == 2:
                        heroIcon = "Alien"
                        break
                    else:
                        print("Not one of the option!")
                except ValueError:
                    print("Must be a number!")
            while True:
                heroUniverse = 0
                while True:
                    try:
                        heroUniverse = int(input("Are you from"
                                                 "\n1: DC"
                                                 "\n2: Marvel Comics"
                                                 "\n>>>"))
                        break
                    except ValueError:
                        print("Must be a number!")

                if heroUniverse == 1:
                    print(f"{heroName}", file=heroFileDC)
                    numHeroDC += 1
                    break
                elif heroUniverse == 2:
                    print(f"{heroName}", file=heroFileMC)
                    numHeroMC += 1
                    break
                else:
                    print("Not one of the option!")

            newHeroFile = open(f"{heroName}.txt", 'w')
            print(f"{heroIcon}\n{heroName}\n{heroPower}\n{heroAlias}", file=newHeroFile)
            newHeroFile.close()

        elif mainChoice == 2:
            heroFileDC.close()
            heroFileMC.close()

            while True:
                universeChoice = 0
                while True:
                    try:
                        universeChoice = int(input("1: DC"
                                                   "\n2: Marvel Comics"
                                                   "\n>>>"))
                        break
                    except ValueError:
                        print("Must be a number!")

                print('Please choose from the following heroes:'
                      '\n========================================')
                if universeChoice == 1:
                    while True:
                        heroListDC = open("dc_comics.txt", 'r')
                        for line in heroListDC:
                            print(">>>  ", line.rstrip())
                        break
                elif universeChoice == 2:
                    while True:
                        heroListMC = open("marvel_comics.txt", 'r')
                        for line in heroListMC:
                            print(">>>  ", line.rstrip())
                        break
                if universeChoice == 1 or universeChoice == 2:
                    heroChoice = input("Which hero?\t")
                    try:
                        with open(f"{heroChoice}.txt", 'r') as heroDetail:
                            print("===========================================")
                            heroInfo = heroDetail.readline().rstrip()
                            print(heroInfo)
                            heroInfo = heroDetail.readline().rstrip()
                            print("Name:\t", heroInfo)
                            heroInfo = heroDetail.readline().rstrip()
                            print("Power:\t", heroInfo)
                            heroInfo = heroDetail.readline().rstrip()
                            print("AKS:\t", heroInfo)
                            print("==========================================")
                        break
                    except IOError:
                        print(f"The superhero \'{heroChoice}\' is not in our records. Please"
                              f"\ncheck that you have typed this properly and try again...")

        elif mainChoice == 3:
            heroFileDC.close()
            heroFileMC.close()

            totalNumHero = int(numHeroDC + numHeroMC)
            percentDC = (numHeroDC / totalNumHero) * 100
            percentMC = (numHeroMC / totalNumHero) * 100
            print(type(totalNumHero))
            print(f"There are {totalNumHero:d} on record."
                  f"\nDC heroes make up {percentDC:.f}% and Marvel Comics heroes make up {percentMC:.f}% "
                  f"\nof the {totalNumHero} heroes"
                  f"\nShortest name(s): {shortestName}"
                  f"\nLongest name(s): {longestName}"
                  f"\n\nBye Bye \U0001F44B and Thank You ")
            programOn = False
        else:
            print("Not one of the option!")

    except ZeroDivisionError:
        print("Must have at least 1 only from both Universe")
