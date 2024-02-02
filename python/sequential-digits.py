class Solution:
    # arr = [12, 23, 34, 45, 56, 67, 78, 89, 123, 234, 345, 456, 567, 678, 789, 1234, 2345, 3456, 4567, 5678, 6789, 12345, 23456, 34567, 45678, 56789, 123456, 234567, 345678, 456789, 1234567, 2345678, 3456789, 12345678, 23456789, 123456789]
    def generateValidNumber(self,starting , length):
        if(starting+length-1 > 9):
            # print(starting, length)
            return False
        tempstr = ""
        for i in range(length):
            tempstr+= str(starting + i)
        return int(tempstr)
        
    def sequentialDigits(self,low, high):
        if(low>123456789):
            return []
        lengthOfLow = len(str(low))
        startingDigit = int(str(low)[0])
        currentLength = lengthOfLow
        foo = True
        ans = []
        while(foo):
            num = self.generateValidNumber(startingDigit,currentLength)
            if num == False:
                # print("here1")
                currentLength+=1
                startingDigit = 1
            else:
                if num < low:
                    startingDigit += 1
                if num >= low and num <= high:
                    # print("here2")
                    ans.append(num)
                    startingDigit = int(str(num)[0])
                    if str(num)[-1] == 9:
                        currentLength+=1
                    else:
                        startingDigit+=1
                if num > high:
                    # print("here3")
                    foo = False
                if num == 123456789:
                    return ans
            # print(num)
        return ans


something = Solution()
# yes = something.sequentialDigits(10, 1000000000)
# yes = something.sequentialDigits(58 , 155)
yes = something.sequentialDigits(1000 , 13000)
print(yes)

# 372591426
# 123456789