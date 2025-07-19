
# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Generate reminder based on priority
match priority:
    case "high":
        base_message = f"'{task}' is a high priority task"
    case "medium":
        base_message = f"'{task}' is a medium priority task"
    case "low":
        base_message = f"'{task}' is a low priority task"
    case _:
        base_message = f"'{task}' has an unrecognized priority level"


# Add time-bound info
if time_bound == "yes":
    final_message = f"Reminder: {base_message} that requires immediate attention today!"
else:
    final_message = f"Reminder: {base_message}. Consider completing it when you have free time."

# Print the final reminder
print(final_message)