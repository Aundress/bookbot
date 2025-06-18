def word_count(text):
    words = text.split()
    num_words = len(words)

    return num_words
def sort_list(list):
    print("Here in sort_list")
    return list["num"]
   

def create_dict_list(dict):
    expanded_dict = {}#[char,num]
    list_dict = []
    for d in dict:
        expanded_dict = {"char" : d, "num" : dict[d]} 
        list_dict.append(expanded_dict)
    
    return list_dict



def list_char_count(letter_dict):
    #take the dict and creat a list of dict
    dict_list = create_dict_list(letter_dict)
    dict_list.sort(reverse=True, key= sort_list)
    for letter in dict_list:
        if letter["char"].isalpha():
            character = letter["char"]
            num = letter["num"]
            print(f"The {character} character was found {num} times")
                



def letter_count(words):
    letters = {}
    
    for word in words:
        for letter in word:
            letter = word.lower()
            if letter not in letters:
                letters[letter] = 1
            elif letter in letters:
                letters[letter] += 1
    return letters

def read_file(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents