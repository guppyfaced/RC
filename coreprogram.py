import collections
from operator import add
class orders:
    def __init__(self):
        self.direction = collections.deque(['north','east','south','west'])
        self.cartesiandict = {'north':[0,1], 'east':[1,0], 'south':[0,-1], 'west':[-1,0]}
        self.wall = False
        try:
            print('The room')
            x = int(input('How wide is the room? '))
            y = int(input('How long is the room? '))
            self.roomsize = [x,y]
            splitstartinglocation = [int(x) for x in input('Where is the car in the room? Enter two numbers, seperated by a space ').split()]
            self.currentlocation = splitstartinglocation
            self.tracepath = [self.currentlocation,]
            numorientation = int(input('What is the starting direction? For north (N), select 1. For east (E), select 2. For south (S), select 3. For west (W), select 4 '))
            listorientation = {1:'north',2:'east',3:'south',4:'west'}
            self.orientation = listorientation[numorientation]
            while True:
                self.commands(input('Enter a direction. Try "f" for forward, "b" for backward, "l" for left and "r" for right '))
                if self.wall == True:
                    print(self.tracepath)
                    break
        except ValueError:
            print("That's not quite right. Try entering a number")
        except IndexError:
            print("It seems like the car got lost. Try loading it again")
    def step(self, currentlocation, orientation, cartesiandict):
        self.currentlocation = list(map(add, self.currentlocation, self.cartesiandict[self.orientation]))
        if ((self.currentlocation[0] > self.roomsize[0]) or (self.currentlocation[1] > self.roomsize[1])) or ((self.currentlocation[0] < 0) or (self.currentlocation[1] < 0)):
            print('The remote control car hit a wall. Oh dear')
            self.wall = True
            return self.wall
        else:
            self.tracepath.append(self.currentlocation)
            return self.currentlocation, self.tracepath
    def turn(self, cycle):
        self.direction.rotate(cycle)
        self.orientation = self.direction[0]
        return self.direction, self.orientation
    def commands(self, commands):
        for command in commands:
            print(command)
            if command == 'r':
                self.turn(-1)
            elif command == 'l':
                self.turn(1)
            elif command == 'f':
                self.turn(0)
                self.step(self.currentlocation, self.orientation, self.cartesiandict)
            elif command == 'b':
                self.turn(-2)
                self.step(self.currentlocation, self.orientation, self.cartesiandict)
                self.turn(2)
            else:
                print('The command was not understood. Try again')
                
if __name__ == "__main__":
    test1 = orders()

#test1 = orders()