# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 09:48:01 2019

@author: SHANKAR
"""
#counting of number of words in file"
j=0
with open("hello.txt", mode="r") as my:
    for i in my.readlines():
        j = j + len(i.split())
    print(j)

    
with open("hello.txt", mode="r") as my:
       d = len(my.read())
       print(d)
       
with open("hello.txt", mode="r") as my:
    for i in my.readlines():
        print(i.split())

with open("hello.txt","r") as my:
    for i in my.readlines():
        print(len(i.split()))
       
       
s=[]      
with open("hello.txt", mode="r") as my:
    for i in my.readlines():
        s.append(i.split())
    print(s)
    
#uniqu words in the file    
s=[]      
with open("hello.txt", mode="r") as my:
    for i in my.readlines():
        s.append(i.split())
    l = [j for i in s for j in i]
    print(l)
    print(list(set(l))) 
    
# plaindromes in the file    
data = ['world', 'mom', 'world2', 'hello']

for i in data:
    if i == "".join(reversed(i)):
        print("the palindrome word from list is: ",i)



#annagrame in the file
with open('hello.txt','r') as my:
    for i in my.readlines():
        i=sorted(i)
    for j in my.readlines():
        j=sorted(j)
    if(i==j):
        print("anagrame word",i)
s=[]        
with open('hello.txt','r') as my:
    for i in my.readlines():
        print(i.split())
        s.append(i)
        print(s)
    for j in s:
        j=sorted(j)
        
    if (i==j):
        print(i)

data=['hello','world','welcome','to','the','world']

for k in data:
    for l in data:
        if (k==l):
            print(k)





        


