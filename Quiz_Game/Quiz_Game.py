print("Welcome to quiz game!")

playing = input("Shall we begin? ")

if playing.lower() != "yes":
        quit()
        
print("OK!, Let's play! ;)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
        print("Correct!")
        score += 1
else:
        print("Incorrect!")
        

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
        print("Correct!")
        score += 1
else:
        print("Incorrect!")
        
        
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
        print("Correct!")
        score += 1
else:
        print("Incorrect!")
        
        
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
        print("Correct!")
        score += 1
else:
        print("Incorrect!")
        
print(f"You got {score} question(s) correct!")
print(f"You got {score/4*100} %.!")