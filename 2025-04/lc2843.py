class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        low_ = str(low)
        i = low if len(low_)%2 == 0 else 10**(len(low_))
        while i <= high:
            num_ = str(i)
            n = len(num_)
            if n%2 != 0:
                i *= 10
                continue
            a=int(num_[:n//2])
            b=int(num_[n//2:])
            num1,num2=0,0
            while a:
                num1+=a%10
                a//=10
            while b:
                num2+=b%10
                b//=10
            if(num1==num2):
                res+=1
            i += 1
        return res
s = Solution()
print(s.countSymmetricIntegers(100,1782))