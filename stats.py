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



# create an empty list to store the dictionaries 
# create a new dictionary with two k:v inputs, {name: "", num: ""}
# loop the data from the unique characters into the dictionary
# pass the information into the dictionaries then append them to the list of dictionaries
# call a helper function that takes a list of dictionaries and sorts it by number greatest to least
# return the sorted dictionary 

def sorted_list(dict):
    list_of_dictionaries = []

    for k, v in dict.items():
        char_dict = {"name": k, "num": v}
        list_of_dictionaries.append(char_dict)
    list_of_dictionaries.sort(key=sort_on, reverse=True)
    return list_of_dictionaries

    #for d in list_of_dictionaries:
    #    print(f"{d["name"]}: {d["num"]}")

def sort_on(item):
    return item["num"]

    


