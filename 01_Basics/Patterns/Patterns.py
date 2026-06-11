




class Patterns:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    
    def dashedLine(self):
        print("=============================================\n\n")


    def printSquareOfStars(self):
        for i in range(self.row):
            for j in range(self.col):
                print("*", end=" ")
            print("\n")
        self.dashedLine()
 

    def patternOfOnesAndTwos(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.col - j, end=" ")
            print("\n")
        self.dashedLine()

    def trianglePattern(self):
        for i in range(self.row):
            for j in range(i + 1):
                print("*", end=" ")
            print("\n")
        self.dashedLine()

    def triangluarRowPattern(self):
        for i in range(self.row):
            for j in range(i + 1):
                print(i + j + 1, end=" ")
            print("\n")
        self.dashedLine()


    def triangluarRowPatternReverse(self):
        for i in range(1, self.row):
            for j in range(1, i + 1):
                print(i - j + 1, end=" ")
            print("\n")
        self.dashedLine()

    def charPattern(self):
        charValue = 65 #Stores A
        for i in range(1, self.row):
            for j in range(1, self.col):
                print(chr(charValue + j - 1), end=" ")
            print("\n")
        self.dashedLine()

    
    def charPatternTriangle(self):
        value = 65

        for i in range(self.row):
            for j in range(i + 1):
                print(chr(value + i + j), end=" ")
            print("\n")
        self.dashedLine()


    def charPatternTriangleReverse(self):
        value = self.row - 1

        for i in range(self.row):
            for j in range(i + 1):
                print(chr(65 + value + j ), end=" ")
            value -= 1
            print("\n")
        self.dashedLine()


    def invertedRightAngledTriangle(self):
        for i in range(1, self.row + 1):
            j = 0
            spaces = self.row - i
            #print spaces
            while spaces:
                print(" ", end="")
                spaces -= 1
                j += 1
            #print stars
            while j < self.col:
                print("*", end="")
                j += 1
            print('\n')
        self.dashedLine()
    


    def dummyPattern(self):
        for i in range(self.row):
            #Number of spaces
            spaces = i
            while spaces:
                print(" ", end="")
                spaces -= 1
            for j in range(self.col - i):
                print(i + 1, end="")
            print("\n")
        self.dashedLine()


    def dummyPatternSecond(self):
        for i in range(self.row):
            #Number of spaces
            spaces = i
            while spaces:
                print(" ", end="")
                spaces -= 1
            for j in range(self.col - i):
                print(i, end="")
            print("\n")
        self.dashedLine()


    

    def pascalsTriangle(self):
        for i in range(1, self.row + 1):
            #Print spaces
            spaces = self.row - i
            while spaces:
                print(" ", end="")
                spaces -= 1
            #Print first triangle
            for j in range(1, i + 1):
                print(j, end="")
            #Print second triangle
            start = i - 1
            for k in range(1, start + 1):
                print(k, end="")
            print("\n")
        self.dashedLine()

    def dabbangPattern(self):
        for i in range(self.row):
            #Print first part
            for j in range(self.row - i):
                print(j + 1, end=" ")
            numStars = 2 * i

            #Print second part
            for k in range(numStars):
                print("*", end=" ")

            #Print third part
            start = self.row - i
            while start:
                print(start, end=" ")
                start -= 1

            print("\n")

    def zerosOnesPattern(self):
        for i in range(self.row):
            for j in range(i + 1):
                print("1", end=" ") if not (i + j) % 2 else print("0", end=" ")
            print("\n")

    def uPattern(self):
        for i in range(1, self.row + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
        
            spaces = 2 * self.row - 2 * i
            while spaces:
                print(" ", end=" ")
                spaces -= 1
            
            for j in range(i, 0, -1):
                print(j, end=" ")

            print("\n")

        
    def patternOfAB(self):
        for i in range(1, self.row + 1):
            spaces = self.row - i

            while spaces:
                print(" ", end="")
                spaces -= 1
            for j in range(i):
                print(chr(65 + j), end="")

            for k in range(i, 1, - 1):
                print(chr(65 + k - 2), end="")

            print("\n")

    def diamond(self):
        for i in range(self.row):
            for j in range(self.row - i):
                print("*", end="")

            spaces = 2 * i
            while spaces:
                print(" ", end="")
                spaces -= 1
            for j in range(self.row - i):
                print("*", end="")
            print("\n")

        for i in range(1, self.row + 1):
            for j in range(i):
                print("*", end="")
            spaces = 2 * self.row - 2 * i
            while spaces:
                print(" ", end="")
                spaces -= 1
            
            for j in range(i):
                print("*", end="")
            print("\n")

        

            
            

            


            


        


        

    

    


#Square pattern
print("\nPattern 01:\n")
squarePattern = Patterns(5, 5)
squarePattern.printSquareOfStars()

#Pattern of ones and twos
print("\nPattern 02:\n")
onesTwosPattern = Patterns(5, 4)
onesTwosPattern.patternOfOnesAndTwos()


#Triangle pattern
print("\nPattern 03:\n")
trianglePattern = Patterns(5, 4)
trianglePattern.trianglePattern()

#Triangular row pattern
print("\nPattern 04:\n")
triangluarRowPattern = Patterns(5, 5)
triangluarRowPattern.triangluarRowPattern()


#Triangluar row pattern in reverse order
print("\nPattern 05:\n")
triangluarRowPatternReverse = Patterns(5, 5)
triangluarRowPatternReverse.triangluarRowPatternReverse()

#Character pattern
print("\nPattern 06:\n")
charPattern = Patterns(5, 5)
charPattern.charPattern()

#Character pattern triangle
print("\nPattern 07:\n")
charPatternTriangle = Patterns(5, 5)
charPatternTriangle.charPatternTriangle()

#Character pattern triangle in reverse
print("\nPattern 08:\n")
charPatternTriangleReverse = Patterns(5, 5)
charPatternTriangleReverse.charPatternTriangleReverse()


#Inverted right triangular pattern
print("\nPattern 09:\n")
invertedRightAngledTriangle = Patterns(5, 5)
invertedRightAngledTriangle.invertedRightAngledTriangle()

#Dummy pattern
print("\nPattern 10:\n")
dummyPattern = Patterns(5, 5)
dummyPattern.dummyPattern()


#Pascals triangle
print("\nPattern 11:\n")
pascalsTriangle = Patterns(5, 8)
pascalsTriangle.pascalsTriangle()


#Dabbang pattern
print("\nPattern 12:\n")
dabbangPattern = Patterns(5, 5)
dabbangPattern.dabbangPattern()

#Pattern of 0's and 1's
print("Pattern 13: \n")
zerosOnes = Patterns(5, 5)
zerosOnes.zerosOnesPattern()
zerosOnes.dashedLine()

#U pattern
print("Pattern 14: \n")
uPattern = Patterns(5, 5)
uPattern.uPattern()
uPattern.dashedLine()

#Pattern of AB's
print("Pattern 15: \n")
patternOfAB = Patterns(5, 5)
patternOfAB.patternOfAB()
patternOfAB.dashedLine()

#Diamond pattern
print("Pattern 16: \n")
diamond = Patterns(5, 5)
diamond.diamond()
diamond.dashedLine()