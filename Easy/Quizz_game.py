print("Welcome to my Quizzz GAAAAme!")

playing = input("Are you REEEEEAAAAAAAADYYYYYYYYY!? ")

if playing.upper() != "yes":
    quit()

print("Let's GOOOOOOO!")    
score = 0

answer = input("Who work as a backend and as a front-end ?")
if answer.upper == "A full stack developer":
    print('Correct!')
    score+=1

else: 
    print("Wrong!") 

answer = input()
if answer.upper == "A full stack developer":
    print('Correct!')
    score+=1

else: 
    print("Wrong!")   


answer = input()
if answer.upper == "A full stack developer":
    print('Correct!')
    score+=1

else: 
    print("Wrong!") 

answer = input()
if answer.upper == "A full stack developer":
    print('Correct!')
    score+=1

else: 
    print("Wrong!") 


answer = input()
if answer.upper == "A full stack developer":
    print('Correct!')
    score+=1

else: 
    print("Wrong!") 

answer = input()
if answer.upper == "A full stack developer":
    print('Correct!')
    score+=1

else: 
    print("Wrong!")  

answer = input()
if answer.upper == "A full stack developer":
    print('Correct!')
    score+=1


else: 
    print("Wrong!")          

answer = input()
if answer.upper == "A full stack developer":
    print('Correct!')
    score+=1

else: 
    print("Wrong!")        

print("You got" + str((score / len(answer) * 100) + "%.") + "questions correct!")
