class IntToRoman:
    romanNums = {"0":"","1":"I","2":"II","3":"III","4":"IV","5":"V","6":"VI","7":"VII","8":"VIII","9":"IX"}
    roman10Nums = {"0":"","1":"X","2":"XX","3":"XXX","4":"XL","5":"L","6":"LX","7":"LXX","8":"LXXX","9":"XC"}

    def calc(self,x): 
        a = []
        for i in str(x)[::-1]:
            a.append(i)

        if x < 10:
            return self.romanNums[a[0]]
        else:
            return self.roman10Nums[a[1]] + self.romanNums[a[0]]

class RomanToInt:
    ints = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    specNum = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}

    def calc2(self,x:str):
        rTotal = 0
        for i in self.specNum.keys():
            if x.find(i) != -1:
                rTotal += self.specNum[i]
                x= x.replace(i,"")
        for i in self.ints.keys():
            ixi = x.count(i)
            rTotal += ixi * self.ints[i]
        return rTotal