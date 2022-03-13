#import climage
import colorama
import time

from src.people import *
from src.building import *
from src.input import *
from colorama import Fore, Back, Style
import os
#from replay import *

class Building():
    def __init__(self,id,x,y,h,d): #(self, id, health,x,y):
        self.id = id
        self.x = x
        self.y = y
        self.health = h
        self.damage = d

class Thall(Building):      #health = 100
    def __init__(self,id,x,y,h=120,d=0): #(self,id,x,y)
        Building.__init__(self,id,x,y,h,d)
    health = 120

#

class Wall(Building):
    def __init__(self,id,x,y,h=30,d=0):
        Building.__init__(self,id,x,y,h,d)


class Hut(Building):
    def __init__(self,id,x,y,h=75,d=0):
        Building.__init__(self,id,x,y,h,d)


class Cannon(Building):
    def __init__(self,id,x,y,h=100,d=1,r=6,a=0):#(self, id, health,x,y,damage,range,attack)
        Building.__init__(self,id,x,y,h,d)
        self.range = r
        self.attack = a

class Person():
    def __init__(self,id,x,y,ms,h,d): #(self, id, health)
        self.id = id
        self.x = x
        self.y = y
        self.movement = ms
        self.health = h
        self.damage = d

a = Back.CYAN
b = Style.RESET_ALL
normal = "|_|"
keyused = 0

class King(Person):
    def __init__(self,id,x,y,sym,ms=1,h=120,d=1): #(self, id, health, damage, x, y, prev,movement):
        Person.__init__(self,id,x,y,ms,h,d)
        self.sym = sym
    # damage = 1
    def healthline(self):
        total = self.health
        fraction = total/4
        print("Kings HealthLine <=======>|",end = " ")
        count = 1
        while(fraction >= count):    
            print(a+" ",end = " ")
            print(b,end = "")
            count = count + 1
        while(count <=25):
            print(" ",end = "")
            count = count + 1
        print("\n")

class Barbarians(Person):
    def __init__(self,id,x,y,tx,ty,ms,h,d,sym): #(self, id, health, damage,x,y,tx,ty,prev,movement):
        Person.__init__(self,id,x,y,ms,h,d)
        self.tx = tx
        self.ty = ty
        self.sym = sym
        # self.damage = damage
        # self.x = x
        # self.y =y
        # self.tx = tx
        # self.ty = ty
        # self.prev = prev
        # self.movement = movement

# class Spells():
#     def _init_(self,id,cover):
#         self.id = id


csi = "\u001b["
BuildingsTotal = []
red = csi + "41m"
yellow = csi +"43m"
green = csi +"42m"
end = csi + "0m"
Thalls = []
kingcount = 0
Positions = []
Barbarbots = []
Huts = []
Walls = []
Cannons = []
replay = []
colors = []
h_flag = 0
r_flag = 0
Endgame = 0
for i in range(12):
    string = "Thallno" + str(i)
    quo = i // 3
    rem = i % 3
    obj = Thall(string,11+quo,11+rem)
    Thalls.append(obj)
    BuildingsTotal.append(obj)
    # print(Thalls[i].id)

for i in range(3):
    string = "Hutno" + str(i)
    obj = Hut(string,i+1,i+1)
    Huts.append(obj)
    BuildingsTotal.append(obj)

string = "Hutno" + str(3)
obj = Hut(string,1,0)
Huts.append(obj)
BuildingsTotal.append(obj)

string = "Hutno" + str(4)
obj = Hut(string,0,1)
Huts.append(obj)
BuildingsTotal.append(obj)



string = "Canno" + str(0)
obj = Cannon(string,0,0)
Cannons.append(obj)
BuildingsTotal.append(obj)

string = "Canno" + str(0)
obj = Cannon(string,8,12)
Cannons.append(obj)
BuildingsTotal.append(obj)

string = "Canno" + str(0)
obj = Cannon(string,12,16)
Cannons.append(obj)
BuildingsTotal.append(obj)

string = "Canno" + str(0)
obj = Cannon(string,12,7)
Cannons.append(obj)
BuildingsTotal.append(obj)

string = "Canno" + str(0)
obj = Cannon(string,20,12)
Cannons.append(obj)
BuildingsTotal.append(obj)

symk = "|_|"
king = King("Simba",20,15,symk)

totalpos = 26
n = totalpos
m = totalpos
last_key = ''


# king = King("King", 100, 5, 20, 15, prev,1)

def spawn_king():
    norm = "|_|"
    Positions[20][15] = "|K|"
    king.sym = norm
    # king.health = 120


