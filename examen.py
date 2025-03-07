import random
from datetime import datetime

class Question(object):
    def __init__(self, text, answers, number_answers = 1, weight = 10000, age = 1):
        self.text = text
        self.answers = answers
        self.number_answers = number_answers
        self.weight = weight
        self.age = age

questions = [
    Question("What is the supreme law of the land?",[
        "the constitution",
    ]),
    Question("What does the Constitution do?", [
        "sets up the government",
        "defines the government",
        "protects basic rights of americans",
    ]),
    Question("The idea of self-government is in the first three words of the Constitution. What are these words?", [
        "we the people",
    ]),
    Question("What is an amendment?", [
        "a change to the constitution",
        "an addition to the constitution",
    ]),
    Question("What do we call the first ten amendments to the constitution?", [
        "the bill of rights",
    ]),
    Question("What is one right or freedom from the First Amendment?", [
        "speech",
        "religion",
        "assembly",
        "press",
        "petition the government",
    ]),
    Question("How many amendments does the Constitution have?", [
        "27",
        "twenty-seven",
    ]),
    Question("What did the Declaration of Independence do?", [
        "announced our independence from great britain",
        "declared our independence from great britain",
        "said that the united states is free from great britain",
    ]),
    Question("What are two rights in the Declaration of Independence", [
        "life",
        "liberty",
        "pursuit of happiness",
    ], number_answers = 2),
    Question("What is freedom of religion?", [
        "you can practice any religion or not practice a religion",
    ]),
    Question("What is the economic system in the United States?", [
        "capitalist economy",
        "market economy",
    ]),
    Question("What is the \"rule of law\"", [
        "everyone must follow the law",
        "leaders must obey the law",
        "government must obey the law",
        "no one is above the law",
    ]),
]

random.seed(datetime.now().timestamp())
correct_answers = 0
CORRECT_WEIGHT = 1
WRONG_WEIGHT = 10
while True:
    total_weight = sum([(question.weight * question.age) for question in questions])
    random_weight = random.randint(0, total_weight - 1)
    index = 0
    while index < len(questions):
        random_weight -= questions[index].weight * questions[index].age
        if random_weight < 0:
            break
        index += 1
    print(str(index + 1) + ".", questions[index].text)
    if questions[index].number_answers > 1:
        print("(Give each answer in a single line)")
    answers = set()
    while len(answers) < questions[index].number_answers:
        current_answer = input()
        if  current_answer in answers:
            print("You already provided that answer, please try with a different one.")
        else:
            answers.add(current_answer)
    previous_weight = questions[index].weight
    if previous_weight == CORRECT_WEIGHT:
        correct_answers -= 1
    correct = True
    for answer in answers:
        if answer not in questions[index].answers:
            correct = False
            break
    if correct:
        questions[index].weight = CORRECT_WEIGHT
        print("That is correct! The possible answers are:")
        correct_answers += 1
    else:
        questions[index].weight = WRONG_WEIGHT
        print("That is NOT right! The possible answers are:")
    for line in questions[index].answers:
        print(" - " + line)
    for question in questions:
        question.age += 1
    questions[index].age = 0
    print("Score:", correct_answers, "out of", len(questions))
