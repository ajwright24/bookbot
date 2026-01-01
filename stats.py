def count_words(contents):
    words = contents.split()
    return len(words)

def count_unique_char(contents):
    char_list = list(contents.lower())
    unique_char_set = set(char_list)
    char_dict = {}

    for unique_char in unique_char_set:
        char_dict[unique_char] = 0 #initialize value 
        for char in char_list:
            if char == unique_char:
                char_dict[unique_char] += 1

    return char_dict



#loop each key and make it the value of the new key "char"
# make a key value pair with the new key "num" and the value the count
# call a function that takes a dictionary and sorts it by number greatest to least (not created yet)
# return the sorted dictionary 

#def sorted_list(dict):
    #for key in dict:


