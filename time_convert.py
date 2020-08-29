# Lists of Available Functions

tc_functions = ["Seconds"]

### Console Interface Code

def initiate():
    print("Hi! Thank you for using time_convert.py!")
    print("This script is made by github.com/enzorooo")
    select_unit_to_convert()

# User selects unit to convert 
def select_unit_to_convert():
    print("\nWhat unit of time would you like to convert? Please type the number of your choice.")
    def list_tc_functions():
        for unit in tc_functions:
            return "[" + str(tc_functions.index(unit) + 1) + "] " + unit + "\n"
    follow_function = input(list_tc_functions())

    # Input validation

    if follow_function != 1:
        return "Please input a valid option from the selection."
        select_unit_to_convert()

    if follow_function == 1:
        seconds_to_convert()

# Convert Seconds Functions
def seconds_to_convert():
    seconds_to_input = "How many seconds would you like to convert?\n"
    seconds = input(seconds_to_input)

    # validate input
    while seconds != int:
        print("Sorry, we only accept numbers as input.")
        seconds_to_convert()

    # print results
    print("\n")
    print(seconds + " seconds is equivalent to the following:")
    print(seconds_to_minutes(seconds) + " minutes")
    print(seconds_to_hours(seconds) + "hours")
    print(seconds_to_dayss(seconds) + "days")
    print(seconds_to_years(seconds) + "years")


### v 1.0 Functions - Seconds Converter
# second = 1
# minute = 60 * second
# hour = minute * 60
# day = hour * 24


def seconds_to_minutes(seconds):
    minutes = seconds * 60
    return minutes

def seconds_to_hours(seconds):
    hours = seconds_to_minutes(seconds) * 60
    return hours

def seconds_to_days(seconds):
    days = seconds_to_hours(seconds) * 24
    return days

def seconds_to_years(seconds):
    years = seconds_to_days(seconds)
    return years


### Execution Functions
initiate()
