import random

import string

adjectives = ['sleepy','slow','smelly','wet','fat','red','orange','green','purple','fluff','white','proud','brave',]
print('Welcome to password picker!')
nouns = ['goblin','america','clockworkVoluminous','stubbornRomeo','bejeweledFace','arsenicCheeseburger','diamondDomination','underprivilegedIntelligence','englishRebirth','conditionalMarksman','arachnidsTroubadour']
adjective = random.choice(adjectives)
noun = random.choice(nouns)
number = random.randrange(0,1000)
special_char = random.choice(string.punctuation)

password = adjective + noun + str(number)+ special_char
print('Your new password is %s' %password)