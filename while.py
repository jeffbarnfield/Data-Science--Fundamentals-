# Using a while loop to calculate the average of all numbers entered by the user
# Enter -1 to exit while loop
# Average rounded to 2 decimal places

total = 0
num_entries = 0

while True:
    user_number = float(input("Please enter a number (enter -1 to exit): ").strip())
    # Only increases total and number of entries if value is not -1
    if user_number != -1:
        total += user_number
        num_entries += 1
    # Outputs average when -1 entered, total is not zero and prevents division by 0
    elif user_number == -1 and total != 0:
        average = float(total/ num_entries)
        print(f"The average of the numbers to 2 decimal places is: {average:.2f}")
        break
    # Output if division is by 0
    else:
        print("Please enter a number other than -1 to calculate the average. -1 is only used to exit the program.")
        break