import random

class PuzzleGenerator:
    def generate(self, difficulty_level):

        #Difficulty:Easy
        #this has simple addition/subtraction
        if difficulty_level == "Easy":
            num1 = random.randint(1,9)
            num2 = random.randint(1,9)
            operation = random.choice(['+','-'])
            
            if operation == '-' and num1 < num2: #As this is easy difficulty so i wanted to avoid having -ve integers
                num1,num2 = num2,num1

        #Difficulty:Medium
        #this has double digits (10-50) and allows negative answers
        elif difficulty_level == "Medium":
            num1 = random.randint(10, 50)
            num2 = random.randint(1, 49)
            operation = random.choice(['+', '-'])

        #Difficulty:Hard
        # this has multiplication and larger addition
        else:
            num1 = random.randint(5, 12)
            num2 = random.randint(5, 12)
            operation = '*'
        if operation == '+':
            answer = num1 + num2
        elif operation == '-':
            answer = num1 - num2
        else:
            answer = num1 * num2

        return {
            "question": f"{num1} {operation} {num2}",
            "answer": answer
        }