import time
import csv

class LearningTool:
    def __init__(self):
        self.command_prompts = {
            "Type 'add' to add new questions.": "add",
            "Type 'stats' to view question statistics.": "stats",
            "Type 'activate' to disable or enable questions.": "activate",
            "Type 'practice' to enter practice mode.": "practice",
            "Type 'test' to enter test mode.": "test",
        }

    # Initializes the start up and makes it possible to pick a mode.
    def start_up(self):
        print(
            "Hello! This is an interactive learning tool. To begin, please type in one of the following:"
        )
        time.sleep(1)
        for prompt, comm in self.command_prompts.items():
            print(prompt)

        user_choice = input().casefold().strip()

        while user_choice not in self.command_prompts.values():
            print(
                "Incorrect command. Please try again. If you wish to exit, type in 'quit'."
            )
            user_choice = input()
            if "quit" in user_choice:
                raise (SystemExit("Program stopped."))
        else:
            print("Command accepted.")
            return user_choice

    def main(self):
        if self.start_up() == "add":
            questions_mode()

class QuestionsMode:
    def __init__(self):
        self.question_count = 0

    # Enters question mode, provides the choice between quiz and free form mode and goes into the respective mode.
    def questions_mode(self):
        print(
            "You have chosen questions mode. You will now be able to enter and save your questions."
        )
        print(
            "Please note, that a minimum of 5 questions are required. Enter 'done' once you're finished."
        )

        with open("questions.csv") as file:
            reader = csv.DictReader(file)
            while True:
                type = (
                    input("Enter 'quiz' or 'free form' to select question type: ")
                    .casefold()
                    .strip()
                )
                if "quiz" in type:
                    quiz()
                elif "free form" in type:
                    free_form()
                if type == "done":
                    for row in reader:
                        self.question_count += 1
                    if self.question_count < 5:
                        print("At least 5 questions must be added.")
                        continue
                    if self.question_count >= 5:
                        print("All questions have been added.")
                        break


#Inputs the question and answer to csv in free form.
def free_form():
    with open("questions.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["question", "answer"])

        question = input("Enter your question: ")
        answer = input("Enter the answer: ")
        writer.writerow({"question": question, "answer": answer})

#Inputs the question and answer to csv in quiz form.
def quiz():
    with open("questions.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["question", "answer"])

        question = input("Enter your question: ")
        answer = ""
        answer_list = []
        while True:
            answer = input("Enter an answer:")
            if answer.casefold().strip() == "done":
                if 1 <= len(answer_list) <= 4:
                    break
                else:
                    print("You must provide at least 1 and up to 4 questions.")
                    continue

            answer_list.append(answer)

            if len(answer_list) == 4:
                print("You've reached the maximum limit of 4 answers.")
                break

        writer.writerow({"question": question, "answer": answer_list})


if __name__ == "__main__":
    main()
