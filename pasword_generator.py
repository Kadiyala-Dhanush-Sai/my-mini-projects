import random
print("WELCOME TO PASSWORD GENERATOR")
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
,"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]
symbols=["!","@","#","$","%","^","&","*","(",")","-","_","=","+","{","}","[","]","|","\\",":",";","\"","'",",",".","<",">","/","?","~","`"
]
numbers=['0','1','2','3','4','5','6','7','8','9']
l=int(input("how many letters you want in password:"))
s=int(input("enter how many symbols ypu want in password:"))
n=int(input("enter how many numbers you want in password:"))
k=0
L=0
m=0
password=[]
while k!=l:
    a=random.choice(letters)
    password.append(a)
    k=k+1
while L!=s:
    b=random.choice(symbols)
    password.append(b)
    L=L+1
while m!=n:
    c=random.choice(numbers)
    password.append(c)
    m=m+1
random.shuffle(password)
lis=''.join(password)
print(lis)
