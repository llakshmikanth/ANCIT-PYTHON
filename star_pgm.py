def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")


say_hello("lakki")
a = greet_bob(say_hello)
print(a)

def simple_decor(func):
  def inner(p,v):
    p *= 10
    v *= 20
    return func(p,v)
  return inner

@simple_decor
def fun(a,b):
  c = a+b
  print(c)
  return c

fun(4,5)





'''
from itertools import izip

with open("demofile4") as textfile4, open("demofile3") as textfile3: 
    for x, y in izip(textfile4, textfile3):
        x = x.strip()
        y = y.strip()
        print("{0}\t{1}".format(x, y))'''




'''        
print("pgm.7-------------------------------------------")       
# rows
n = int(input("enter the row value::"))
assci=65
for i in range(0,n):
  for i in range(0,i+1):
    val=chr(assci)
    print(val,end=" ")
    assci+=1
  print()

'''



print("pgm.6-------------------------------------------")
'''
n = int(input("enter then row num::"))
#num = 1
for row in range(1,n+1):
  for col in range(1,row+1):
    print(num,end="  ")
    #num=num+1
  print()
  '''




'''
print("pgm.5-------------------------------------------")

f = open("newfilec.txt", "w")
f.write("Woops! I have deleted the content!")
f.write("\n")
f.write("i am lazy")
f.write("\n")
f.write("i can't do anything")
f.write("\n")
f.write("i am nothing!")
f.write("\n")
f.write("--------------------------------------------------------")
f.close()
'''



'''
print("pgm.4-------------------------------------------")
f = open("demofile4.txt", "r")
for x in range(5):
  print(f.readline())
f.close()
'''

'''
print("pgm.3-------------------------------------------")
tup = (22,33,44,26)
L1=list(tup)
L1[1]=55
L1[2]=63
tup=tuple(L1)
print(tup)
'''


'''
print("pgm.1-------------------------------------------")

num = int(input("enter the numer::"))
for i in range(num):
    for j in range(num-i):
        print(num-i,end="  ")
        
    print()
print("pgm.2-----------------------------------------")
    
for i in range(num):
    for j in range(i+1):
        print(i+1,end="  ")
    print()    
print("-----------------------------------------")     
for i in range(6):
    for j in range(5-i):
        print("#",end="")
        
    print()
    '''
#li = [1,2,1,4,3,2,1,5,6,3,6]
print("-------------------------------------------------")
'''
T1=(10,50,20,9,40,25,60,30,1,56)
L1=list(T1)
L1[5]=100
T1=tuple(L1)
print(T1)
#(10, 50, 20, 9, 40, 100, 60, 30, 1, 56)
'''

