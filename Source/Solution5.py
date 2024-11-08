"""
1-999 list in english
in alphabetical order
start
8,18,800,808 .... 202
THIS CODE IS PURPOSELY NOT EFFICIENT RATHER IT IS VERY COMPACT AND PRIORITISES THE LEAST LINES
"""
import inflect , word2number.w2n
e = inflect.engine()
nums = sorted([e.number_to_words(num).replace("-"," ") for num in range(1,1000)])
print(f"ans:{sum([word2number.w2n.word_to_num(nums[idx]) for idx in range(nums.index("eight")+1, nums.index("nine"))])}")