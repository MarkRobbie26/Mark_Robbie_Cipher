from tqdm import tqdm  # imports module to create progress bar
from time import sleep  # imports module to pause program
import mr_cipher_helpers  # imports module containing custom functions/data


class CipherConverter:  # declares CipherConverter class using CapWords convention
    def __init__(self):  # initializes current instance
        self.user_birth_month = None  # assigns user birth month to None
        self.user_text_input = None  # assigns user input to None
        self.converted_text = ""  # assigns converted text to empty string

    def get_birth_month(self):  # defines method to get users birth month
        while True:
            user_birth_month = input("~ Please begin by entering your birth month (Jan/Feb/...): ").title()  # assigns input as birth month
            if user_birth_month not in mr_cipher_helpers.month_dict:  # checks if given month is not valid
                print("~ That was not a valid selection, please try again.")  # displays message stating month is invalid
            else:
                self.user_birth_month = user_birth_month  # assigns given month as users birth month if valid
                print(f"~ Month entered: {user_birth_month}")  # prints users valid birth month
                break  # breaks from while loop because valid month has been entered

    def get_user_text_input(self):  # defines method to get input to be converted
        while True:
            user_text_input = input(r"~ Please enter the phrase you would like to convert to ciphertext: ")  # assigns raw input as text to be converted
            if len(user_text_input) > 0:  # ensures the user entered something
                self.user_text_input = user_text_input  # assigns user input as users text input
                print(f"~ Text to be converted: '{self.user_text_input}'")  # prints users text input
                break  # breaks from while loop because valid text has been entered
            else:
                print("ERROR. You did not enter anything. Try again.")  # displays error message if input was blank

    def convert_text(self):  # defines method to convert user input to ciphertext
        for character in self.user_text_input:  # iterates through each character in given input
            if character.isalpha():  # checks if the character is alphabetic, will be converted if so
                a_unicode = ord("A") if character.isupper() else ord("a")  # sets base 'a' depending on lower/upper
                converted_character_unicode = ord(character) + mr_cipher_helpers.month_dict[self.user_birth_month]  # applies offset for each character
                converted_character_unicode = (converted_character_unicode - a_unicode) % 26  # mod 26 to ensure eny char after 'z' begins at 'a'
                self.converted_text += chr(a_unicode + converted_character_unicode)  # concatenates each converted character
            else:
                self.converted_text += character  # concatenates character if not alphabetic
        print("......CONVERTING TO CIPHERTEXT......")  # displays message stating conversion is taking place
        for _ in tqdm([i for i in range(10)]):  # splits progress bar into 10 sections
            sleep(0.1)  # pauses execution for 0.1 per section for a total of 1 second
        print(f"~ Converted text: {self.converted_text}")  # displays converted text to user

    def run_cipher(self):  # defines method to run whole instance
        self.get_birth_month()  # calls get_birth_month on current instance
        self.get_user_text_input()  # calls get_user_text_input on current instance
        self.convert_text()  # # calls convert_text on current instance
