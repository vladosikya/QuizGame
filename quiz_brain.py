class Brain:
    def __init__(self):
        self.score = 0

    def take_answer(self, question_date, num):
        while True:
            choose = input(f"{num}. {question_date.text}? True / False ").lower()
            if choose == 'true' or choose == 'false':
                if choose == question_date.answer.lower():
                    self.score += 1
                    print(f"This is the correct answer. Score {self.score}/{num}")
                    return True
                else:
                    print(f"Wrong answer. Score {self.score}/{num}")
                    return True
            if choose == "exit":
                print("Buy! Buy!")
                return False
            else:
                print("Unknown command.")

    def play_again(self):
        while True:
            choose = input('Do you want to play again? "y" or "n" ').lower()
            if choose == 'y':
                self.score = 0
                return True
            elif choose == 'n':
                print('See you later.')
                return False
            else:
                print('Unknown command.')
