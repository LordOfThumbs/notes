import random

notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print('Play the right note! Press Q to quit.')
while True:
    test = random.choice(notes)
    print('Play: ', test)
    key = input()
    if key.lower() == 'q':
        break
    elif key == test:
        print('Correct!')
    else:
        print('Wrong!')