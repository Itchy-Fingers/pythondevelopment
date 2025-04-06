import os
# This script reads a file, allows the user to modify its content, and saves it to a new file.r
def read_and_modify_file():
    try:
        # Ask the user for a filename
        filename = input("Please enter the file name: ")
        # Check if the file exists
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' does not exist.")
            return
        with open(filename, 'r') as file:
            content = file.read()

        # User input for modifications (this can be as complex as needed)
        modified_content = input("Enter modifications or leave blank to save the existing content: ").strip()

        # Save the modified content to a new file
        if not modified_content:  # If no modifications were made, just use the original content
            new_filename = input(f"Please enter the new file name: ")
            with open(new_filename, 'w') as new_file:
                new_file.write(content)
        else:
            # If modifications were made, use them
            new_filename = input(f"Please enter the new file name with modified content: ")
            with open(new_filename, 'w') as new_file:
                new_file.write(modified_content)

    except FileNotFoundError:
        print(f"Error: File '{filename}' does not exist.")
    except IOError as io_error:
        print(f"Error: {io_error}")

# Start the program
read_and_modify_file()