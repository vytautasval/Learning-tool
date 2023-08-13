import time
import sys
import csv


def main():
    if start_up() == "add":
        questions_mode()


# Initializes the start up and makes it possible to pick a mode.
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
        "Type 'test' to enter test mode.": "test",
    }

    for prompt, comm in command_prompts.items():
        print(prompt)

    user_choice = input().casefold().strip()

    while user_choice not in command_prompts.values():
        print(
            "Incorrect command. Please try again. If you wish to exit, type in 'quit'."
        )
        user_choice = input()
        if "quit" in user_choice:
            raise (SystemExit("Program stopped."))
    else:
        print("Command accepted.")
        return user_choice


# Enters question mode, provides the choice between quiz and free form mode and goes into the respective mode.
def questions_mode():
    print(
        "You have chosen questions mode. You will now be able to enter and save your questions."
    )
    print(
        "Please note, that a minimum of 5 questions are required. Enter 'done' once you're finished."
    )

    type = ""
    while type != "done":
        type = (
            input("Enter 'quiz' or 'free form' to select question type: ")
            .casefold()
            .strip()
        )
        if "quiz" in type:
            ...
        elif "free form" in type:
            free_form()

#Inputs the question and answer to csv in free form.
def free_form():
    with open("questions.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["question", "answer"])

        if file.tell() == 0:
            writer.writeheader()

        question = input("Enter your question: ")
        answer = input("Enter the answer: ")
        writer.writerow({"question": question, "answer": answer})

def quiz():



if __name__ == "__main__":
    main()
