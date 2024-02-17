class SingleChoiceQuestion:
    def __init__(self, text: str, answers: list[str]):
        self.text = text
        self.answers = answers

    def ask(self) -> int | None:
        mp = {}
        print(self.text)
        for idx, answer in enumerate(self.answers):
            letter = chr(idx + ord('a'))
            print(f"{letter}) {answer}")
            mp[letter] = idx

        while True:
            answer = input("Answer: ")
            if answer not in mp.keys():
                print("Invalid answer, try again: ")
            else:
                return mp[answer]


class Questionnaire:
    def __init__(self, title: str):
        self.title = title
        self.questions = []

    def add_question(self, question: SingleChoiceQuestion):
        self.questions.append(question)

    def run(self):
        answers = {}
        print(f"{self.title}")
        for idx, question in enumerate(self.questions):
            answer = question.ask()
            answers[idx] = chr(answer + ord("a"))

        print("Thank u!")
        return answers


if __name__ == "__main__":
    questionnaire = Questionnaire('Laptop satisfaction questionnaire')
    q1 = SingleChoiceQuestion('Size of screen', ['less than 15 inches', 'from 15 to 17 inches', 'more than 17 inches'])
    q2 = SingleChoiceQuestion('Type of screen', ['matte', 'glossy'])
    q3 = SingleChoiceQuestion('Would you recommend it?',
                                   ['definitely yes', 'rather yes', 'not sure', 'rather not', 'definitely not'])
    questionnaire.add_question(q1)
    questionnaire.add_question(q2)
    questionnaire.add_question(q3)

    answers = questionnaire.run()

    print(answers)
