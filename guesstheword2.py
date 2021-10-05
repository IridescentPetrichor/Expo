score = 0

print('Guess the word!')
guess1 = input('which bear lives at the north pole?')
def check_guess(guess_answer):
    global score
    if guess1 == answer:
        print('Correct Answer')
        score = score + 1
