n = int(input("enter the number::"))
num = 1
for row in range(1,n+1):
    for col in range(1,row+1):
        print(num,end=" ")
        num = num + 1
    print("")
print("-----------------------------------------")

n = int(input("enter the num:"))
def genfun():
    yield 1

for x in genfun():
    print(x)
print("-----------------------------------------")

import datetime
x = datetime.datetime(2014,3,31,11,5,0)

print(x.year)
print(x.month)
print(x.day)
print(x.strftime("%A"))
print(x.strftime("%b"))
print("------------------------------------------")

import json
dic = {"name":"lakki", "age":24,"marks":"one","subject":1}

jsonn = json.dumps(dic,indent=2,sort_keys="")
print(jsonn)
jsonn = json.loads(dic)
print(jsonn)
print("--------------------------------------------")

num1 = float(input("enter the num1::"))
num2 = float(input("enter the num2::"))
num3 = num1/num2
try:
  print(num3)
except Exception as e:
  print("Something went wrong",e)
else:
  print("Nothing went wrong")

n = int(input("enter the row value::"))
assci=65
for i in range(0,n):
  for i in range(0,i+1):
    val=chr(assci)
    print(val,end=" ")
    assci+=1
  print()
lis = [1,2,3,4,2,3,]
namee = str(input("enter the name::"))
age  = int(input ("enter the age::"))

def fun(name,age):
  return "hello",name
  print("i am %d years old " % )

a = fun(namee)

print("calculate the age -------- ")
from datetime import datetime
# import arrow
Datetime_str = input("enter the dob::")
name = input("What is your name: ")
birthDate = datetime.strptime(Datetime_str,'%d-%m-%Y').date()

# birthDate = datetime.strptime(Datetime_str,arrow.now().format('YYYY-MM-DD'))
#dtobject
# dat_time = datetime.datetime.strptime(stDate,'%Y-%m-%d %H:%M:%S.%f')
todays = datetime.today()
wtodays = birthDate.weekday()
dic = {0:"monday",1:"tuesday",2:"wednesday",3:"thursday",4:"friday",5:"saturday",6:"sunday"}
pdays = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
age = int(todays.strftime("%Y")) - birthDate.year - ((todays.month, todays.day) < (birthDate.month, birthDate.day))
print("--------------------------------------------------------------------------------------------------")



print("take the input as file and count the lines,charecter,words ")
fh = ("programmes.py.txt","r")
fh.count()
file__IO = input('\nEnter file name here to analize with path:: ')
with open(file__IO, 'r') as f:
    data = f.read()
    line = data.splitlines()
    words = data.split()
    spaces = data.split(" ")
    charc = (len(data) - len(spaces))

    print('\n Line number ::', len(line),
'\n Words number ::', len(words), '\n Spaces ::', len(spaces), '\n Charecters ::', (len(data)-len(spaces)))
print("-----------------------------------------------------------------")



print("print thee * values usig alphabets")
n = int(input("enter the row value::"))
assci=65
for i in range(0,n):
  for i in range(0,i+1):
    val=chr(assci)
    print(val,end=" ")
    assci+=1
  print()
lis = [1,2,3,4,2,3,]
print("-----------------------------------------------------------------")





print("count the length of the character")
name = "i am lakki "
name = str(input("enter the sentence::"))
charect = name.split()
# chare = len(name)
# charee = len(name)- len(charect)
# print(" with space count:: ",chare)
# print(" without spaceount::",charee)
print(" number of words::   ",len(charect))
print("------------------------------------------------------------")
import re
count = 0
txt = "abcabdghdabcabc"
matcher = re.search("abc",txt)
# for i in matcher:
#   print("start {} ,end {} ,group {}".format(i.start(),i.end(),i.group()))
#   count+= 1
# print("matcher occurence::",count )
# print(f.matcher{})

print(matcher)
'''  file handling is an important part of the web application
   python has several function are there creating and reading updating ,deleting files  '''

