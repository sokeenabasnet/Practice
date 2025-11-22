#FUNCTIONS 
# #function definition 
# def cal(a,b): #parameters 
#     sum=a+b
#     print(sum)
#     return(sum)
# cal(2,3) #function call; arguments
# cal(4,5)
# cal(7,7)
# def print_hello():
#     print("hello")
# print_hello()
# print_hello()
# output=print_hello()
# print(output)#none aaucha kina ki return bhako chaina
# def cal(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(avg)
#     return avg
# cal(2,3,5)
# print("sokeena",12) #sep
# print("sokeena",end="")
# print("basnet")
# def multi(a=1,b=1): #default values
#     print(a*b)
#     return a*b
# multi() 
#default values last ma aauna parchaa
# cities=["ktm","bhktp","pokhara"]
# country=["nepal","india","china","bhutan"]
# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(country)
# def print_list(list):
#     for item in list:
#         print(item,end=" ")

# print_list(cities)
# print_list(country)
# def calu_fact(n=1):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)
# calu_fact(7)
# def converter(usd):
#     inr=usd*83
#     print(usd,"usd:",inr,"inr")
# converter(int(input("enter usd:")))
# def num(a):(
#     if(a%2==0):
#         print("even")
#     elif(a%2!=0):
#         print("odd")
# num(int(input("enter a number:")))
#RECURSIVE FUNCTION
# def show(n):
#     if(n==0): #BASE CASE
#         return
#     print(n)
#     show(n-1)
 

# show(int(input("ENTER A NUM:")))
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n 
# print("welcome to nepal telecom")
# balance={"data":1415,
#          "balance":400}
# dataa=["voice pack","data pack"]
# balance2=int(input("enter a number:"))
# if(balance2==balance["data"]):
#     print(n for n in dataa)
# elif(balance2==balance["balance"]):
#     print("your remaining data is:",)
# else:
#     print("please enter correct numberrr")
# import random 
# a=random.randint(1,10)
# print("guess a number from 1 to 10")
# guessed=int(input("enter a guess number:"))
# while a<=11:
#     a==guessed
#     print("your guess is correctt")
#     break
# if(a<=guessed):
#     print("your guess is lesser than correct guess")
# elif(a>=guessed):
#     print("your guess is higer than numberr")
# else:
#     print("error")
# import random

# a = random.randint(1, 10)
# print("Guess a number from 1 to 10")

# while True:
#     guessed = int(input("Enter your guess: "))
    
#     if guessed == a:
#         print("🎉 Your guess is correct!")
#         break
#     elif guessed < a:
#         print("Your guess is too low. Try again!")
#     else:
#         print("Your guess is too high. Try again!")
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
 
 
