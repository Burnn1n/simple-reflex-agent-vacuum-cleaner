import random
class rooms():
    roomCondition = [] # conditions of room dirty or clean
    place = 0 # position of vacuum cleaner(number of room)
    #0 if dirty else 1
    def __init__(self,n):
        # all conditions of room are random
        for _ in range(n):
            self.roomCondition.append(random.randint(0,1))
        print(self.roomCondition)
class actions(rooms):
    count = 1 # count of cleaned area
    def __init__(self,n):
        super().__init__(n)
    # clean(make dirty condition clean)
    def suck(self):
        rooms.roomCondition[rooms.place] = 1
        print("successfully cleaned")
    # move to the left 
    def left(self):
        rooms.place -= 1
    # move to the right
    def right(self):
        rooms.place += 1
    # if condition is clean. Obviously this function is not needed but for better understanding in simple reflex agent it is included
    def noOp(self):
        pass
class operation(actions):
    def __init__(self,n):
        print(actions.count,"th operation of vacuum cleaner has started")
        super().__init__(n)
        if(rooms.place == 0): # if operation is starting from left
            for i in range(n):
                if rooms.roomCondition[rooms.place] == 0: # if room is dirty
                    super().suck()                
                    print(rooms.roomCondition)
                else : # if room is clean
                    super().noOp()
                if i == n-1:
                    break
                super().right()
                print("just moved to right")
        else: # if operation is starting from right
            for i in range(n):
                if rooms.roomCondition[rooms.place] == 0: # if room is dirty
                    super().suck()                
                    print(rooms.roomCondition)
                else : # if room is clean
                    super().noOp()
                if i == n-1:
                    break
                super().left()
                print("just moved to left")
        rooms.roomCondition = []
        print(actions.count,"th operation of vacuum cleaner has successfully finished")
        actions.count += 1
count_of_operation = 2
count_of_rooms = 4
for _ in range(count_of_operation):
    operation(count_of_rooms)
