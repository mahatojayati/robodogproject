# List of possible commands
possible_commands = [
    "sit", 
    "stand", 
    "walk", 
    "run", 
    "jump", 
    "bark", 
    "fetch", 
    "roll over", 
    "come here", 
    "stop"
]

def check_command(command):
    """
    This function checks if the command is in the list of possible commands.
    Returns 1 if the command is recognized, and 0 if it is not.
    """
    command = command.strip().lower()
    
    if command in possible_commands:
        return 1
    else:
        return 0

def Tomy():
    """
    This function continuously asks the user for commands,
    checks if the command is possible, and asks if the user wants to continue.
    """
    while True:
        command = input("Please give a command: ")
        result = check_command(command)
        print(f"Command recognized: {result}")
        
        # Ask if the user wants to input another command
        more_commands = input("Do you want to enter another command? (yes/no): ").strip().lower()
        
        if more_commands != 'yes':
            print("Goodbye!")
            break

# Call the Tomy function
Tomy()
