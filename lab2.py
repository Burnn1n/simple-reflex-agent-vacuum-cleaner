import random
class rooms():
    roomCondition = [] # uruunuudiin baidal tsewer eswel bohir eseh
    place = 0 # toos sorogchnii bairlal oroonii dugaar
    #dirty bol 0 harin clean bol 1
    def __init__(self,n):
        # oroonuuded sanamsargui baidlaar tolowuudiig ogoh
        for _ in range(n):
            self.roomCondition.append(random.randint(0,1))
        print(self.roomCondition)
class actions(rooms):
    count = 1 # niit hiisen tsewerlegeenii too
    def __init__(self,n):
        super().__init__(n)
    # tsewerleh(dirty-s clean tolow ruu shiljuuleh)
    def suck(self):
        rooms.roomCondition[rooms.place] = 1
        print("Амжилттай цэвэрлэлээ")
    # 1 zuun tiish shiljih
    def left(self):
        rooms.place -= 1
    # 1 baruun tiish shiljih
    def right(self):
        rooms.place += 1
    # tsewerhen oroond yu ch hiihgui
    def noOp(self):
        pass
class operation(actions):
    def __init__(self,n):
        print(actions.count,"дахь тоос сорогчны үйлдэл эхлэв")
        super().__init__(n)
        if(rooms.place == 0): # herew zuun zahaas uildel ehleh bol
            for i in range(n):
                if rooms.roomCondition[rooms.place] == 0: # herew bohir bol
                    super().suck()                
                    print(rooms.roomCondition)
                else : # herew tsewer bol
                    super().noOp()
                if i == n-1:
                    break
                super().right()
                print("Баруун тийш шилжив")
        else: # herew baruun zahaas uildel ehleh bol
            for i in range(n):
                if rooms.roomCondition[rooms.place] == 0: # herew bohir bol
                    super().suck()                
                    print(rooms.roomCondition)
                else : # herew tsewer bol
                    super().noOp()
                if i == n-1:
                    break
                super().left()
                print("Зүүн тийш шилжив")
        rooms.roomCondition = []
        print(actions.count,"дахь тоос сорогчны үйлдэл амжилттай дуусав")
        actions.count += 1
for _ in range(2):
    operation(2)
