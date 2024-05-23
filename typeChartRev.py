class MoreThanSixError(Exception):
    def __init__(self, value):
        self.value = value

class TypeNotFoundError(Exception):
    def __init__(self, value):
        self.value = value

class InavlidNumTypesError(Exception):
    def __init__(self, value):
        self.value = value

fullTypeList = ['Normal', 'Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy']

numPkmn = int(input('How many Pokemon are in your party? '))

if numPkmn > 6:
    raise MoreThanSixError('The maximum number of party members is 6.')
else:
    pass

print("For the following questions, type your Pokemon's type(s) separated by ONLY a space.")
print("Type Q to quit.")
nameList = []
partyTypeList = []
abilityList = []
for pkmn in range(1, numPkmn + 1):
    name = input(f"Pokemon {pkmn}'s Name: ").title()
    if name[0] == "Q":
        exit()
    type = input('Pokemon Type: ').title().split()
    if type[0] == "Q":
        exit()
    if len(type) == 1:
        if type[0] not in fullTypeList:
            raise TypeNotFoundError('Pokemon type not found.')
            exit()
    elif len(type) == 2:
        if (type[0] not in fullTypeList) or (type[1] not in fullTypeList):
            raise TypeNotFoundError('Pokemon type not found.')
            exit()
    else:
        raise InavlidNumTypesError('Number of types is invalid.')
    
    #ability = input('Ability: ').title()

    nameList.append(name)
    partyTypeList.append(type)
    #abilityList.append(ability)

fullPartyMatchups = []

for typeCombo in partyTypeList:
    typeMatchups = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for specificType in typeCombo:
        if specificType == 'Normal':
            resists = []
            weaknesses = ['Fighting']
            immunities = ['Ghost']
        elif specificType == 'Fire':
            resists = ['Fire', 'Grass', 'Ice', 'Bug', 'Steel', 'Fairy']
            weaknesses = ['Water', 'Ground', 'Rock']
            immunities = []
        elif specificType == 'Water':
            resists = ['Fire', 'Water', 'Ice', 'Steel']
            weaknesses = ['Grass', 'Electric']
            immunities = []
        elif specificType == 'Grass':
            resists = ['Water', 'Grass', 'Electric', 'Ground']
            weaknesses = ['Fire', 'Ice', 'Poison', 'Flying', 'Bug']
            immunities = []
        elif specificType == 'Electric':
            resists = ['Electric', 'Flying', 'Steel']
            weaknesses = ['Ground']
            immunities = []
        elif specificType == 'Ice':
            resists = ['Ice']
            weaknesses = ['Fire', 'Fighting']
            immunities = []
        elif specificType == 'Fighting':
            resists = ['Bug', 'Rock', 'Dark']
            weaknesses = ['Flying', 'Psychic', 'Fairy']
            immunities = []
        elif specificType == 'Poison':
            resists = ['Grass', 'Fighting', 'Poison', 'Bug', 'Fairy']
            weaknesses = ['Ground', 'Psychic']
            immunities = []
        elif specificType == 'Ground':
            resists = ['Poison', 'Rock']
            weaknesses = ['Water', 'Grass', 'Ice']
            immunities = ['Electric']
        elif specificType == 'Flying':
            resists = ['Grass', 'Fighting', 'Bug']
            weaknesses = ['Electric', 'Ice', 'Rock']
            immunities = ['Ground']
        elif specificType == 'Psychic':
            resists = ['Fighting', 'Psychic']
            weaknesses = ['Bug', 'Ghost', 'Dark']
            immunities = []
        elif specificType == 'Bug':
            resists = ['Grass', 'Fighting', 'Ground']
            weaknesses = ['Fire', 'Flying', 'Rock']
            immunities = []
        elif specificType == 'Rock':
            resists = ['Normal', 'Fire', 'Poison', 'Flying']
            weaknesses = ['Water', 'Grass', 'Fighting', 'Ground', 'Steel']
            immunities = []
        elif specificType == 'Ghost':
            resists = ['Poison', 'Bug']
            weaknesses = ['Ghost', 'Dark']
            immunities = ['Normal', 'Fighting']
        elif specificType == 'Dragon':
            resists = ['Fire', 'Water', 'Grass', 'Electric']
            weaknesses = ['Ice', 'Dragon', 'Fairy']
            immunities = []
        elif specificType == 'Dark':
            resists = ['Ghost', 'Dark']
            weaknesses = ['Fighting', 'Bug', 'Fairy']
            immunities = ['Psychic']
        elif specificType == 'Steel':
            resists = ['Normal', 'Grass', 'Ice', 'Flying', 'Psychic', 'Bug', 'Rock', 'Dragon', 'Steel', 'Fairy']
            weaknesses = ['Fire', 'Fighting', 'Ground']
            immunities = ['Poison']
        elif specificType == 'Fairy':
            resists = ['Fighting', 'Bug', 'Dark']
            weaknesses = ['Poison', 'Steel']
            immunities = ['Dragon']

        for pos in range(len(fullTypeList)):
            if fullTypeList[pos] in resists:
                typeMatchups[pos] *= 0.5
            elif fullTypeList[pos] in weaknesses:
                typeMatchups[pos] *= 2
            elif fullTypeList[pos] in immunities:
                typeMatchups[pos] *= 0
    fullPartyMatchups.append(typeMatchups)

print('  < Types >  ', end = '')
for type in fullTypeList:
    print('|', end = '')
    print(type, end = '')
    print('|', end = ' ')
print()

print('  ' + ('-' * 160))

pkmnNum = 0
for pkmn in nameList:
    print(f'{pkmn:<16}', end = '')
    print(f'{fullPartyMatchups[pkmnNum][0]:>2}', end = '')
    print(f'{fullPartyMatchups[pkmnNum][1]:>8}', end = '')
    print(f'{fullPartyMatchups[pkmnNum][2]:>7}', end = '')
    print(f'{fullPartyMatchups[pkmnNum][3]:>8}', end = '')
    print(f'{fullPartyMatchups[pkmnNum][4]:>10}', end = '')
    print(f'{fullPartyMatchups[pkmnNum][5]:>8}', end = '')
    print(f'{fullPartyMatchups[pkmnNum][6]:>9}', end = '')
    print(f'{fullPartyMatchups[pkmnNum][7]:>9}', end = '')
    print(f'{fullPartyMatchups[pkmnNum][8]:>10}', end = '')
    print(f'{fullPartyMatchups[pkmnNum][9]:>9}', end = '')
    print(f'{fullPartyMatchups[pkmnNum][10]:>9}', end = '')
    print(f'{fullPartyMatchups[pkmnNum][11]:>8}', end = '')
    print(f'{fullPartyMatchups[pkmnNum][12]:>7}', end = '')
    print(f'{fullPartyMatchups[pkmnNum][13]:>7}', end = '')
    print(f'{fullPartyMatchups[pkmnNum][14]:>9}', end = '')
    print(f'{fullPartyMatchups[pkmnNum][15]:>8}', end = '')
    print(f'{fullPartyMatchups[pkmnNum][16]:>7}', end = '')
    print(f'{fullPartyMatchups[pkmnNum][17]:>8}')
    pkmnNum += 1
