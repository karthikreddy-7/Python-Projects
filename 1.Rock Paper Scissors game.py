#rock paper scissors:
import random as r
import time as t    
print("Welcome to the Rock Paper Scissor game")
t.sleep(2)
print("choose any one of the following:")
print("computer will choose itself among the three")
print("let's see who wins ")
print("0 for rock \n1 for paper \n2 for scissors ")
x=int(input())
if 0<=x<=2:
    y=r.randint(0, 2)
    if x==1:
        z1="paper"
    elif x==0:
        z1="rock"
    elif x==2:
        z1="scissors"
    if y==1:
        z2="paper"
    elif y==0:
        z2="rock"
    elif y==2:
        z2="scissors"
    if (y==0 and x==2) or (y==1 and x==0) or (y==2 and x==1) :
        print("you have lost")
        print(f"you have choosed {z1}")
        print(f"computer has choosed {z2}")
    if x==y:
        print("match draw as you and computer choosed same")
    if (x==0 and y==2) or (x==1 and y==0) or (x==2 and y==1) :
        print("you have won")
        print(f"you have choosed {z1}")
        print(f"computer has choosed {z2}")
else:
    print("sorry ! invalid key entered")
        