def kingmoves(key):
    symbio = king.sym
    if king.health <= 0:
        return
    Positions[king.x][king.y] = symbio
    if (key == 'W' or key == 'w'):
        king.x -= king.movement
        last_key = 'w'
    if key == 'S' or key == 's':
        king.x += king.movement
        last_key = 's'
    if key == 'A' or key == 'a':
        king.y -= king.movement
        last_key = 'a'
    if key == 'D' or key == 'd':
        last_key = 'd'
        king.y += king.movement

    if king.x > 25:
        king.x = 25    
    normal = "|_|"
    if king.x < 0:
        king.x = 0
    kins = "|K|"
    if king.y < 0:
        king.y = 0
    norm = "|_|"
    if king.y > 25:
        king.y = 25
    
    
    if Positions[king.x][king.y] == normal:
        king.sym = Positions[king.x][king.y]
        Positions[king.x][king.y] = kins
    else:
        if key == 'W' or key == 'w':
            king.x = king.x + king.movement
        if key == 'S' or key == 's':
            king.x = king.x - king.movement
        if key == 'A' or key == 'a':
            king.y = king.y + king.movement
        if key == 'D' or key == 'd':
            king.y = king.y - king.movement
        Positions[king.x][king.y] = kins

def kingfight():
    dmg = king.damage
    if king.health <= 0:
        return
    minik = 0
    hlt = king.health
    norm = "|_|"
    if last_key == 'w' and hlt >= 0 :
        kins = "|K|"
        for i in range(len(BuildingsTotal)):
            dest = 0
            if BuildingsTotal[i].id[0] != 'T' and minik == 0 and BuildingsTotal[i].health > 0 and hlt >=0 :
                if BuildingsTotal[i].x == king.x-1 and hlt >=0 and BuildingsTotal[i].y == king.y and kins != norm:
                    if BuildingsTotal[i].health > king.damage and dmg > -1 and kins != norm:
                        BuildingsTotal[i].health = BuildingsTotal[i].health - king.damage
                    else:
                        dest += 1 
                        BuildingsTotal[i].health = 0
                        BuildingsTotal[i].health = BuildingsTotal[i].health * minik
                        Positions[BuildingsTotal[i].x][BuildingsTotal[i].y] = norm 
            elif Thall.health > 0 and hlt >=0: 
                if (king.y == 11 or king.y == 12 or king.y == 13) and kins != norm and (king.x == 15) and minik ==0:
                    if Thall.health > king.damage and hlt >=0 and kins != norm and BuildingsTotal[i].x == king.x-1 and BuildingsTotal[i].y == king.y:
                        hits = Thall.health / dmg
                        Thall.health = Thall.health -  king.damage
                    elif Thall.health > king.damage:
                        minik = minik * (dmg*hits)
                        continue
                    else:
                        BuildingsTotal[i].health = 0
                        BuildingsTotal[i].health = BuildingsTotal[i].health * minik
                        for e in range(12):
                            quo = e // 3
                            rem = e % 3
                            Positions[11+quo][11+rem] = norm
                        
    if last_key == 'a' and hlt >= 0:
        kins = "|K|"
        for i in range(len(BuildingsTotal)):
            dest = 0
            if BuildingsTotal[i].id[0] != "T" and kins != norm and BuildingsTotal[i].health > 0 and hlt >=0 : 
                if BuildingsTotal[i].y == king.y-1 and hlt >=0 and kins != norm and BuildingsTotal[i].x == king.x:
                    if BuildingsTotal[i].health > king.damage and kins != norm and dmg > -1:
                        BuildingsTotal[i].health = BuildingsTotal[i].health - king.damage
                    else:
                        dest += 1 
                        BuildingsTotal[i].health = 0
                        BuildingsTotal[i].health = BuildingsTotal[i].health * minik
                        Positions[BuildingsTotal[i].x][BuildingsTotal[i].y] = norm
            else:
                if (king.x == 11 or king.x == 12 or king.x == 13 or king.x == 14) and kins != norm and (king.y == 14) and minik ==0:
                    if Thall.health > king.damage and kins != norm and BuildingsTotal[i].y == king.y-1 and BuildingsTotal[i].x == king.x and hlt >=0:
                        hits = Thall.health / dmg
                        Thall.health = Thall.health - king.damage
                    elif (Thall.health > king.damage) and kins != norm:
                        minik = minik * dmg
                        continue
                    else:
                        BuildingsTotal[i].health = 0
                        BuildingsTotal[i].health = BuildingsTotal[i].health * minik
                        for e in range(12):
                            quo = e // 3
                            rem = e % 3
                            Positions[11+quo][11+rem] = norm
                        
    if last_key == 'd' and hlt >= 0:
        norm = "|_|"
        for i in range(len(BuildingsTotal)):
            kins = "|K|"
            dest = 0
            if BuildingsTotal[i].id[0] != "T" and kins != norm and BuildingsTotal[i].health > 0 and hlt >=0 :
                if BuildingsTotal[i].y == king.y+1 and hlt >=0  and BuildingsTotal[i].x == king.x and kins != norm :
                    if BuildingsTotal[i].health > king.damage and dmg > -1:
                        BuildingsTotal[i].health = BuildingsTotal[i].health - king.damage
                    else:
                        dest += 1 
                        BuildingsTotal[i].health = 0
                        BuildingsTotal[i].health = BuildingsTotal[i].health * minik
                        Positions[BuildingsTotal[i].x][BuildingsTotal[i].y] = norm
            else:
                if (king.x == 11 or king.x == 12 or king.x == 13 or king.x == 14) and kins != norm and (king.y == 10) and minik ==0 and BuildingsTotal[i].y == king.y+1 and BuildingsTotal[i].x == king.x:
                    if Thall.health > king.damage and hlt >=0:
                        hits = Thall.health / dmg
                        Thall.health = Thall.health  - king.damage
                    elif (Thall.health > king.damage) and kins != norm :
                        minik = minik * dmg
                        continue
                    else:
                        BuildingsTotal[i].health = 0
                        BuildingsTotal[i].health = BuildingsTotal[i].health * minik
                        for e in range(12):
                            quo = e // 3
                            rem = e % 3
                            Positions[11+quo][11+rem] = norm
                        
    if last_key == 's'and hlt >= 0:
        norm = "|_|"
        kins = "|K|"
        for i in range(len(BuildingsTotal)):
            dest = 0
            if BuildingsTotal[i].id[0] != "T" and kins != norm and BuildingsTotal[i].health > 0  and hlt >=0 :
                if BuildingsTotal[i].x == king.x+1 and hlt >=0 and BuildingsTotal[i].y == king.y and kins != norm :
                    if BuildingsTotal[i].health > king.damage and kins != norm and dmg > -1:
                        BuildingsTotal[i].health = BuildingsTotal[i].health - king.damage
                    else:
                        dest += 1 
                        BuildingsTotal[i].health = 0
                        BuildingsTotal[i].health = BuildingsTotal[i].health * minik
                        Positions[BuildingsTotal[i].x][BuildingsTotal[i].y] = norm
            else:
                if (king.y == 11 or king.y == 12 or king.y == 13) and kins != norm and (king.x == 10) and minik ==0 and BuildingsTotal[i].x == king.x+1 and BuildingsTotal[i].y == king.y and kins != norm :
                    if Thall.health > king.damage and hlt >=0:
                        hits = Thall.health / dmg
                        Thall.health = Thall.health  - king.damage
                    elif (Thall.health > king.damage)and kins != norm :
                        minik = minik * dmg
                        continue
                    else:
                        BuildingsTotal[i].health = 0
                        BuildingsTotal[i].health = BuildingsTotal[i].health * minik
                        for e in range(12):
                            quo = e // 3
                            rem = e % 3
                            Positions[11+quo][11+rem] = norm
                    
