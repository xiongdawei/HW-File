#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 22:37:22 2018

@author: davidxiong
"""
"""
file Homework Sep25th, 2018
 
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
"""
reverse the line in the file
"""
def file_reverse():
    file_a = open('filea','w')
    content = file_a.readlines()
    content.reverse()
    fileb = open("sortedtest.txt","r")
    for i in content:
        fileb.write(i)
    fileb.close()
    file_a.close()



# question 2
"""
print the line in which contain the the string 'snake'
"""
def find_snake():
    filec = open('test.txt',"r")
    lista = filec.readlines()
    for i in lista:
        if 'snake' in i:
            print(i)
        else:
            print(end=",")
        
        
# question 3 
"""
add numbers at the very beginning of first five snetence
"""
def add_number():
    filed = open('test.txt',"r")
    listb = filed.readlines()
    a='1234 '
    for i in range(5):
        listb[i]= str(a+listb[i])
    filee = open('test.txt',"w")
    for ele in listb:
        filee.write(ele)
    filed.close()
    filee.close()


# question 4
"""
delete the number and the space at the beginning of the line
"""
def remove_number():
    filef = open('test.txt',"r")
    fileg = open('test.txt','w')
    listt = filef.readlines()
    for i in range(len(listt)):
        fileg.write(listt[i][5:-1])
