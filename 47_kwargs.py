'''args store value in tuple'''
import sys
def fun(*args):
	if (len(args)== 3):
		print("The Name of the student",args[0],"and age is ",args[1],"and Rollno is ",args[2])
	else:
		print("The name of the student is ",args[0],"And age is ",args[1])




name = input("Enter Your Name :")
age = int(input("Enter Your Age :"))
roll = int(input("Enter Your Roll no:"))
lis = [name,age,roll]
fun(*lis)	
if lis == 0:
	print("milu")
