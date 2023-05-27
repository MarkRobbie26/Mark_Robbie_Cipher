import datetime

# defines a dictionary with the shift values for each month
month_dict = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}


def print_welcome_message():
    # prints welcome message to user
    print("""
    WELCOME TO MY
             _         __               
      _____ (_)____   / /_   ___   _____
     / ___// // __ \ / __ \ / _ \ / ___/
    / /__ / // /_/ // / / //  __// /    
    \___//_// .___//_/ /_/ \___//_/     
           /_/                                            
                              GENERATOR!                                                                                                                                                                                                                                                    
    """)


def write_to_file(user_month, user_text, converted_text):  # defines function that will write to text file
    current_date_time = datetime.datetime.now()
    with open(f"{current_date_time.strftime('%Y%m%d%H%M%S&f')}", "w") as output_file:  # uses with statement to open file as alias. also closes file
        output_file.write(f"User birth month: {user_month}\n"  # writes users birth month to opened file
                          f"Initial user input: {user_text}\n"  # writes users input to be converted to file
                          f"Converted ciphertext: {converted_text}\n"  # writes the converted output to file
                          f"Logged at {current_date_time.strftime('%H:%M:%S on %a %d/%B/%y')}")  # logs time/date
    print("~ Log of conversion sent to 'converted_text.txt' file")  # displays confirmation of log generation

