import time
class GameCharater:
    def __init__(self,name,health,level):
        self.name=name
        self.health=health
        self.level=level


class Wizard(GameCharater):
    def __init__(self, name, health, level,daggers):
        super().__init__(name, health, level)
        self.daggers=daggers

    # attack
    def magic_attack(self,other):
        '''when wizard attacks other reduce health of other charatcers by 1,dagger count by 1'''
        if self.daggers>0:
            print("="*100)
            print(f"{self.name.title()} attacking {other.name.title()}.....")
            other.health-=1
            self.health+=1
            self.daggers-=1
            print(f"{self.name.title()} Health: {self.health}, {other.name.title()} Health: {other.health}, Darggers Left: {self.daggers}")

        
class Warrior(GameCharater):
    def __init__(self, name, health, level,sword):
            super().__init__(name, health, level)
            self.sword=sword
    
    # attack
    def warrior_attack(self,other):
        '''when warrior attacks other reduce health of other charatcers by 1,sword count by 1'''
        if self.sword>0:
            print("="*100)
            print(f"{self.name.title()} attacking {other.name.title()}.....")
            other.health-=1
            self.health+=1
            self.sword-=1
            print(f"{self.name.title()} Health: {self.health}, {other.name.title()} Health: {other.health}, SwordLeft: {self.sword}")

class Archer(GameCharater):
    def __init__(self, name, health, level,arrow):
            super().__init__(name, health, level)
            self.arrow=arrow
    
    # attack
    def archer_attack(self,other):
        '''when archer attacks other reduce health of other charatcers by 1,arrow count by 1'''
        if self.arrow>0:
            print("="*100)
            print(f"{self.name.title()} attacking {other.name.title()}.....")
            other.health-=1
            self.health+=1
            self.arrow-=1
            print(f"{self.name.title()} Health: {self.health}, {other.name.title()} Health: {other.health}, Arrows Left: {self.arrow}")

wizard1= Wizard("wizard",10,1,10)
warrior1= Warrior("warrior",10,1,10)
archer1= Archer("archer",10,1,10)

# repate the loop till all the charter health because zero
frameCount=1000
timer=0
print("Level 1 started...")
while timer<60:
    # level 1
    time.sleep(1)
    if frameCount%2==0:
          wizard1.magic_attack(warrior1)
    elif frameCount%7==0:
        warrior1.warrior_attack(wizard1)
    elif frameCount%3==0:
        archer1.archer_attack(wizard1)
    elif frameCount%20==0:
        wizard1.daggers+=10   # wizard gets more power
    else:
        wizard1.magic_attack(archer1)

    if warrior1.health<=0 and archer1.health<=0 and wizard1.health<=0:
        break
    
    timer+=1
    frameCount-=1

if timer==60:
    print("Game Over")
    print(f"Wizard Health: {wizard1.health},Warrior Health: {warrior1.health},Archer Health: {archer1.health}")
    
