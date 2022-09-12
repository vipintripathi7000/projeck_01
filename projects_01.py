import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp == 'w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp =='w':
        if you=='g':
            return False
        elif you=='s':
            return True    
        
print("Comp  Turn: Snake(S) Water(W) or Gun(G)?")           


randNo = random.randint(1, 2)
print(randNo)
# print("Comp  Turn: Snake(S) Water(W) or Gun(G)?")
# b = input("player's Turn: Snake(S) Water(W) or Gun(G)?")