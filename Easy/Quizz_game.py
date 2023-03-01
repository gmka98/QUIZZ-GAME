print("Welcome to my Quiz Game!")

playing = input("Are you ready? ")

if playing.lower() != "yes":
    quit()
else:
    print("Let's go!")    

score = 0

answer = input("Who works as both a backend and front-end developer? ")
if answer.lower() == "a full stack developer":
    print('Correct!')
    score += 1
else: 
    print("Wrong!") 

answer = input("What language is commonly used for web development? ")
if answer.lower() == "javascript":
    print('Correct!')
    score += 1
else: 
    print("Wrong!")   

answer = input("What does CSS stand for? ")
if answer.lower() == "cascading style sheets":
    print('Correct!')
    score += 1
else: 
    print("Wrong!") 

answer = input("What is the primary function of a database? ")
if answer.lower() == "store and organize data":
    print('Correct!')
    score += 1
else: 
    print("Wrong!") 

answer = input("What is a commonly used version control system for software development? ")
if answer.lower() == "git":
    print('Correct!')
    score += 1
else: 
    print("Wrong!") 

answer = input("What is the purpose of a loop in programming? ")
if answer.lower() == "repeat a sequence of instructions":
    print('Correct!')
    score += 1
else: 
    print("Wrong!")  

answer = input("What is an API? ")
if answer.lower() == "application programming interface":
    print('Correct!')
    score += 1
else: 
    print("Wrong!")        

answer = input("What is the purpose of a function in programming? ")
if answer.lower() == "perform a specific task":
    print('Correct!')
    score += 1
else: 
    print("Wrong!")        

print("You got " + str((score / 8) * 100) + "% of questions correct!") 
