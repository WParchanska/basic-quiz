questions = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What is the color of the sky?": "Blue"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        score += 1
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {answer}.")

print(f"\nYour final score is {score}/{len(questions)}")
