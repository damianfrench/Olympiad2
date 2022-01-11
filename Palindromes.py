def main():
    # num = input("enter your number")
    # print(nextBiggest(num))
    print(countingPalindromes())
    print(1097*1097)
def nextBiggest(num):
    intNum = int(num)
    # if len(num) % 2 == 0:
    #     position = int(num[int(len(num)/2)])
    #     intNum+=(10**position)+(10**(position-1))
    # else:
    #     position = int(num[int((len(num)+1)/2)])
    #     intNum += (10**position)
    # return intNum

    if len(num)%2==0:
        middleNums=[int((len(num)/2)-1),int(len(num)/2)]
        if num[middleNums[0]]>num[middleNums[1]]:
            reversedPart=reversing(int(num[0:middleNums[1]]))
            intNum-=int(num[middleNums[0]+1:len(num)])
            intNum+=reversedPart

        else:
            reversedPart=reversing(int(num[0:middleNums[1]])+1)
            position = int(len(num) / 2)
            intNum-=int(num[middleNums[0]+1:len(num)])
            intNum+=10**position
            intNum+=reversedPart
    else:
        middle=int((len(num)+1)/2)-1
        if num[middle]<num[middle+1]:
            reversedPart=reversing(int(num[0:middle]))
            position=int(len(num)/2)
            intNum-=int(num[middle+1:len(num)])
            intNum+=10**position
            intNum+=reversedPart
        else:
            reversedPart=reversing(int(num[0:middle]))
            intNum-=int(num[middle+1:len(num)])
            intNum+=reversedPart


    return intNum
        


def reversing(nonReversedPart):
    reversedPart = 0

    while nonReversedPart != 0:
        digit = nonReversedPart % (10)
        reversedPart = reversedPart * 10 + digit
        nonReversedPart //= 10
    return reversedPart

def countingPalindromes():
    count=0
    for x in range(1,99999):
        if reversing(x)==x:
            print(x)


if __name__ == '__main__':
    main()

    #123321
    #12321
    #1354834
    # if even, look at middle 2, if first one bigger then flip the first half. if not then add 1 to the first one then flip it. if odd, if middle number if smaller than one to the right, then add 1
    #and copy the rest of the left side, otherwise just make left side of middle the same as right side.

#github token : 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
