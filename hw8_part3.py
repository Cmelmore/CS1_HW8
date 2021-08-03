"""
Author: Christina Elmore
RIN: 661542904
Section #: 2
Assignment: HW 8 Part 3
Purpose: Implement a simple game of battleship
"""
import sys

class Battleship(object):
    def __init__(self, name, x0, y0, length, height, health):
        self.name = name
        self.x = int(x0)
        self.y = int(y0)
        self.length = int(length)
        self.height = int(height)
        self.health = int(health)
                
    def check_hit(self, x, y): #checks to see if strike at x,y hits a ship and adjusts health if it does
        if self.x <= int(x) <= (self.x+self.length) and self.y <= int(y) <= (self.y+self.height):
            self.health = self.health-1
            if self.health < 1:
                self.health = 0
                return 'sunk'
            else:
                return 'hit'
        else:
            return 'miss'
        
    def ship_name(self): #right justified name
        return '%s:' %self.name.rjust(12)
    
    def ship_name_l(self): #name of ship
        return self.name
        
    def status(self): #returns status of the ship
        return "(%d,%d,%d,%d) Health: %d" %(self.x, self.y, self.x+self.length, self.y+self.height, self.health)
        
if __name__ == '__main__':
    f_name = raw_input('File name => ')
    print f_name

    f = open(f_name)
    info = f.read()
    list_info = info.split('\n')
    
    #gets ship info from file
    ship_num = int(list_info[0])
    ship_list = []
    i = 1
    while i <= ship_num:
        ship = list_info[i].split('|')
        ship_list.append(Battleship(ship[0], ship[1], ship[2], ship[3], ship[4], ship[5]))
        i += 1
    for ship in ship_list:
        print '%s %s' %(ship.ship_name(), ship.status())
    
    #run through player commands and executes attacks
    i = (ship_num + 1)   
    while i < len(list_info):
        player_info = list_info[i].split('|')
        if player_info[0] == '':
            break
        miss_count = 0       
        for ship in ship_list:
            if ship.check_hit(player_info[1], player_info[2]) == 'hit':
                print '%s fires (%s, %s) hits %s %s' %(player_info[0], player_info[1], player_info[2], ship.ship_name(), ship.status())
            elif ship.check_hit(player_info[1], player_info[2]) == 'sunk':
                print '%s fires (%s, %s) hits %s %s' %(player_info[0], player_info[1], player_info[2], ship.ship_name(), ship.status())
                print '%s is sinking!' %ship.ship_name_l()
                ship_list.remove(ship)
                miss_count -= 1
                
                #if all ships sink
                if len(ship_list) < 1:
                    print "%s won" %player_info[0]
                    sys.exit()
            else:
                miss_count += 1
        if miss_count == len(ship_list):
            print '%s misses at (%s,%s)' %(player_info[0], player_info[1], player_info[2])
        i += 1
    #if not all ships sunk
    print 'No player won!'       