#!/usr/bin/env python
import libcatan

tokens = "abcdefghijklmnopqr"
resources = ["Brick,","Lumber","Ore","Sheep","Wheat","Unknown"]

newgame = libcatan.CatanGame()
print "Input player names in turn order:"
i = 0
names = []
while i < 4:
    name = raw_input("Player #"+str(i+1)+":")
    names.append(name)
    i+=1

newgame.setOrder(names)

def bold(string):
    bold = "\033[1m"
    reset = "\033[0;0m"
    return bold + string + reset

def extend(instring, checklist):
    if instring == "":
        return ""
    for word in checklist:
        if word.lower().startswith(instring.lower()):
            return word
    return ""

print "Input elements under letter markers."
elements = []
for character in tokens:
    element = raw_input( "Resource under token "+str(character)+" :")
    while extend(element, resources) == "":
        print bold("B")+"ricks "+bold("L")+"umber "+bold("O")+"re "+bold("S")+"heep "+bold("W")+"heat"
        element = raw_input( "Resource under token "+str(character)+" :")
    element = extend(element, resources)
    print "Marking "+character+" as "+element
    elements.append(element)
newgame.board.setBoard(elements)

print "Board and four players initialized"

# First rotation
for player in newgame.players:
    # First road
    player.recieveRoad(True)
    print "For player "+player.name
    # First settlement
    coords = raw_input(player.name+"'s first settlement coords:")
    porttype = raw_input("Port type: BLOSWU for element")
    player.recieveSettlement(coords,porttype)

# Reverse rotation
for player in reversed(newgame.players):
    print "For player "+player.name
    coords = raw_input("Second settlement coords")
    porttype = raw_input("Port type: BLOSW for element, enter for none")
    road_extension = input("Is the road an extension? True/False")
    player.recieveRoad(True)
    player.recieveSettlement(coords,porttype)
    
    #Second settlement income
    for character in coords:
        player.deltaResource(newgame.board.element[character],1)    
    
    player.recieveRoad(True)
    print "For player "+player.name
    coords = raw_input("First settlement coords")
    porttype = raw_input("Port type: BLOSWU for element")
    player.recieveSettlement(coords,porttype)


# Second road - could be extension
# Game loop:
# Roll
# Trade
# Build

for player in newgame.players:
    player.recieveSettlement("ekf")
    print "player "+player.name+" recieved settlement ekf"

newgame.income(8)
def printState():
    for player in newgame.players:
        print player.shortScore()
print "defined printState()"
printState()
