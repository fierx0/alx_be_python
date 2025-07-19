
# Prompt for task details
task = input("Enter your task for today: ")
priority = input("What is the priority level? (high/medium/low): ").strip().lower()
time_bound = input("Is the task time-bound? (yes/no): ").strip().lower()

# Generate the base reminder message using match-case for priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task."
    case _:
        reminder = f"Reminder: '{task}' has an UNKNOWN priority level."

# Add time sensitivity warning if applicable
if time_bound == "yes":
    reminder += " It requires immediate attention today!"

# Print the final reminder
print(reminder)
