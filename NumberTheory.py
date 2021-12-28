num = int (raw_input ("Please give me an integer (negative integer to quit):"))

while num >= 0:
    if num <= 9:
        print "Multiplicative and Additive Persistence:",0,"additive and digital root:",num
    else:
        addCnt = 0
        prodCnt = 0

        print "\nMultiplicative loop"
        mRoot = num
        while mRoot > 9:
            theProd = 1
            calcNumber = mRoot
            while calcNumber > 9:
                digit = calcNumber%10
                calcNumber = calcNumber/10
                theProd *= digit
            theProd *= calcNumber
            mRoot = theProd
            prodCnt +=1
            print "product:",theProd

        print "\nAdditive loop"
        aRoot = num
        while aRoot > 9:
            theSum = 0
            calcNumber = aRoot
            while calcNumber > 9:
                digit = calcNumber%10
                calcNumber = calcNumber/10
                theSum += digit
            theSum += calcNumber
            aRoot = theSum
            addCnt +=1
            print "sum:",theSum
        print "\nFor the integer:",num
        print "\t Additivie Persistence: ",addCnt,", Additive Root:", aRoot
        print "\t Multiplicative Persistence: ",prodCnt,", Multiplicative Root:", mRoot
        print ""
    num = int (raw_input("Please give me an integer (negative integer to quit):"))

print "Thanks for playing"