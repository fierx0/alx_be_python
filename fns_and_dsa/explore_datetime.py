# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()
    # Format the date and time as YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date):
    try:
        # Prompt user for number of days to add
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        # Calculate future date
        future_date = current_date + timedelta(days=number_of_days)
        # Format future date as YYYY-MM-DD
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Please enter a valid integer number of days.")

# Main execution
if __name__ == "__main__":
    current_date = display_current_datetime()
    calculate_future_date(current_date)
