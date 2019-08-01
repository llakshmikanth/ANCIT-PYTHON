print("1:stating process")
print("2;using class&fun&methodes")
# lii = input("enter the list values::")
# strlii = lii.split(",")
# print(strlii)
# t1 = tuple(strlii)
# print(t1)
#
# for x in strlii:
#     print(int(x))
print("-------------11------Input: 34,67,55,33,12,98['34', '67', '55', '33', '12', '98'],"
"('34', '67', '55', '33', '12', '98'),"
"-------------------------------")
class commasepstr:
    def __init__(self):
        pass
        # self.lii = lii
        # print(self.lii)
    def commasepstrr(self):
        lii = input("enter the list of  values::")
        strlii = lii.split(",")
        print("list separeted using split",strlii)
        t1 = tuple(strlii)
        print("list converted into tuple",t1)
        list1 = []
        for x in strlii:
            y = int(x)
            list1.append(y)
        print("list separeted like a number",list1)


if __name__ == "__main__":
    print("hi")
    css = commasepstr()
    css.commasepstrr()





print("----------------------------12----------------print the pow of num using dic{}---------------------------")
#we can using list methodprint(d)
'''
l = []
for x in range(1,n+1):
    m = x*x
    l.append(m)
print(l)
'''
class powdic:
    def __init__(self,n = int(input("Input a number:: "))):
        self.n = n
        # n = int(input("Input a number:: "))
        d = {}
        for x in range(1, n + 1):
            d[x] = x * x
        print(d)
pd = powdic()


print(""----------------------14--------------------------------------------------"")
items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))

class inputcommasepofwords:
    def __init__(self):
        pass
    def word(self,str= input("Input comma separated sequence of words::")):
        self.str = str
        words = [word for word in str.split(",")]
        print(",".join(sorted(list(set(words)))))

itcsofwrds = inputcommasepofwords()
itcsofwrds.word()




print("-------------calculate chrecrecter and digit in string----------------")
# s = input("Input a string::")
# d=l=0
# for c in s:
#     if c.isdigit():
#         d=d+1
#     elif c.isalpha():
#          l=l+1
#          print(l)
#     # else:
#     #     pass
# print("Letters", l)
# print("Digits", d)


class calalphaanddigit:
    def __init__(self,s = input("Input a string::")):
        self.s = s
        d=l=0
        for c in s:
            if c.isdigit():
                d=d+1
            elif c.isalpha():
                l=l+1
        else:
            pass
        print("Letters", l)
        print("Digits", d)

alpdig = calalphaanddigit()




print("---------------------------------15------------------------------------------")
from collections import Counter


def remov_duplicates(input):
    input = input.split(" ")

    for i in range(0, len(input)):
        input[i] = "".join(input[i])
        input.sort()

    UniqW = Counter(input)
    s = " ".join(UniqW.keys())
    print(s)


if __name__ == "__main__":
    input = 'hello world and practice makes perfect and hello world again '
    remov_duplicates(input)


print("--------------------------")














