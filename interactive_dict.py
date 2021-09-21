import json
from difflib import get_close_matches

class dict:

    def __init__(self,wrd):
        self.wrd=wrd


    data = json.load(open("data.json"))
    #print(data["rain"])
    def find(self,user_word):
        user_word = user_word.lower()
        if user_word in self.data:
            return self.data[user_word]
        elif user_word.title() in self.data:  # if user entered "delhi" this will check for "Delhi" as well.
            return self.data[user_word.title()]
        elif user_word.upper() in self.data:  # in case user enters words like USA or NATO
            return self.data[user_word.upper()]
        elif len(get_close_matches(user_word, self.data.keys()))>0:
            yn = input("Did you mean %s instead? Enter Y if yes, or N if no : " % get_close_matches(user_word, self.data.keys())[0])
            if yn == 'Y' or yn == 'y':
                t=self.data[get_close_matches(user_word, self.data.keys())[0]]
                return t
            elif yn == 'N' or yn == 'n':
                return "Word does not exists"
            else:
                return 'Enter correct choice'
        else:
            return "Word not found"

    #def print_interactive_dict(self,output):


d=input("Enter word :")
d1=dict(d)
output = d1.find(d)

if type(output) == list:
    count = 1
    for item in output:
        print("{}.{}".format(count, item))
        count += 1
else:
    print(output)
