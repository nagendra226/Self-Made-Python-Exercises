import random
import emoji


class GuessingGame:
    print('''
                 *************************************************************
                 ************* BEGIN CONDITIONS ************* 
                 These are the guessing game conditions
                 1.start and stop value must be integer.
                 2.start and stop value should be not equal.
                 3.start value should be less than stop value.
                 4.The Difference between start and stop must be greater than 5.
                 ************* END CONDITIONS *************
                 ***************************************************************
                 ''')

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        if (self.start != self.stop and self.start < self.stop and (self.stop - self.start) >= 5 and type(
                self.start) == int and type(self.stop) == int):
            print(f'conditions met {emoji.emojize(":beaming_face_with_smiling_eyes:") * 5}')
        else:
            raise Exception("Conditions not satisfied.")

    def play_game(self):
        guess_number = None
        count = 0
        play_again = 1
        try:
            while True:
                if play_again == 1:
                    guess_number = int(input(f"Guess a number between {self.start} and {self.stop}:"))
                    play_again = 0


                random_number = random.randint(self.start, self.stop)
                count += 1
                if random_number == guess_number:
                    print(
                        f"Congratulations your random number {random_number} and guess number {guess_number} are matched.")
                    print(f'You have attempted {count} times to guess a number')

                    try:
                        play_again = int(input('If you want to try again enter 1 or 0 1:PlayAgain 0:Exit'))
                        if play_again == 1:
                            count = 0
                            continue
                        elif play_again == 0:
                            break
                        else:
                            return f'sorry you have entered wrong input {play_again}.'
                    except ValueError:
                        print(
                            f"Please enter a number and do not enter alphabets or any special characters {emoji.emojize(':zipper-mouth_face:')}.")
                        continue
                else:
                    play_again = 1
                    continue
        except ValueError:
            return "Please enter a number and don't enter alphabets or any special characters."

        return count


# Whose is the winner
def winner(a: int, b: int):
    if a < b:
        return 'Player 1 is the winner.'
    else:
        return 'Player 2 is the winner'


player1 = GuessingGame(1, 10)
score_player1 = player1.play_game()

player2 = GuessingGame(1, 10)
score_player2 = player2.play_game()

print(winner(score_player1, score_player2))
