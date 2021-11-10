eight_things = "Dogs Cats Hamsters Gerbils GuineaPigs SugarGlider"

print("There aren't eight things on that list.")

stuff = eight_things.split(' ')
more_stuff = ["Tiger", "Lion", "Koala", "Eagle", "Sloth"]

while len(stuff) != 10:
    next_one = more_stuff.pop
    print("Adding: "), next_one
    stuff.append(next_one)
    print("There's %d items now.") % len(stuff)

print("There we go: "), stuff

print("Let's do lots of things!")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))