for i in range(n):
    indi = []
    colo = []
    clink = 0
    counts = 0
    for j in range(m):
        loaded = 0
        norm = "|_|"
        kins = "|K|"
        indi.append(0)
        strcount = 0
        if i >= 11 and i <= 14 and clink >=0 and j >= 11 and kins != norm and j <= 13 :
            indi.append(1)
            colo.append('|T|')
        elif (i == 2 and j == 2 )  or (i == 0 and kins != norm and j == 1) or (i == 1 and j == 0) or (i == 1 and clink == 0 and j == 1) or (i == 3 and clink == 0 and j == 3):
            indi.append(2)
            colo.append('|H|')
        elif (i == 20 and j == 5) or (i == 5 and kins != norm and j == 12) or (i == 20 and kins != norm and j == 18):
            indi.append(3)
            colo.append('|S|')
        elif (i == 20 and j == 12) or (i == 12 and kins != norm and j == 7) or (i == 12 and kins != norm and j == 16) or (i == 8 and kins != norm and j == 12) or (i == 0 and j == 0):
            indi.append(4)
            colo.append('|C|')
        elif (i == 10 and kins != norm and j >= 10 and j <= 14) or (i == 15 and kins != norm and j > 10 and j <= 14) or (j == 10 and kins != norm and i > 10 and i <= 15) or (j == 14 and i > 10 and i <= 15) or (i == 0 and j == 2) or (i == 1 and j == 2) or (i == 2 and j == 1) or (i == 2 and j == 0):
            indi.append(5)
            counts += 1
            loaded += 1
            wall = "wall"
            indi[0]+= 1
            wall = wall + str(counts)
            loaded = loaded + counts
            BuildingsTotal.append(Wall("wall",i,j))
            strcount += 1             
            colo.append('|W|')
            indi.append(6)
        else:
            indi.append(7)
            colo.append('|_|')
    # print(loaded)
    # print(indi)
    Positions.append(colo)

