def longest_word(w):
    largest =0
    for word in w:
        if len(word) > largest:
            largest= len(word)
    print("longest word is:",word)
    return largest 
return_value = longest_word(["python","java","c++","javascript"])
print("longest word length is:",return_value)