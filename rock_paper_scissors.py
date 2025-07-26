'''
rock paper sicssors
'''
import random
r=int(input("enter the number for Rock:"))
p=int(input("enter the number for paper:"))
s=int(input("enter the number for scissors:"))
l=[]
l.append(r)
l.append(p)
l.append(s)
input_user=int(input("enter the number that which correspounds to your choice:"))
#computer process
a=random.randint(0,len(l)-1)
if input_user==r and l[a]==p:
    print("You Won")
elif input_user==r and l[a]==s:
    print("better luck next time")
elif input_user==p and l[a]==r:
    print("You Won")
elif input_user==p and l[a]==s:
    print("better luck next time")
elif input_user==s and l[a]==r:
    print("You Won")
elif input_user==s and l[a]==p:
    print("better luck next time")
elif input_user==l[a]:
    print("Match has been Draw")