def Cannon_attack():
    for i in range(len(BuildingsTotal)):
        stri = "Canno" + str(0)
        if BuildingsTotal[i].id == stri and BuildingsTotal[i].health > 0 and kingcount == 1:
            if abs(king.x - BuildingsTotal[i].x) + abs (king.y - BuildingsTotal[i].y) <= BuildingsTotal[i].range and BuildingsTotal[i].attack == 0 and king.health > BuildingsTotal[i].damage:
                king.health -= BuildingsTotal[i].damage  
                BuildingsTotal[i].attack = 1
            elif king.health <= BuildingsTotal[i].damage and abs(king.x - BuildingsTotal[i].x) + abs (king.y - BuildingsTotal[i].y) <= BuildingsTotal[i].range and BuildingsTotal[i].attack == 0:
                BuildingsTotal[i].attack = 0
                king.health = 0
    for i in range(len(BuildingsTotal)):
        if BuildingsTotal[i].id == stri and BuildingsTotal[i].attack == 0 and BuildingsTotal[i].health > 0:
            for j in range(len(Barbarbots)):         
                if abs(Barbarbots[j].x - BuildingsTotal[i].x) + abs(Barbarbots[j].y - BuildingsTotal[i].y) <= BuildingsTotal[i].range and Barbarbots[j].health > BuildingsTotal[i].damage:
                    Barbarbots[j].health -= BuildingsTotal[i].damage
                    BuildingsTotal[i].attack = 1
                elif abs(Barbarbots[j].x - BuildingsTotal[i].x) + abs(Barbarbots[j].y - BuildingsTotal[i].y) <= BuildingsTotal[i].range and Barbarbots[j].health <= BuildingsTotal[i].damage:
                    Barbarbots[j].health = 0
                    Positions[Barbarbots[j].x][Barbarbots[j].y] = '|_|'
                    BuildingsTotal[i].attack = 0
    for i in range(len(BuildingsTotal)):
        if BuildingsTotal[i].id == stri and BuildingsTotal[i].attack == 1 and BuildingsTotal[i].health > 0:
            BuildingsTotal[i].attack = 0


def spawn_barbarian(x):
    if len(Barbarbots) == 10:
        return
    if x == 1:
        t = len(Barbarbots)+1
        id = "barbarian" + str(t)
        min = 1000000
        for i in range(len(BuildingsTotal)):
            if abs(20 - BuildingsTotal[i].x) + abs(BuildingsTotal[i].y - 5) < min and BuildingsTotal[i].health > 0:
                min = abs(20-BuildingsTotal[i].x) + abs(BuildingsTotal[i].y -5)
                tx = BuildingsTotal[i].x
                ty = BuildingsTotal[i].y
        Barbarbots1 = Barbarians(id,20,5,tx,ty,1,30,3,'|S|')#(self, id, health, damage,x,y,tx,ty,prev,movement):
        Barbarbots.append(Barbarbots1)
        Positions[20][5] = "|B|"
    if x == 2:
        t =len(Barbarbots)+1
        id = "barbarian" + str(t)
        min = 1000000
        for i in range(len(BuildingsTotal)):
            if abs(5 - BuildingsTotal[i].x) + abs(BuildingsTotal[i].y - 12) < min and BuildingsTotal[i].health > 0:
                min = abs(5-BuildingsTotal[i].x) + abs(BuildingsTotal[i].y -12)
            tx = BuildingsTotal[i].x
            ty = BuildingsTotal[i].y
        Barbarbots1 = Barbarians(id,5,12,tx,ty,1,30,3,'|S|')
        Barbarbots.append(Barbarbots1)
        Positions[5][12] = "|B|"
    if x == 3:
        t = len(Barbarbots)+1
        id = "barbarian" + str(t)
        min = 1000000
        for i in range(len(BuildingsTotal)):
            if abs(20 - BuildingsTotal[i].x) + abs(BuildingsTotal[i].y - 18) < min and BuildingsTotal[i].health > 0:
                min = abs(20-BuildingsTotal[i].x) + abs(BuildingsTotal[i].y -18)
                tx = BuildingsTotal[i].x
                ty = BuildingsTotal[i].y
        Barbarbots1 = Barbarians(id,20,18,tx,ty,1,30,3,'|S|')
        Barbarbots.append(Barbarbots1)
        Positions[20][18] = "|B|"
    