f = open("filename","a")
f.write('hello')
f.write( ", ")
# for f in f:
#     print(f)
# print(f.readline())
f.close()
f = open("filename","r")
for f in f:
    print(f)
import os
if os.path.exists("filename"):
    os.remove('filename')
else:
    print("file does not here")
def fun(games,end):
    # print("end::",end,end=" ")
    for games in games:
        # print("end::",games, end=" ")
        print("games::"+games,end=" ")
    for end in end:
        print(end)
sports = ["volley ball","cricket","shotput","ko ko"]
fun(sports,":e
# class college:
    """i am lakki"""
    def __init__(self,name,name1):
        self.name = (input("enter the num1::"))
        self.name2 = (input("enter the num2::"))
        z = name/name1
        print(name,name1,z)
        print(self.name,self.name2)

# help(college)
# print(college.__doc__)




x = college(1,10)


n = int(input('Num:'))
if n%2 == 1:
   print('prime')
# if n%2==1:
#       print("prime")
else:
  print('not prime')


x = int(input("NUM1:"))
y = int(input("NUm2:"))
if x%2 !=0  or y%2 !=0:
    print(x," is an prime number")
    # print(y,"is an prime number")
else:
        # or  x%2 ==1 :
    print(y,"is an not prime number")
    # print(x,"is an not prime NUmber")

print("1")
x = int(input("Enter the NUmber::"))
for i in range(2,x):
    if (x%i==0):
      # if(x%i==1)
        print("Not prime")
        break
else:
    print("prime")


x = int(input("Enter the Number1:"))
# y = int(input("Enter the Number2:"))
for i in range(0,x,2):
    print("Even Number",i)
    list = []
    list1 = list.append(i)
    if x==x-1:
        print(len(list1))
    if i%2==0:
        print(list)
summ = sum +2
print("sum::",summ)




if x%2==0:
    print("even")
else:
    print("odd")

elif y%2==0:
    print("odd")

n = int(input("Enter a Number :"))

print("--3")
num = int(input("Enter the number::"))
num1 = int(input("Enter the number::"))
i=1
sum=0
while i<=num:
    if i%2!=0:
        sum=sum+i
    i=i+1
print ('Sum of odd numbers',sum)
while i<=num1:
    if i%2==0:
        sum=sum+i
    i=i+1
print ('Sum of even numbers',sum)


print("---------4------------------")
num1 = int(input("enter the number1::"))
num2 = int(input("enter the number2::"))
for i in range(num1,num2 + 1):
    if i >1 :
        for num in range(2,i):
            if i%num ==0:
                break

        else:
            print(num," is prime number")




lower = 900
upper = 1000
lower = int(input("enter the number:"))
upper = int(input("enter the number2: "))
# print("Prime numbers between",lower,"and",upper,"are:")
for num in range(lower,upper + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)



print("FIND DUPLICATES AND PRINT WITHOUT ONLY UNIQUE VALUES IN ASCENDING-------5----------------------------")
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
    # print(final_list)
    # print(final_list.sort(key=Remove(duplicate)))


# Driver Code
duplicate = [1,2,1,6,3,4,5,2,3,1]
# Remove(duplicate)
# print(Remove().sort(key=Remove(duplicate)))
y = Remove(duplicate)
y.sort()
print(y)
# print(Remove(duplicate))


print("COUNT LIST DUPLICATES-----------------------------6-------------------------------------------")
list = ["1","2","3","1","5","4","3","2"]
print([[l,list.count(1)] for l in set(list)])
print(dict((l,list.count(1))for l in set(list)))





print("-------------convert upper into lower and lower into uppercase.prg-----------------------")
str = "I Am LaKKi"
newstr = ""
for i in str:
    if i.isupper() == True:
        newstr += i.lower()
    elif i.islower() == True:
        newstr += i.upper()
    elif i.isspace() == True:
        newstr += i
print(newstr)










































