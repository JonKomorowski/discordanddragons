import random
#both PCs and NPCs are characters
class Character(object):
    #Constructor
    def __init__(self,name,charClass,race,maxHitPoints, currHitPoints,inventory,weapon,status,position,initiative):
        self.name = name                #name
        self.charClass = charClass      #character's class expressed as tuple containing string of class and class level
        self.race = race                #character's race
        self.maxHitPoints = max         #maximum hitpoints
        self.currHitPoints = hitPoints  #current hitpoints
        self.inventory = inventory      #inventory
        self.weapon = weapon            #weapon equipped by character
        self.status = status            #concious, unconcious, dead, status ailements eventually
        self.position = position        #tuple for xy coordinates on grid
        self.initiative = initiative    #initiative when in combat
        self.strength = strength        #str
        self.dexterity = dexterity      #dex
        self.constitution = constitution#con
        self.intelligence = intelligence#int
        self.wisdom = wisdom            #wis
        self.charisma = charisma        #char
    #########
    #Methods#
    #########
    '''
    method to roll dice
    die is type of dice
    num is how many
    eg 2d6 => roll(2,6)
    add modifiers on the backend
    '''
    def roll(num, die):
        result = 0
        for i in range(num):
            result += random.randint(1,die)
        return result
    #method to take damage
    def takeDamage(damage):
        return self.CurrHitPoints - damage
    #method that changes status of character
    def changeStatus(damage):
        if self.currHitPoints - damage == 0:
            self.status = unconcious
        elif self.currHitPoints - damage < 0:
            self.status = dying
        elif damage >= self.maxHitPoints*2:
            self.status = dead
#player character that inherits from Character class
class PC(Character):
    #Constructor
    def __init__(self,deathSaves):
        super(PC, self).__init__(name)
        #Character.name = name
        self.deathSaves = deathSaves #Death saving throws

'''
Test zone below to make sure stuff works
'''
#plainJane = PC("Jane",("fighter", 1), "Human", 1,1,None,"Bare Hands", "conscious", (0,0), 1,1)
#plainJane = PC("jane",0)
