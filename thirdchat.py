#lists in python
# a=[1,2,3,4,5,6,7]
# print(len(a))
# b=["sokeena",19,"bhaktapur"]
# print(b[2])
# b[2]="nepal"
# print(b[2])#list are mutable whereas strirng are not mutable
# print(a[0:2]) #slicing
# print(type(a)) 
# a.append(3) #adding 3 on the list
# print(a)
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# B=["S","O","P"]
# B.sort(reverse=True)
# print(B)
# B.reverse()
# print(B )
# B.insert(1,"B")
# print(B)
# B.pop(2)
# print(B)
# a=[]
# num1=int(input("enter first num:"))
# a.append(num1)
# num2=int(input("enter a numb:"))
# a.append(num2)
# num3=int(input("enter a numb:"))
# a.append(num3)
# print(a)
# a.sort()
# print(a)
# a.sort(reverse=True)
# a=(3,4,5,6)
# print(type(a))
# tup=(2,3,5,6,7,8,9,6,8,9)
# print(type(tup))
# print(tup[1:5])  
# print(tup.index(6)) #first occurance i.e 6 3rd index ma aaucha
# print(tup.count(6))
# a=[]
# subj=[]
# subj.append(input("enter subject:"))
# subj.append(input("enter subject:"))
# subj.append(input("enter subject:"))
# print(subj)
# list=[1,2,2,1]
#DICTIONARY
# dict={"name":"sokeena",
#       "age":19,
#       "subj":"science"}
# print(dict)
# print(type(dict))
# print(dict.pop("age")) #19
# dict2={"age group":[2,3,4,5,6,7,77,7],
#        "rolln":(2,3,4,4,4),
#        "IS_TRUE":True,}
# print(dict2["age group"])
# dict2["rolln"]=[33,44,5,6,7]
# dict2["hername"]="sokeena"
# dict2["moviee"]=input("enter your favorite movie:")
# print(dict2)
#NESTED 
# student={"name":"sokeena",
#          "subject":{"subject1":"science",
#                     "subject2":"maths"},
#                     "age":19}
# print(student["subject"]["subject1"])
# print(student.keys())#kati ota key cha main{}ma tei aaucha
# print(tuple(student.keys()))#we can change into list or tuple too
# print(len(student))
# print(student.values())
# print(list(student.values()))
# print(student.items()) #tuples bhayera aauchaa ()
# print(student.get("subject"))#none aaucha if key chaina bhane error chai aaudaina 
# student.update({"digit":22})
# print(student)
#SETTSS
# Set={2,4,5,6,6,7,8,8}
# print(Set)
# print(type(Set)) 
# print(len(Set ))
# nullset=set()
# nullset.add(input("enter any numb:"))
# nullset.add(input("enter any numb:"))
# nullset.add(input("enter any numb:"))
# print(nullset)
# nullset.remove("3")
# print(nullset)
# collection={"her","name","what"}
# print(collection.pop())
# print((collection.pop())
# print(collection.pop())
# Y={2,3,4,5,6,5}
# Z={3,4,4,8,9,9}
# print(Y.intersection(Z))
# print(Z.union(Y))
# print(Z.difference(Y))
# print((Z.issubset(Y)))
#QUESTIONSS
# A={}
# A.update({"HER NAME":"SOKEENA"})
# A.update({"HER AGE":input("HER AGE IS:")})
# A["CLASS"]="12"
# print(A)
# print(A["HER NAME"])
# print(list(A))
# print(tuple(A))
# print(A.values())
# SET={"PYTHON","JAVA","PYTHON","JAVA","JAVASCRIPT"}
# print(len(SET))
# sett=set()
# sett.add(3)
# print(sett)
# a={}
# a.update({"name":"sokeena"})
# a.update({"age":input("enter your age:")})
# a.update({"class":"bachelor"})
# print(a)
# print(a.items())
# print(a.values())
# print(a.pop("age"))
# print(list(a))
# print(len(a))
# print(a.get("name"))
# set1={3,4,5,6,7}
# set2={4,4,5,6,7,8,2,3}
# print(set1.intersection(set1))
# print(len(set1))
# print(set2.pop())
# print(set2.issubset(set2))
# list1=[2,3,4,5,6,7,8,8,8]
# list2=[3,3,4,5,6,7,7,8,8]
# list3=[list1,list2]
# print(list3)
#LOOP #for repeating
# i=1
# while i<=5:
#     print(i)
#     i+=1
# n=int(input("enter a number:"))
# while n<=8:
#     print("*")
#     n+=4
# n=1
# while n<=100:
#     print(n)
#     n+=1
# n=100
# while n>=0:
#     print(n)
#     n-=1
# n=1
# while n<=10:
#     print(3*n)
#     n+= 1
#qs4
# numb = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(numb):
#     print(numb[idx])
#     idx+=1
# Y=['a','b','c','d','e']
# idx=0(
# while idx<len(Y):
#     print(Y[idx])
#     idx+=1
# numb=(1,4,9,16,25,36,49,64,81,100)
# x=36
# i=0
# while i<len(numb):
#     if(numb[i]==x):
#         print("found it at idx",i)
#         break
#     else:
#         print("processinggg...")
#     i+=1
# i=1
# while i <=7:
#     print(i)
#     if(i==6):
#         break
#     i+=1
# i=0
# while i<=5:
#     if(i==3):
#         i+=1
#         continue #skip garnako lagi
#     print(i)
#     i+=1
# i=1
# while i<=10:
#     if(i%2!=0):
#         i+=1
#         continue
#     print(i)
#     i+=1
# numb=[1,2,3,4,4,5,6,7,8,9,9]
# i=0
# while i<len(numb):
#     if(i==4):
#         i+=1
#         continue
#     print(numb[i])
#     i+=1
#FOR LOOP
# list=[1,2,3,4,5,5]
# for el in list:
#     print(el)
# tup=('cat','dog','rat','cow')
# for animals in tup:
#     print(animals)
# name="sokeena"
# for a in name :
#     print(a)
# else:
#     print("endd")
# list=[1,4,9,16,25,36,49,64,81,100]
# for num in list:
#     print(num)
# tup=(1,4,9,16,25,36,49,64,81,10)
# x=16
# idx=0
# for num in tup:
#     if(num==16):
#         print("found x at index:",idx)
#     idx+=1
#RANGEEEE
# for val in range(1,10):
#     print(val)
# for el in range(9):
#     print(el)
# for el in range(1,7,2):#range(start ,stop, step)
#     print(el)
# for i in range(100,0,-1):
# #     print(i)
# n=3
# for i in range(n,10*n,n):
#     print(i)
# n=int(input("enter a num:"))
# for a in range(1,11):
#     print(n*a)
# n=3
# sum=0
# for i in range(1,n+1):
#     sum+=1
#     print(sum)
# n=7
# sum=0
# i=1
# while i <=n:
#     sum+=i
#     i+=1
# # print("total:",sum)
# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
# #     print(fact)
# for i in range(1,101,2):
#     print(i)
# n=1
# while n<=10:
#     print(n)
#     n+=1
# k=[1,2,3,4,5,6,7,8,9,9,9,9,9,9,9]
# print(k.count(9))
# print(len(k))
# k.append(8)
# print(k)
# k.sort()
# print(k)
# k.sort(reverse=True)
# print(k)
# k.insert(5,6)
# print(k)
# # print(k[3])
# numbers = [3, -1, 0, -7, 5, -2, 9]
# positives = [n for n in numbers if n >= 0]
# negatives = [n for n in numbers if n < 0]

# print("Positives:", positives)
# print("Negatives:", negatives)
# numb=[1,2,3,4,5,6,7,8,9,10]
# even = [n for n in numb if n%2==0]
# odd = [n for n in numb if n%2!=0]
# print("even numbers are:",even)
# print("odd numbers aree :",odd)
# # num1=[1,2,1]
# # num1.copy()
# # num1.reverse()
# # if(num1.copy()==num1.reverse()):
# #     print("parlindrone")
# # else:
# #     print("nott")

# num1 = [1, 2, 1]

# # Make a copy before reversing
# original = num1.copy()
# num1.reverse()

# if original == num1:
#     print("palindrome")
# else:
#     print("not")

# dict={}
# dict["name"]="sokeena"
# dict.update({"class":12})
# print(dict)
# name="sokeena"
# i=1
# while i<=4:
#     print(name)
#     i+=1
# for r in name:
#     print(name)
