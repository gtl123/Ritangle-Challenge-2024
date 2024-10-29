import inflect
p = inflect.engine()


print(p.number_to_words(99).replace("-"," "))

def Calculate_vowels(str):
    count =  0
    for vowel in ["a", "e", "i" ,"o", "u"]:
        count += str.lower().count(vowel)
    return count

def Word_count(str):
    return  len(str.split(sep=" "))



print(Calculate_vowels("Hello People"))

Sentence = "Count Carefully and you will see that this sentence contains words and between them they contain vowels."
