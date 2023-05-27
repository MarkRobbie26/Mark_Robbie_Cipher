import sys  # imports sys module to allow us to exit program safely
from mr_cipher_helpers import print_welcome_message, write_to_file
from mr_cipher_class import CipherConverter


if __name__ == "__main__":  # allows execution of code if run as main program and not imported
    while True:  # enters while loop which allows us to repeat the program or break from loop to exit
        try:
            print_welcome_message()
            instance = CipherConverter()
            instance.run_cipher()
            write_to_file(instance.user_birth_month, instance.user_text_input, instance.converted_text)
            repeat = input("~ Would you like to run the cipher again? ('Y'/'N' to quit): ").upper()  # asks user if they would like to repeat prog
            if repeat != "Y":  # checks if user entered Y to repeat program
                print("~ User has closed the program.")  # displays exit message
                break  # breaks from while loop, causing the program to end
        except KeyboardInterrupt:  # handles keyboard interruptions from user to exit program safely
            print("\n~ Program has been interrupted by the user")  # displays message to tell user they have interrupted the program
            sys.exit(0)  # uses the exit function and passes 0 to allow exit of code without errors
        except Exception as e:  # catches any other errors
            print("~ An error occurred:", str(e))  # displays message with exception object converted to a string
