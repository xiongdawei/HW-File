#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 22:37:22 2018

@author: davidxiong
"""
"""
#question 1 Write a program that reads a file and 
prints only those lines that
 contain the substring snake.
 
"""
myfile = open("test.txt", "w")
myfile.write("My first file written from Python\n")
myfile.write("----------snake-\n")
myfile.write("hello,world!\n")
myfile.write("hello,world!\n")
myfile.write("hello,world!\n")
myfile.write("hello,world!\n")
myfile.write("hello,world!\n")
myfile.write("hello,world!\n")
myfile.write("hello,world!\n")

myfile.close()
# question 1
filea = open("test.txt","r")
content = filea.readlines()
filea.close()

content.reverse()
fileb = open("sortedtest.txt","w")
for i in content:
    fileb.write(i)
fileb.close()


# question 2

filec = open('test.txt',"r")
lista = filec.readlines()
for i in lista:
    if 'snake' in i:
        print(i)
    else:
        print(end=",")
        
        
# question 3 
filed = open('test.txt',"r")
listb = filed.readlines()
listd = listb
a='1234 '
for i in range(5):
    listb[i]= str(a+listb[i])
filee = open('test.txt',"w")
for ele in listb:
    filee.write(ele)



# question 4

filef = open('test.txt',"r")
listc = filef.readlines()
filef.close()
fileg = open("test.txt","w")
for mlm in listc:
    mlm = mlm[5:-1]
    fileg.write(mlm)
fileg.close()
print(listc)
    
    





    

    
    





    





