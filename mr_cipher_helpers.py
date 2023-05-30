import datetime  # imports module to allow formatting of data/time

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


def print_welcome_message():  # prints welcome message to user
    print("""
  __  __          _____  _  ___  _____                         
 |  \/  |   /\   |  __ \| |/ ( )/ ____|                        
 | \  / |  /  \  | |__) | ' /|/| (___                          
 | |\/| | / /\ \ |  _  /|  <    \___ \                         
 | |  | |/ ____ \| | \ \| . \   ____) |                        
 |_|  |_/_/    \_|_|  \_|_|\_\ |_____/                         
   _____ _____ _____  _    _ ______ _____                      
  / ____|_   _|  __ \| |  | |  ____|  __ \                     
 | |      | | | |__) | |__| | |__  | |__) |                    
 | |      | | |  ___/|  __  |  __| |  _  /                     
 | |____ _| |_| |    | |  | | |____| | \ \                     
  \_____|_____|_|    |_|  |_|______|_|  \_\                    
   _____ ______ _   _ ______ _____        _______ ____  _____  
  / ____|  ____| \ | |  ____|  __ \    /\|__   __/ __ \|  __ \ 
 | |  __| |__  |  \| | |__  | |__) |  /  \  | | | |  | | |__) |
 | | |_ |  __| | . ` |  __| |  _  /  / /\ \ | | | |  | |  _  / 
 | |__| | |____| |\  | |____| | \ \ / ____ \| | | |__| | | \ \ 
  \_____|______|_| \_|______|_|  \_/_/    \_|_|  \____/|_|  \_\ 
  
  """)


def write_to_file(user_month, user_text, converted_text):  # defines function allowing user to write data to file
    current_date_time = datetime.datetime.now()  # assigns current time/date to a variable
    with open(f"cipher_logs/{current_date_time.strftime('%Y%m%d%H%M%S&f')}", "w") as output_file:  # uses 'with' statement to open file as alias
        output_file.write(f"User birth month: {user_month}\n"  # writes users birth month to opened file
                          f"Initial user input: {user_text}\n"  # writes users input to be converted to file
                          f"Converted ciphertext: {converted_text}\n"  # writes the converted output to file
                          f"Logged at {current_date_time.strftime('%H:%M:%S on %a %d/%B/%y')}")  # formats and logs time/date
    print("~ All cipher logs have been sent to log directory...")  # displays confirmation of log generation
