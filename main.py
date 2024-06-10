class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

class Quiz:
    def __init__(self):
        self.questions = []
        self.guesses = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def take_quiz(self):
        for question_num, question in enumerate(self.questions):
            print("----------------------")
            print(question.text)
            for option in question.options:
                print(option)

            guess = input("Enter (A, B, C, D): ").upper()
            self.guesses.append(guess)
            if guess == question.answer:
                self.score += 1
                print("CORRECT!")
            else:
                print("INCORRECT!")
                print(f"{question.answer} is the correct answer")

    def show_results(self):
        print("----------------------")
        print("       RESULTS        ")
        print("----------------------")

        print("Answers: ", end="")
        for question in self.questions:
            print(question.answer, end=" ")
        print()

        print("Guesses: ", end="")
        for guess in self.guesses:
            print(guess, end=" ")
        print()

        score_percentage = int(self.score / len(self.questions) * 100)
        print(f"Your score is: {score_percentage}%")

def main():
    questions = [
        Question("How many elements are in the periodic table?: ",
                 ("A. 116", "B. 117", "C. 118", "D. 119"), "C"),
        Question("Which animal lays the largest eggs?: ",
                 ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"), "D"),
        Question("What is the most abundant gas in Earth's atmosphere?: ",
                 ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"), "A"),
        Question("How many bones are in the human body?: ",
                 ("A. 206", "B. 207", "C. 208", "D. 209"), "A"),
        Question("Which planet in the solar system is the hottest?: ",
                 ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"), "B")
    ]

    quiz = Quiz()

    for question in questions:
        quiz.add_question(question)

    quiz.take_quiz()
    quiz.show_results()

if __name__ == "__main__":
    main()
