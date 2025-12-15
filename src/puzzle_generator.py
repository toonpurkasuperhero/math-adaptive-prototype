import random

class PuzzleGenerator:
    def generate(self, difficulty):
        if difficulty == "Easy":
            a, b = random.randint(1, 10), random.randint(1, 10)
            op = random.choice(["+", "-"])
        elif difficulty == "Medium":
            a, b = random.randint(10, 50), random.randint(1, 12)
            op = random.choice(["+", "-", "*"])
        else:
            a, b = random.randint(20, 100), random.randint(1, 15)
            op = random.choice(["+", "-", "*", "/"])

            if op == "/":
                b = random.randint(1, 10)

        question = f"{a} {op} {b}"
        answer = eval(question)

        if op == "/":
            answer = round(answer, 2)

        return question, answer
