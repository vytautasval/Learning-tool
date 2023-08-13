import time

def main():
    start_up()

#Initializes the start up and makes it possible to pick a mode.
def start_up():
    print(
        "Hello! This is an interactive learning tool. To begin, please type in one of the following:"
    )
    time.sleep(1)
    command_prompts = {
        "Type 'add' to add new questions.": "add",
        "Type 'stats' to view question statistics.": "stats",
        "Type 'activate' to disable or enable questions.": "activate",
        "Type 'practice' to enter practice mode.": "practice",
        "Type 'test' to enter test mode.": "test"
    }

    for prompt, comm in command_prompts.items():
        print(prompt)

    user_choice = input()
    user_choice.casefold().strip()

    while user_choice not in command_prompts.values():
        print("Incorrect command. Please try again.")
        user_choice = input()
    else:
        print("Command accepted.")
        return user_choice


if __name__ == "__main__":
    main()
