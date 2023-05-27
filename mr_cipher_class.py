from tqdm import tqdm
from time import sleep
import mr_cipher_helpers


class CipherConverter:
    def __init__(self):
        self.user_birth_month = None
        self.user_text_input = None
        self.converted_text = ""

    def get_birth_month(self):
        while True:  # enters while block to get users birth month
            user_birth_month = input("~ Please begin by entering your birth month (Jan/Feb/...): ").title()  # gets birth month
            if user_birth_month not in mr_cipher_helpers.month_dict:  # checks if given month is valid
                print("~ That was not a valid selection, please try again.")  # displays message stating month is invalid
            else:
                self.user_birth_month = user_birth_month
                print(f"~ Month entered: {user_birth_month}")  # if month is valid, month will be printed back to user
                break  # breaks from while loop because valid month has been entered

    def get_user_text_input(self):
        while True:
            user_text_input = input("~ Please enter the phrase you would like to convert to ciphertext: ")
            if len(user_text_input) > 0:
                self.user_text_input = user_text_input
                print(f"~ Text to be converted: '{self.user_text_input}'")
                break
            else:
                print("ERROR. You did not enter anything. Try again.")

    def convert_text(self):  # defines function used to generate ciphertext. takes user input and month
        for character in self.user_text_input:  # iterates through each character in given text
            if character.isalpha():  # checks if the character is alphabetic, will be converted if so
                a_unicode = ord("A") if character.isupper() else ord("a")
                converted_character_unicode = ord(character) + mr_cipher_helpers.month_dict[self.user_birth_month]
                converted_character_unicode = (converted_character_unicode - a_unicode) % 26
                self.converted_text += chr(a_unicode + converted_character_unicode)
            else:
                self.converted_text += character
        print("......CONVERTING TO CIPHERTEXT......")
        for _ in tqdm([i for i in range(10)]):
            sleep(0.1)
        print(f"~ Converted text: {self.converted_text}")

    def run_cipher(self):
        self.get_birth_month()
        self.get_user_text_input()
        self.convert_text()
