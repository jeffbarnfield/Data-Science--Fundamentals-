# Asks user to input 2 numbers then perform + - * / operation on the two numbers
# Saves the equation to a .txt file
# Reads the .txt file and output the contents of the file

import os

def main():

    while True:
        option1 = "Option 1: Enter two numbers and an operator."
        option2 = "Option 2: Read equations from a file"
        print(option1)
        print(option2)
        selected_option = input("Enter 1 or 2 to Select the Option, e to exit: ").strip()
        if selected_option == "1":
            user_filename = input("Enter a filename: ").strip()
            # Allows multiple equations to be written to the same file without prompting for a filename each time
            while True:
                if len(user_filename) > 0:
                    return_value = calculator(user_filename)
                    if return_value == False:
                        break
                else:
                    print("Filename should have at least 1 character")
                    break
                                                            
        elif selected_option == "2":
                    get_file()

        elif selected_option == "e":
            break

        else:
            print("Enter 1, 2 or e as an option")
    
# calculator function takes user_filename as an input, requests 2 numbers and the operation to be performed.
# Appends the equation to .txt file
# Returns False when e is entered as the input to number_1
    
def calculator(user_filename = "equations"):

    while True:
        try:
            # Used https://www.w3schools.com/python/python_file_write.asp for writing to a file
            file = open(f"{user_filename}.txt", "a")   
                            
            number_1 = input("Enter Number 1, e to exit: ").strip()
            if number_1 == "e":
                print(number_1)
                file.close()
                return False
            number_2 = input("Enter Number 2: ").strip()
            operation = input("Enter the operation to be performed: ").strip()

            if operation == "+":
                answer = float(number_1) + float(number_2)
                print(f"Answer: {answer:.2f}")
                file.write(f"{number_1} + {number_2} = {answer:.2f}\n")
                file.close()
                return True
            elif operation == "-":
                answer = float(number_1) - float(number_2)
                print(f"Answer: {answer:.2f}")
                file.write(f"{number_1} - {number_2} = {answer:.2f}\n")
                file.close()
                return True
            elif operation == "*":
                answer = float(number_1)* float(number_2)
                print(f"Answer: {answer:.2f}")
                file.write(f"{number_1} * {number_2} = {answer:.2f}\n")
                file.close()
                return True
            elif operation == "/":
                answer = float(number_1) / float(number_2)
                print(f"Answer: {answer:.2f}")
                file.write(f"{number_1} / {number_2} = {answer:.2f}\n")
                file.close()
                return True
            else:
                print("Operator must be +, -, * or /")
                return True
        except ValueError:
            print("Values must be numbers.") 
            return True

# get_file function prompts the user to enter a filename that exists, keeps prompting until a correct filename is entered
# prints the equations stored in the file

def get_file():

    # Used https://stackoverflow.com/questions/5137497/find-the-current-directory-and-files-directory to find the current directory
    file_path = os.getcwd()

    # Used https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python to list the .txt files in the current directory
    print(".txt files found in the current directory: ")
    for file in os.listdir(file_path):
        if file.endswith(".txt"):
            print(file)

    while True:
        try:
            user_filename = input("Enter a filename from the list above: ").strip()
            file = open(f"{user_filename}.txt", "r")
            print(file.read())
            file.close()
            break
        except FileNotFoundError:
            print("The file you have requested does not exist") 

main()