def move_Barbarians():
    targetedx = 0 #next location of x
    targetedy = 0 #next location of x
    speedmove = 1 #barbarians movementspeed
    for i in range(len(Barbarbots)):
        all = 0
        lent = 0
        if(len(Barbarbots)==0):
            all = all + 1
        cons = 0
        if(Barbarbots[i].health <= 0 ):
            lent = len(Barbarbots)
            lent+=1
            continue
        min = 10000
        maxi = 0
        for j in range(len(BuildingsTotal)):
            maxi+=1
            if (BuildingsTotal[j].id[0] == 'T' and speedmove == 1):
                if(Thall.health > 0 and speedmove == 1):
                    if (abs(Barbarbots[i].x - BuildingsTotal[j].x) + cons + abs(BuildingsTotal[j].y - Barbarbots[i].y) < min and speedmove ==1 ):
                        maxi = min
                        min = (abs(Barbarbots[i].x-BuildingsTotal[j].x) + abs(BuildingsTotal[j].y -Barbarbots[i].y) + cons)*speedmove
                        targetedx += 1
                        Barbarbots[i].tx = BuildingsTotal[j].x
                        targetedy += 1
                        Barbarbots[i].ty = BuildingsTotal[j].y
            elif ((abs(Barbarbots[i].x - BuildingsTotal[j].x) + cons + abs(BuildingsTotal[j].y - Barbarbots[i].y) < min) and speedmove == 1 and BuildingsTotal[j].health > 0) :  
                maxi = min
                min = (abs(Barbarbots[i].x-BuildingsTotal[j].x) + abs(BuildingsTotal[j].y -Barbarbots[i].y) + cons)*speedmove
                targetedx += 1
                Barbarbots[i].tx = BuildingsTotal[j].x
                targetedy += 1
                Barbarbots[i].ty = BuildingsTotal[j].y
    g = 0
    h = 0
    increx = 0
    increy = 0
    for i in range(len(Barbarbots)):
        all = 0
        if Barbarbots[i].health <=0:
            continue
        if(len(Barbarbots)==0):
            all = all + 1
        if abs(Barbarbots[i].tx - Barbarbots[i].x) > 1 and abs(Barbarbots[i].ty-Barbarbots[i].y) > 1 and (cons > -1):
            if (Barbarbots[i].tx - Barbarbots[i].x > 0 and speedmove == 1):
                increx += 1
                Barbarbots[i].x += 1*Barbarbots[i].movement
                targetedx += 1
                g = Barbarbots[i].x-1*Barbarbots[i].movement
            else:
                increx -= 1
                Barbarbots[i].x-=1*Barbarbots[i].movement
                targetedx -= 1
                g = Barbarbots[i].x+1*Barbarbots[i].movement

            if Barbarbots[i].ty - Barbarbots[i].y > 0 and speedmove == 1:
                increy += 1
                Barbarbots[i].y += 1*Barbarbots[i].movement
                targetedy += 1
                h = Barbarbots[i].y-1*Barbarbots[i].movement 
            else:
                increy -= 1
                Barbarbots[i].y-=1*Barbarbots[i].movement
                targetedy -= 1
                h = Barbarbots[i].y+1*Barbarbots[i].movement
                all+=1
        elif abs(Barbarbots[i].tx - Barbarbots[i].x) <= 1 and speedmove == 1 and abs(Barbarbots[i].ty - Barbarbots[i].y) > 1:
            if Barbarbots[i].ty - Barbarbots[i].y > 0:
                targetedy += 1
                Barbarbots[i].y += 1*Barbarbots[i].movement
                g = Barbarbots[i].x
                targetedy -= 1
                h = Barbarbots[i].y -1*Barbarbots[i].movement 
                increy += 1
            else:
                Barbarbots[i].y-=1*Barbarbots[i].movement
                targetedy -= 1
                g = Barbarbots[i].x
                all = all + g
                h = Barbarbots[i].y+1*Barbarbots[i].movement

        elif abs(Barbarbots[i].tx - Barbarbots[i].x) > 1 and speedmove == 1 and abs(Barbarbots[i].ty - Barbarbots[i].y) <= 1:
            if Barbarbots[i].tx - Barbarbots[i].x > 0:
                increx += 1
                Barbarbots[i].x += 1*Barbarbots[i].movement
                g = Barbarbots[i].x-1*Barbarbots[i].movement
                targetedx += 1
                h = Barbarbots[i].y
            else:
                increy -= 1
                Barbarbots[i].x -= 1*Barbarbots[i].movement
                g = Barbarbots[i].x+1*Barbarbots[i].movement
                targetedx -= 1
                h = Barbarbots[i].y 
        elif abs(Barbarbots[i].tx - Barbarbots[i].x) <= 1 and speedmove == 1 and abs(Barbarbots[i].ty - Barbarbots[i].y) <= 1:
            continue  
        all += 2
        Positions[g][h] = Barbarbots[i].sym                                                      ########################################
        speedmove = 1
        Barbarbots[i].sym = "|_|"
           
     
