import random
import emoji

def guessing_new_game(start:int,stop:int):
    '''
    INPUT: Guessing a number between start and stop value. start,stop,number are provided.
    OUTPUT:Boolean value and string of contents is returned until your guess is corrected.
    '''
    #initialize variables
    try_again = 1
    count = 0
    
    print('''
             *************************************************************
             ************* BEGIN CONDITIONS ************* 
             These ar guessing game conditions
             1.start and stop value must be integer.
             2.start and stop value should be not equal.
             3.start value should be less than stop value.
             4.The Difference between start and stop must be greater than 5.
             ************* END CONDITIONS *************
             ***************************************************************
             ''')
    
    if(start != stop and start < stop and (stop - start) >= 5 and type(start) == int and type(stop) == int):
        print(f'conditions met {emoji.emojize(":beaming_face_with_smiling_eyes:")*5}')
        try:
            while True:
                if(try_again == 1):
                    guess_number = int(input(f"Guess a number between {start} and {stop}:"))
                    try_again = 0
                    
                random_number = random.randint(start,stop)
                count += 1
                if(random_number == guess_number):
                    print(f"Congratulations your random number {random_number} and guess number {guess_number} are matched.\n You have attempted {count} times to guess a number.")
                    try:
                        try_again = int(input('If you want to try again enter 1 or 0 1:PlayAgain 0:Exit'))
                        if(try_again == 1):
                            continue
                        elif(try_again == 0):
                            break
                        else:
                            return 
                    except ValueError:
                        return f'Please enter a number and donot enter alphabets or any special characters {emoji.emojize(":zipper-mouth_face:")}.'
                else:
                    try_again = 1
                    continue
        except ValueError:
            return "Please enter a number and don't enter alphabets or any special characters."
    else:
        return f"conditions not satisified {emoji.emojize(':shushing_face:')} ."
    
    return f'Thanks for playing the game {emoji.emojize(":beaming_face_with_smiling_eyes:")}'
