'''
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

'''

class Solution:
    def countAndSay(self, n: int) -> str:
        start="1"
        # print(len(start))
        # print(start[0])
        for i in range(n-1):
            count=0
            res=''
            var=start[0]
            for char in start:
                if(char==var):
                    count+=1
                else:
                    res += str(count)+var
                    var=char
                    count=1
            res += str(count)+var
            start = res
        return start