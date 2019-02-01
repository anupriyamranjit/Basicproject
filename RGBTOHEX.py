red = int(input("What is the RBG value for red"))
green = int(input("What is the RBG value for green"))
blue = int(input("What is the RBG value for blue"))
import math
letters="A B C D E F".split()

def toHex(r, g, b):
    red1=math.floor(r/16)
    if red1>9:
        red1=letters[red1-10]
    red2=r%16
    if red2>9:
        red2=letters[red2-10]
    green1=math.floor(g/16)
    if green1>9:
        letters[green1-10]
    green2=g%16
    if green2>9:
        green2=letters[green2-10]
    blue1=math.floor(b/16)
    if blue1>9:
        blue1=letters[blue1-10]
    blue2=b%16
    if blue2>9:
        blue2=letters[blue2-10]
    red1=str(red1)
    red2=str(red2)
    green1=str(green1)
    green2=str(green2)
    blue1=str(blue1)
    blue2=str(blue2)
    hex=red1+red2+green1+green2+blue1+blue2
    return hex




def toRGB(h):
    mylist=[]
    for i in h:
        mylist.append(i)
        if i == "A":
            mylist[mylist.index('A')] = '10'
        if i == "B":
            mylist[mylist.index('B')] = '11'
        if i == "C":
            mylist[mylist.index('C')] = '12'
        if i == "D":
            mylist[mylist.index('D')] = '13'
        if i == "E":
            mylist[mylist.index('E')] = '14'
        if i == "F":
            mylist[mylist.index('F')] = '15'
    mylist=list(map(int, mylist))

    red= (mylist[0]*16) + mylist[1]
    green= (mylist[2]*16) + mylist[3]
    blue= (mylist[4]*16) + mylist[5]

    rgb="RGB({},{},{})".format((red),(green),(blue))
    return rgb



print()
print("RGB({},{},{})".format(str(red),str(green),str(blue)))
print("")
myhex=toHex(red,green,blue)
print("To Hexadecimal-\n#" + myhex)
print("\nBack to RGB -")
print(toRGB(myhex))
