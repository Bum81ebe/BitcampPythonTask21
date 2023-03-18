import datetime


# List of valid month names
MONTH_NAMES = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    # Prompt the user for a date
    date_str = input("Please enter a date in the format MM/DD/YYYY or Month DD, YYYY: ")

    try:
        # Attempt to parse the date using strptime, which can handle both formats
        date = datetime.datetime.strptime(date_str, "%m/%d/%Y")
    except ValueError:
        try:
            date = datetime.datetime.strptime(date_str, "%B %d, %Y")
        except ValueError:
            # If the date is invalid, reprompt the user
            print("Invalid date format. Please try again.")
            continue

    # Format the date 
    print(date.strftime("%Y-%m-%d"))
