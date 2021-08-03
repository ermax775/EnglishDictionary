import json
from difflib import get_close_matches

data = json.load(open("data.json"))
ans = 'z'
while (ans == 'z'):
    
    def translate(word):
        word = word.lower()
        if word in data:
            return data[word]
        elif word.title() in data:
            return data[word.title()]
        elif word.upper() in data:
            return data[word.upper()]
        elif len(get_close_matches(word , data.keys())) > 0 :
            print("\n Did you mean %s instead" %get_close_matches(word, data.keys())[0])
            decide = input("\n press y or Y for yes or press N or n for no\n")
            if decide == "y" or decide == "Y":
                return data[get_close_matches(word , data.keys())[0]]
            elif decide == "n" or decide == "N":
                return("\n Sorry, you have entered a word not in this dictionary \n")
            else:
                return("\n You have entered wrong input please enter just y or n\n")
        else:
            print("\n Sorry, you have entered a word not in this dictionary\n")



    word = input("\n Enter the word you want to search\n")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)


    ans = input("\n Do you want to continue?\n Press 'z' or 'Z' to continue, or any other key to exit: \n")
print("\n Terminating Dictionary. Good-Bye!!!")
