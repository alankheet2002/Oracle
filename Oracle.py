import random
#creating a function that reads the .txt file into the function.
def answer_me(): 
    with open('oracle_answers.txt') as f:
        text = f.read()
        lines = text.split('\n')
        return random.choice(lines).strip()

for i in range(1):
    print(i, ":", answer_me())

def oracle():
    state = ''
    while state != "Q":
        state = input("To ask a question, enter A. To quit enter Q: ")
        if (state == "A"):
            question = input("Enter a yes/no question: ")
            if (question !="" and "?" in question): 
                print(answer_me())
            else: 
                print("It is empty or no question mark")
                
        elif (state == "Q"): 
            print("You quit the oracle")  