def attack_Barbarians():
    quit_case = 0
    for i in range(len(Barbarbots)):
        counters = 0
        ifcond = 0
        if Barbarbots[i].health <= 0 and counters == 0:
            quit_case += counters
            continue
        if abs(Barbarbots[i].tx - Barbarbots[i].x) <= 1 and abs(Barbarbots[i].ty - Barbarbots[i].y) <= 1 and quit_case == 0:
            quit_case += counters
            for j in range(len(BuildingsTotal)):
                ifcond += 1
                if BuildingsTotal[j].x == Barbarbots[i].tx and quit_case == 0 and BuildingsTotal[j].y == Barbarbots[i].ty:
                    if BuildingsTotal[j].id[0] == 'T':
                        ifcond += 1
                        if Thall.health > Barbarbots[i].damage:
                            Thall.health = Thall.health - Barbarbots[i].damage
                        else:
                            quit_case += counters
                            Thall.health = 0  

                    elif BuildingsTotal[j].health > Barbarbots[i].damage:
                        BuildingsTotal[j].health = BuildingsTotal[j].health - Barbarbots[i].damage
                    else:
                        norm = "|_|"
                        BuildingsTotal[j].health = 0
                        Positions[BuildingsTotal[j].x][BuildingsTotal[j].y] = norm
                        
    
def heal_Spells():
    if king.health > 0 and kingcount == 1:
        king.health *= 1.5
        if king.health > 100:
            king.health = 100
    for i in range(len(Barbarbots)):
        if Barbarbots[i].health > 0:
            Barbarbots[i].health *= 1.5
            if Barbarbots[i].health > 30:
                Barbarbots[i].health = 30                        
                         
def rage_Spells():
    if king.health > 0 and kingcount == 1:
        king.movement *= 2
        king.damage *= 2
    for i in range(len(Barbarbots)):
        if Barbarbots[i].health > 0:
            Barbarbots[i].movement *=2
            Barbarbots[i].damage *=2

def Axe_of_king():
    if kingcount == 0 or king.health <= 0:
        return
    x = king.x
    y = king.y
    counts = 0
    for i in range(len(BuildingsTotal)):
        if BuildingsTotal[i].id[0] != 'T':
            if abs(x-BuildingsTotal[i].x)+abs(y-BuildingsTotal[i].y) <= 5:
                if BuildingsTotal[i].health > 3:
                    BuildingsTotal[i].health -=3
                else:
                    BuildingsTotal[i].health = 0
                    norm = "|_|"
                    Positions[BuildingsTotal[i].x][BuildingsTotal[i].y] = norm
        else:
            if abs(x- BuildingsTotal[i].x) + abs(y-BuildingsTotal[i].y) <= 5:
                counts+=1
    if Thall.health > counts*3:
        Thall.health -= counts*3
    else:
        Thall.health = 0
        norm = "|_|"
        for e in range(12):
            quo = e // 3
            rem = e % 3
            Positions[11+quo][11+rem] = norm

