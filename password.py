#!/usr/bin/python3
user = input("enter your name: \n")
user_age = int(input("enter your age: \n"))
user_pass =  input("enter your password: \n")

if(user == "" or user_pass == ""):
    print("user didn't enter neme/password")
elif(user_age < 18 or user_age > 120):
    print("user age is not good...")
elif(user_pass != "123456"):
    print("wrong password!")
else:
    print("user", user, "OK to enter program..")
    print("program is running..")
