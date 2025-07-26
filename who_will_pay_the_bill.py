import random
a=input("enter every body's names and seperate by them with commas:").split(",")
b=random.randint(0,len(a)-1)
print(f"{a[b]} will pay the bill")