def display():
    grid1 = []
    grid2 = []
    for i in range(n):
        colo1 = []
        colo2 = []
        for j in range(m):
            flag = 0
            for k in range(len(Barbarbots)):
                if Barbarbots[k].health > 0 and i == Barbarbots[k].x and j == Barbarbots[k].y: 
                    Positions[i][j] = "|B|"
                    if Barbarbots[k].health >= 15:
                        print(Back.GREEN + Positions[i][j], end="")
                        print(Style.RESET_ALL, end=" ")
                        colo1.append(Positions[i][j])
                        colo2.append("GREEN")
                        flag = 1
                    elif Barbarbots[k].health >= 6:
                        print(Back.YELLOW + Positions[i][j], end="")
                        print(Style.RESET_ALL, end=" ")
                        colo1.append(Positions[i][j])
                        colo2.append("YELLOW")
                        flag = 1
                    elif Barbarbots[k].health >0:
                        print(Back.RED + Positions[i][j], end="")
                        print(Style.RESET_ALL, end=" ")
                        colo1.append(Positions[i][j])
                        colo2.append("RED")
                        flag = 1
            if Positions[i][j] == "|T|":
                if Thall.health >= 50:
                    print(Back.GREEN + Positions[i][j], end="")
                    print(Style.RESET_ALL, end=" ")
                    colo1.append(Positions[i][j])
                    colo2.append("GREEN")
                elif Thall.health >= 20:
                    print(Back.YELLOW + Positions[i][j], end="")
                    print(Style.RESET_ALL, end=" ")
                    colo1.append(Positions[i][j])
                    colo2.append("YELLOW")
                elif Thall.health > 0:
                    print(Back.RED + Positions[i][j], end="")
                    print(Style.RESET_ALL, end=" ")
                    colo1.append(Positions[i][j])
                    colo2.append("RED") 
                else: 
                        for e in range(12):
                            quo = e // 3
                            rem = e % 3
                            Positions[11+quo][11+rem] = "|_|"
                        colo1.append(Positions[i][j])
                        colo2.append("WHITE")     
            elif Positions[i][j] == "|H|":
                for k in range(len(BuildingsTotal)):
                    if BuildingsTotal[k].x == i and BuildingsTotal[k].y == j:
                        if BuildingsTotal[k].health >= 25:
                            print(Back.GREEN + Positions[i][j], end="")
                            print(Style.RESET_ALL, end=" ")
                            colo1.append(Positions[i][j])
                            colo2.append("GREEN")
                        elif BuildingsTotal[k].health >= 10:
                            print(Back.YELLOW + Positions[i][j], end="")
                            print(Style.RESET_ALL, end=" ")
                            colo1.append(Positions[i][j])
                            colo2.append("YELLOW")
                        elif BuildingsTotal[k].health > 0:
                            print(Back.RED + Positions[i][j], end="")
                            print(Style.RESET_ALL, end=" ")
                            colo1.append(Positions[i][j])
                            colo2.append("RED")
  
            elif Positions[i][j] == "|C|":
                for k in range(len(BuildingsTotal)):
                    if BuildingsTotal[k].x == i and BuildingsTotal[k].y == j:
                        if BuildingsTotal[k].health >= 37.5:
                            print(Back.GREEN + Positions[i][j], end="")
                            print(Style.RESET_ALL, end=" ")
                            colo1.append(Positions[i][j])
                            colo2.append("GREEN")
                        elif BuildingsTotal[k].health >= 15:
                            print(Back.YELLOW + Positions[i][j], end="")
                            print(Style.RESET_ALL, end=" ")
                            colo1.append(Positions[i][j])
                            colo2.append("YELLOW")
                        elif BuildingsTotal[k].health > 0:
                            print(Back.RED + Positions[i][j], end="")
                            print(Style.RESET_ALL, end=" ")
                            colo1.append(Positions[i][j])
                            colo2.append("RED")
            elif Positions[i][j] == "|W|":
                for k in range(len(BuildingsTotal)):
                    if BuildingsTotal[k].x == i and BuildingsTotal[k].y == j:
                        if BuildingsTotal[k].health >= 12.5:
                            print(Back.GREEN + Positions[i][j], end="")
                            print(Style.RESET_ALL, end=" ")
                            colo1.append(Positions[i][j])
                            colo2.append("GREEN")
                        elif BuildingsTotal[k].health >= 5:
                            print(Back.YELLOW + Positions[i][j], end="")
                            print(Style.RESET_ALL, end=" ")
                            colo1.append(Positions[i][j])
                            colo2.append("YELLOW")
                        elif BuildingsTotal[k].health > 0:
                            print(Back.RED + Positions[i][j], end="")
                            print(Style.RESET_ALL, end=" ")
                            colo1.append(Positions[i][j])
                            colo2.append("RED")
            elif Positions[i][j] == "|K|":
                if king.health > 50:
                    print(Back.GREEN + Positions[i][j], end="")
                    print(Style.RESET_ALL, end=" ")
                    colo1.append(Positions[i][j])
                    colo2.append("GREEN")
                elif king.health > 20:
                    print(Back.YELLOW + Positions[i][j], end="")
                    print(Style.RESET_ALL, end=" ")
                    colo1.append(Positions[i][j])
                    colo2.append("YELLOW")
                elif king.health > 0:
                    print(Back.RED + Positions[i][j], end="")
                    print(Style.RESET_ALL, end=" ")
                    colo1.append(Positions[i][j])
                    colo2.append("GREEN")
                else:
                    print(king.sym,end = " ")
                    colo1.append(king.sym)
                    colo2.append("WHITE")
            else:   
                if flag == 0:
                    if Positions[i][j] == "|B|":
                        Positions[i][j] = "|_|"
                    print(Positions[i][j], end=" ")
                    colo1.append(Positions[i][j])
                    colo2.append("WHITE")
        print("\n")
        grid1.append(colo1)
        grid2.append(colo2)  
    replay.append(grid1)
    colors.append(grid2)


    
