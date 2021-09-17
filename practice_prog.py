import practice_mod

# below code changes number to roman numerals.
num = int(input("Type a number to convert to Roman Numerals:  "))
abc = practice_mod.IntToRoman()

retVal = abc.calc(num) 

print(retVal)


# below code changes roman numerals to numbers
xyz = practice_mod.RomanToInt()
retVal = xyz.calc2("MCMXCIX")
print(retVal)
