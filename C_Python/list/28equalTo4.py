# 28. Display elements from list having length equal to 4 using list comprehension

lst = ["navaj","mujir","mahi","sam",]
equal_to_4 = [word for word in lst if len(word) == 4 or len(word) == 3]     # take the word and compare the len with the word consider the len is 4 or 3
print("this word of length equal to the 4 :",equal_to_4)