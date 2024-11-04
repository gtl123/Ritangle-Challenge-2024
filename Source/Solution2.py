"""
@GAURAV SHUKLA
Code Notes:
"Count carefully and you will see that this sentence contains X words and between them they contain Y vowels."
valid = (17 + len(X words) + len(Y words)) = X  & vowels(X words + Y words)+31 = Y
THIS CODE IS PURPOSELY NOT EFFICIENT RATHER IT IS VERY COMPACT AND PRIORITISES THE LEAST LINES
"""
ones ,teens,tens = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"], ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
cast = lambda num : ((ones[num]) if 1 <= num <= 9 else (teens[num - 10] if 11 <= num <= 19 else tens[num // 10] + (" " + ones[num % 10] if num % 10 != 0 else "") if 10 <= num < 100 else None))
vc = lambda word: int(sum(1 for char in word if char.lower() in "aeiou"))
valid = lambda X,Y: (True if ((17+len(cast(X).split())+len(cast(Y).split()))  == X and (vc(cast(X))+vc(cast(Y)) + 31) == Y)  else False)
ans = sum([item for sublist in [[ X * Y if valid(X,Y) else 0 for Y in range(31,99)] for X in range(17,99)] for item in sublist])
print(ans)