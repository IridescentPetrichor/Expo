import random

answerlist = ["world","look","hello","goodbye"]

random.shuffle(answerlist)

answer = list(answerlist[0]) #answer = w,o,r,l,d

#print(answer)

#empty list called display
display = []

#adds the variable answer to display
display.extend(answer)

#print(used)

#iterates through the list 'display'

for i in range (len(display)):
    #replaces each index in the list with '_'
    display[i] = "_"

#the join command puts a space between each '_'
print (' '.join(display))
print()

#counter stops the game once all letters have been guessed
count = 0

#keeps asking the user until all letters guessed
while count < len(answer):
    guess = input("Please guess a letter: ")
    guess = guess.lower()
    print (count)

    #iterates through the letters in answer
    for i in range(len(answer)):
        #if the guessed letter matches a letter
        #in the answer
        if answer[i] == guess :
            #replace the index of that guess with
            #the actual letter they guessed
            display[i] = guess
            count = count + 1

            #print (used)

    #print out the new string with guessed letters in
    print (' '.join(display))
    print()

print("Well done, you guessed the word!")