
# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop to handle rows
while row < size:
    # Use for loop to print asterisks in the current row
    for col in range(size):
        print("*", end="")
    # Move to the next line after printing one row
    print()
    # Increment row counter
    row += 1
