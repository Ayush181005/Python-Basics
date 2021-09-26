from Question import Question

Question_prompts = [
    "What is the colour of an Apple?\nA. Red/Green\nB. Blue\nC. None of the above\n\n",
    "What is the colour of a Strawberry?\nA. Green\nB. Blue\nC. Red\n\n",
    "What is the colour of Orange?\nA. Red/Green\nB. Orange\nC. None of the above\n\n"
]

questions = [
    Question(Question_prompts[0], "A"),
    Question(Question_prompts[1], "C"),
    Question(Question_prompts[2], "B")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Score: "+str(score)+"/"+str(len(questions)))

run_test(questions)
