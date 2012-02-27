import random


class Soldier:
    def __init__(self):
        self.name = "Soldier"

    def invoke(self, player, target):
        pass
        #Game effect goes here

class VictoryPointCard:
    def __init__(self):
        self.name = "Victory Point"

    def invoke(self, player):
        pass
        #Game effect goes here

class MonopolyCard:
    def __init__(self):
        self.name = "Monopoly"

    def invoke(self, player):
        pass
        #Game effect goes here

class YearofPlentyCard:
    def __init__(self):
        self.name = "Year of Plenty"

    def invoke(self, player):
        pass
        #Game effect goes here

class RoadBuildingCard:
    def __init__(self):
        self.name = "Road Building"

    def invoke(self, player):
        pass
        #Game effect goes here

class Building:
    def __init__(self,markers):
        self.markers = []
        for marker in markers:
            self.markers.append(marker)
        self.size = 1

    def getCoords(self):
        return self.markers

    def upgrade(self):
        self.size = self.size+1

class Port:
    def __init__(self, variety):
        self.variety = type
        if (variety=="Generic"):
            self.ratio = 3
        else:
            self.ratio = 2

class ResourceCard:
    def __init__(self, element):
        self.element = element

class Player:
    def __init__(self,name):
        self.name = name
        
        self.Resources = {"Brick":0,"Lumber":0,"Ore":0,"Sheep":0,"Wheat":0,"Unknown":0}
        
        self.DevelopmentCards = []
        
        self.Buildings = {}
        
        self.Ports = []
        
        self.roadlength = 0

        self.army = 0

    def shortScore(self):
        prefixes = ["B:","L:","O:","S:","W:","U:"]
        line = self.name + "\n"
        i = 0
        for key in self.Resources:
            line = line +key+str(self.Resources[key])+"|"
            i+=1

        line = line + "Rd:" + str(self.roadlength) + "|Sl:" + str(self.army)
        return line

    def income(self,markers,board):
        for character in markers:
            for key in self.Buildings:
                if (key.count(character)>0):
                    self.deltaResource(board.element[character],self.Buildings[key].size)

    def deltaResource(self,element,amount):
        self.Resources[element] = self.Resources[element] + amount
    
    def recieveSettlement(self, markers, portType="none"):
        constructed = Building(markers)
        self.Buildings[markers]=constructed
        if (self.Ports.count(portType) and portType!="none"):
            self.Ports.append(portType)

    def recieveCity(self,markers):
        self.Buildings[markers].upgrade()
    
    def recieveRoad(self,extension=False):
        if (extension==True):
            self.RoadLength = self.roadlength + 1

    def recieveDevelopmentCard(self, card):
        self.DevelopmentCards.append(card)

    def recieveSoldier():
        self.army = self.army+1
    
    def loseSoldier():
        self.army = self.army-1
    
    def roll(self):
        return roll()
    
    def randomCard(self):
        for resource in self.Resources:
            total = total+resource
        
        selection = random.randint(1,total)
    
        for resource in self.Resources:
            if selection < Resources[resource]:
                return resource
            else:
                selection = selection - Resources[resource]
    
    def playerTrade(self, giveElement, giveAmount, target, recieveElement,
                    recieveAmount):
        self.deltaResource(giveElement,-giveAmount)
        self.deltaResource(recieveElement,recieveAmount)
        self.deltaResource(giveElement,giveAmount)
        self.deltaResource(recieveElement,-recieveAmount)

class Board:
    def __init__(self):
        self.element = {}
        self.robberPosition = " "

    def setBoard(self,elements):
        i = 0
        for character in "abcdefghijklmnopqr":
            self.element[character]=elements[i]
            i = i+1

        self.rolls = {
            2:"b",
            3:"dq",
            4:"jn",
            5:"ao",
            6:"cp",
            8:"ek",
            9:"gm",
            10:"fl",
            11:"ir",
            12:"h"}

    def setRobber(self,position):
        self.robberPosition = position
    
    def getresource(position):
        if (self.robberPosition == position):
            return ("Unknown", "0")
        else:
            return (self.element[position])

    def getMarkers(self,number):
        return self.rolls[number].replace(self.robberPosition,'')
        



class developmentDeck:
    def __init__(self):
        self.total = {"Soldier":14,
                      "Victory Point":5,
                      "Monopoly":2,
                      "Year of Plenty":2,
                      "Road Building":2,}

class CatanGame:
    def __init__(self):
        self.players=[]
        self.board = Board()
        self.deck = developmentDeck()
    
    def setOrder(self,names):
        for name in names:
            self.players.append(Player(name))

    def invokeRobber(self,player,marker,target,element):
        self.board.setRobber(marker)
        player.deltaResource(element,1)
        target.deltaResource(element,-1)

    def roll(self):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        return d1+d2

    def income(self,number):
        markers = self.board.getMarkers(number) 
        for player in self.players:
            player.income(markers,self.board)
