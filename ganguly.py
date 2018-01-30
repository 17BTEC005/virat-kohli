# snake and ladder
import random
count=0
while int(count<=100):
    n =input(" press r to roll a dice  ")
    if n=="r":
        a=random.randint(1,6)
        count=count+a
        print("your random is ",a)
        print("your count is ",count)
    if count==8:
        count=37
        print("you climb the ladder to", count)
    elif count==11:
        count=2
        print("snake bites you", count)
    elif count==13:
        count=34
        print("you climb the ladder to", count)
    elif count==25:
        count=4
        print("snake bites you ", count)
    elif count==38:
         count=9
         print("you climb the ladder to", count)
    elif count==40:
             count=68
             print("you climb the ladder to", count)
    elif count==52:
             count=81
             print("you climb the ladder to", count)
    elif count==65:
             count=46
             print("snake bites you", count)
    elif count==76:
             count=97
             print("you climb the ladder to", count)
    elif count==89:
             count=70
             print("snake bites you", count)

    elif count>=100:
        print("you win")


    
  

   
        
