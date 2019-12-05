#!/usr/bin/python3
import requests

def pokemonCSVEntry(dexNum):
    url = 'https://pokeapi.co/api/v2/pokemon-species/' + \
        str(dexNum) + '/'  # url that can be changed
    secondUrl = 'https://pokeapi.co/api/v2/pokemon/' + str(dexNum) + '/'
    response1, response2 = requests.get(url), requests.get(secondUrl)
    convertToPy1, convertToPy2 = response1.json(), response2.json()
    name = convertToPy1['name'].title()
    Types = []
    for Type in range(len(convertToPy2['types'])):
        Types.append(convertToPy2['types'][Type]['type']['name'])
    Types.reverse()
    if len(Types) == 2:
        typeStr = Types[0].title() + ',' + Types[1].title()
    else:
        typeStr = Types[0].title() + ','
    stats = convertToPy2['stats']
    statList = []
    for stat in range(len(stats)):
        statList.append(stats[stat]['base_stat'])
    baseStat = str(sum([int(num) for num in statList]))
    statList = [str(num) for num in statList]
    HP, Attack, Def, spAtk, spDef, speed = \
    statList[5], statList[4], statList[3], statList[2], statList[1], statList[0]
    abilities = convertToPy2['abilities']
    listofabilities = []
    for ability in range(len(abilities)):
        listofabilities.append(
            abilities[ability]['ability']['name'].title().replace('-', ' '))
    listofabilities.reverse()
    if len(listofabilities) == 3:
        abilitiesStr = listofabilities[0] + ',' + listofabilities[1] + ',' + \
        listofabilities[2]
    elif len(listofabilities) == 2:
        abilitiesStr = listofabilities[0] + ',' + listofabilities[1] + ','
    else:
        abilitiesStr = listofabilities[0] + ',,'
    generation = convertToPy1['generation']['name']
    dexNum = str(dexNum)
    result = dexNum + ',' + name + ',' + typeStr + ',' + baseStat + ',' + HP + ',' + \
    Attack + ',' + Def + ',' + spAtk + ',' + spDef + ',' + speed + \
    ',' + abilitiesStr + ',' + generation + ',' + 'FALSE' +  ',' + 'FALSE'
    return result

def main():
    result = '#,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk' + \
        ',Sp. Def,Speed,Ability1,Ability2,Ability3,Generation' + \
        ',Legendary,Mythical\n'
    index = 1
    while (index < 808):
        result += pokemonCSVEntry(index) + '\n'
        index+=1
    print(result)

if __name__ == "__main__":
    main()
