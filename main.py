print("Welcome to Python Quiz Game!")

questions = [
    {
        "question":"What is the correct file extension for Python files?",
        "options":[".pyth", ".pt", ".pyt", ".py"],
        "answer":".py"
    },
    {
        "question":"Which of the following is a valid way to create a variable in Python?",
        "options":["var x = 5", "x = 5", "int x = 5", "variable x = 5"],
        "answer":"x = 5"
    },
    {
        "question":"What is the output of the following code: print(2 + 3 * 4)?",
        "options":["14", "20", "24", "None of the above"],
        "answer":"20"
    },
    {
        "question":"What is the output of the following code: print('Hello, World!')?",
        "options":["Hello, World!", "Hello, World", "Hello, World!", "None of the above"],
        "answer":"Hello, World!"
    },
    {        
        "question":"Which of the following is used to define a function in Python?",
        "options":["function", "def", "func", "define"],
        "answer":"def"
    }
]

score = 0

for i in range(len(questions)):
    print(f"Question {i+1}: {questions[i]['question']}")
    for j in range(len(questions[i]['options'])):
        print(f"{j+1}. {questions[i]['options'][j]}")
    answer = input("Enter the number of your answer: ")
    while answer != '1' and answer != '2' and answer != '3' and answer != '4':
        answer = input("Enter the number of your answer: ")
    if questions[i]['options'][int(answer)-1] == questions[i]['answer']:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {questions[i]['answer']}\n")

print(f"Your final score is {score} out of {len(questions)}.")
print(f"Percentage: {(score / len(questions)) * 100:.2f}%")
