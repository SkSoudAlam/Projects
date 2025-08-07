import random 
from colorama import Style, Fore, init
import unittest
from unittest.mock import patch
from io import StringIO

init(autoreset=True)
def get_user_guess():
    while True:
        user_input = input('\nEnter a number from 1 to 20 (q to quit): ')
        if user_input.lower() == 'q':
            print("Thanks for playing")
            return None
        try:
            user_guess = int(user_input)
            if 1 <= user_guess <= 20:
                return user_guess
            else:
                print(Fore.BLUE + "Please enter a number between 1 and 20.")
        except ValueError:
            print(Fore.BLACK + "Invalid input! Please enter a valid number.")


def play_game():
    guesses = random.randint(10, 12)
    correct_guess = random.randint(1, 20)

    while guesses > 0:
        user_guess = get_user_guess()
        if user_guess is None:
            break
        elif user_guess == correct_guess:
            print(Fore.GREEN + f'Congratulations! You guessed it right in {10 - guesses + 1} guesses.')
            break
        else:
            guesses -= 1
            print(Fore.LIGHTBLUE_EX + f"Wrong guess! {guesses} guesses left.")
    else:
        print(Fore.RED + 'Oops! You ran out of guesses. The correct answer was', correct_guess)
        
class TestGuessingGame(unittest.TestCase):
    @patch('builtins.input', side_effect=['25', 'q'])
    def test_invalid_input_then_quit(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            user_guess = get_user_guess()
            self.assertIsNone(user_guess)
            self.assertEqual(mock_stdout.getvalue().strip(), 'Invalid input! Please enter a valid number.\nThanks for playing')

    @patch('builtins.input', side_effect=['15'])
    def test_valid_input(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            user_guess = get_user_guess()
            self.assertEqual(user_guess, 15)
            self.assertEqual(mock_stdout.getvalue().strip(), '')


if __name__ == "__main__":
    play_game()
    print(Style.RESET_ALL)
