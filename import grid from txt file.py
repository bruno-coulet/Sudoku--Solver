# Import the module for file handling
import os

# Path to your text file
file_path = 'sudoku3.txt'

# Check if the file exists
if os.path.exists(file_path):
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the content of the file
        content = file.read()
        # Display the content in the terminal
        print(content)
else:
    print("The file does not exist.")
