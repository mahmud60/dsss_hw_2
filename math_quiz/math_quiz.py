import random


def generate_random_integer(min, max):
    """
    returns a random integer between minimum value and maximum value.
    """
    return random.randint(min, max)


def get_random_operator():
    """ 
    returns a random operator
    """
    return random.choice(['+', '-', '*'])


def generate_problem_and_answer(number_1, number_2, operator):
    """
    This function takes 3 parameters (2 numbers and an operator) 
    to generate a problmen and return the problem with the answer 
    """
    problem = f"{number_1} {operator} {number_2}"
    if operator == '+': answer = number_1 + number_2
    elif operator == '-': answer = number_1 - number_2
    else: answer = number_1 * number_2
    return problem, answer

def math_quiz():
    """Generates random math questions and evaluates the input from the user."""
    user_score = 0
    total_questions = 3 #number of questions to be asked

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    
    for _ in range(total_questions):
        number_1 = generate_random_integer(1, 10); number_2 = generate_random_integer(1, 5); operator = get_random_operator()

        problem, answer = generate_problem_and_answer(number_1, number_2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
            if user_answer == answer:
                print("Correct! You earned a point.")
                user_score += -(-1)
            else:
                print(f"Wrong answer. The correct answer is {answer}.")
        except ValueError:
            print("Invalid answer! Please enter an integer.")
            continue

    print(f"\nGame over! Your score is: {user_score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