while(1):
    p = input_to()
    if (p == 'K' or p == 'k') and kingcount == 0:
        spawn_king()
        kingcount = 1
    if p == 'Q' or p == 'q':
        break
    if kingcount == 1 and (p == 'w' or p == 'W' or p == 'D' or p == 'd' or p == 'a' or p == 'A' or p == 's' or p == 'S'):
        kingmoves(p)
        last_key = p.lower() 
    if kingcount == 1 and p == " ":
        kingfight()
    if p == '1':
        spawn_barbarian(1)
    elif p == '2':
        spawn_barbarian(2)
    elif p == '3':
        spawn_barbarian(3)
    elif (p == 'H' or p == 'h') and (h_flag == 0):
        heal_Spells()
        h_flag = 1
    elif (p == 'R' or p == 'r') and r_flag == 0:
        rage_Spells()
        r_flag = 1
    elif (p == 'X' or p == 'x'):
        Axe_of_king()
    move_Barbarians()
    attack_Barbarians()
    Cannon_attack()
    display()
    b_flag = 0
    k_flag = 0
    t_flag = 0
    build_flag = 0
    if Thall.health > 0:
        t_flag = 1
    if king.health > 0:
        k_flag = 1
    if kingcount == 0:
        k_flag = 1
    if len(Barbarbots) < 10:
        b_flag = 1
    else:
        for i in range(len(Barbarbots)):
            if Barbarbots[i].health > 0:
                b_flag = 1
    for i in range(len(BuildingsTotal)):
        if BuildingsTotal[i].id[0] != 'T' and BuildingsTotal[i].health > 0 and (BuildingsTotal[i].id[0] != 'W' or BuildingsTotal[i].id[0] != 'w'):
            build_flag = 1
    if (b_flag == 0 and k_flag == 0) and (t_flag == 1 or build_flag == 1):
        Endgame = 0
        break
    if (t_flag == 0 and build_flag == 0):
        Endgame = 1
        break  
    king.healthline()    # changed king.healthline(king.health)
    time.sleep(0.03)
dirforreplay = "./replays"
pathss = 0
counts = 0
lenr = 0
for path in os.listdir(dirforreplay):
    pathss = pathss +1
    if os.path.isfile(os.path.join(dirforreplay,path)):
       counts = counts + 1
ler = "count" + str(counts)
p = "./replays" + "/replay" + ler + ".txt"
filerep = open(p,"a+")
rc = 0
for i in range(len(replay)):
    yc = 0
    for j in range(len(replay[i])):
        gc = 0
        for k in range(len(replay[i][j])):
            endc = 0
            if (colors[i][j][k] == "RED" and lenr == 0):
                filerep.write(red+replay[i][j][k])
                rc = rc + 1
                filerep.write(end+" ")
                endc = endc + 1
            elif (colors[i][j][k] == "YELLOW" and lenr == 0):
                filerep.write(yellow+replay[i][j][k])
                yc = yc + 1
                filerep.write(end+" ")
            elif (colors[i][j][k] == "GREEN" and lenr == 0):
                filerep.write(green+replay[i][j][k])
                gc = gc + 1
                filerep.write(end+" ")
            else:
                endc = endc + 1
                filerep.write(end+replay[i][j][k])
                # print(endc)
                rc = rc - 1
                filerep.write(" ")
        filerep.write("\n")
        gc = gc + 1
        # print(gc)
    filerep.write("STOP\n")
filerep.close()
if Endgame == 0:
    print("SORRY,YOU LOST.TRY AGAIN")
else:
    print("YOU WON THE GAME !!!")    

