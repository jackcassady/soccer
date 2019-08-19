# import random for goalkeeper position
import random as rnd

# Counter for score
goals = 0
attempts = 0

# Intial screen
print('\nScore = ' + str(0))
print('\nTo quit type "quit"')

# Store shot value for this attempt
shot = ''

# Available options for shots
shot_options = ['top left', 'top right', 'bottom left', 'bottom right']

# Begin loop
while True:

    # Goalie position
    goalie = rnd.randint(1, 2)

    # Direction of shot as given by user
    def shot_location():

        if 'top left' in shot:
            return 1
        elif 'top right' in shot:
            return 2
        elif 'bottom right' in shot:
            return 2
        elif 'bottom left' in shot:
            return 1

    # Input of the user to give the shot location
    # Stored in shot string above
    shot = input('\ntop left, top right, bottom left or bottom right: ')

    # If user inputs quit the loop stops
    if shot == 'quit':
        print('\nGood Game!')
        break

    # If user gives invalid location or misspells location
    # outputs 'Try Again' but does not end the loop
    if shot not in shot_options:
        print('\nTry Again')
        continue

    # Given shot location and goalie position determines score
    # If goalie chooses different direction from user input
    # a goal is score and the score is updated
    if goalie == shot_location():
        attempts += 1
        print('\nScore = ' + str(goals) + '/' + str(attempts))
        print('\nSAVED!')

    # If goalie and user choose the same direction goalie
    # saves the shot and no goal is awarded, score is updated
    elif goalie != shot_location():
        goals += 1
        attempts += 1
        print('\nScore = ' + str(goals) + '/' + str(attempts))
        print('\nGOOOOOAAALLLL!!')