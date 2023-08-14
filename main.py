import time
import csv

#Base tool itself.
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

    #Initializes the selected mode.
    def main(self):
        if self.start_up() == "add":
            question_mode = QuestionsMode()
            question_mode.questions_mode()
        if self.start_up() == "stats":
            stats_mode = StatisticsMode()


class QuestionsMode:
    def __init__(self):
        self.question_count = 0
        self.id_counter = 1

    def get_next_question_id(self):
        question_id = self.id_counter
        self.id_counter += 1
        return question_id

    #Enters question mode, provides the choice between quiz and free form mode and goes into the respective mode.
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
                question_type = input("Enter 'quiz' or 'free form' to select question type: ").casefold().strip()

                if question_type == "quiz":
                    quiz_question = QuizQuestion()
                    quiz_question.enter_question(self.get_next_question_id())
                elif question_type == "free form":
                    free_form_question = FreeFormQuestion()
                    free_form_question.enter_question(self.get_next_question_id())

                if question_type == "done":
                    for row in reader:
                        self.question_count += 1
                    if self.question_count < 5:
                        print("At least 5 questions must be added.")
                        continue
                    if self.question_count >= 5:
                        print("All questions have been added.")
                        break

#Initializes the question and opens the csv file.
class BaseQuestion:
    def __init__(self):
        self.file_path = "questions.csv"

    def enter_question(self, question_id):
        question = input("Enter your question: ")
        answer = self.get_answer()

        with open("questions.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "question", "answer"])
            writer.writerow({"id": question_id, "question": question, "answer": answer})

#Returns the answer made in free form format.
class FreeFormQuestion(BaseQuestion):
    def get_answer(self):
        return input("Enter the answer: ")

#Returns the answer made in quiz format.
class QuizQuestion(BaseQuestion):
    def get_answer(self):
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

        return answer_list

class StatisticsMode:
    ...

if __name__ == "__main__":
    learning_tool = LearningTool()
    learning_tool.main()

