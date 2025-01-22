    
def numberToWords(num: int) -> str:
    d = {0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion"}
    mag = list(d.keys())
    res = ''

    if num < 20:
        return d[num]
    
    def helper(n: int):
        if n == 0:
            return ""
        r = ""
        if n < 20:
            return d[n] + " "
        elif n < 100:
            tens = (n//10) * 10
            r += d[tens] + " "
            if n % tens != 0:
                r += d[n%tens] + " "
        else:
            hundreds = (n//100)
            r +=  d[hundreds] + " "+  d[100] +" "+ helper(n%100)
        return r
    
    while num > 0:
        c = num // mag[-1]
        if c > 0:
            if num < 1000:
                res += helper(num)
                break
            num -= mag[-1]*c
            res += helper(c) + d[mag[-1]] + " "
        mag.pop()


    return res.strip()

print(numberToWords(100))
