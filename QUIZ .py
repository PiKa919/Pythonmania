#introductory line
print("Welcome to the Quiz!")
print("Please answer the following questions with either 'yes' or 'no'.")

#entry question
playing = input("Are you playing? ")

if playing.lower() != "yes":
    quit()

print("Okey, let's get started! :)")
score = 0

answer = input("Which was the world's first Search engine? ")
if answer.casefold() == "archie":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("Which  company invented USB? ").lower()
if answer == "intel":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What is the maximum size of a Word Document? ")
if answer == "32MB":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("What was the name of the first computer? ").upper()
if answer == "ENIAC":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("Quiz Results: You got " + str(score) + "/4 correct ")
print("Quiz Results: You got " + str((score/4)*100) + "% correct ")
