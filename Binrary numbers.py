import math

number = int(input("Enter a number: "))
BSize = int(input("Enter a bit size: "))
while math.pow(2, BSize) - 1 < number:
    BSize = int(input("Please try again! Enter a bit size: "))

def BNumber(number, BSize):
    pos = -1
    x = 1
    binary = ""
    num = ""
    for i in range(BSize):
        if math.pow(2, BSize - x) <= number:
            number = number - math.pow(2, BSize - x)
            x = x + 1
            binary = binary + "1"
        else:
            binary = binary + "0"
            x = x + 1

    binaryList = list(binary)
    for y in range(len(binaryList)):
        if binaryList[y] == "1":
            binaryList[y] = "0"
        elif binaryList[y] == "0":
            binaryList[y] = "1"
    binary = ''.join(binaryList)

    NBinary = int(binary, 2) + 1
    NBinaryList = list(bin(NBinary)[2:])
    while len(NBinaryList) < BSize:
        NBinaryList.insert(0, '0')
    for t in range(len(NBinaryList)):
        if NBinaryList[pos] == "2":
            NBinaryList[pos] = "0"
            NBinaryList[pos-1] = str(int(NBinaryList[pos-1]) + 1)
            pos = pos + 1
    NBinary = ''.join(NBinaryList)

    return NBinary

print(BNumber(number, BSize))
