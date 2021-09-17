import practice_mod

# Hash out one program to run and vice versa.

# Below code changes number to roman numerals.
num = int(input("Type a number to convert to Roman Numerals:  "))
abc = practice_mod.IntToRoman()
retVal = abc.calc(num) 
print(retVal)


# Below code changes roman numerals to numbers.
xyz = practice_mod.RomanToInt()
retVal = xyz.calc2("MCMXCIX")
print(retVal)
