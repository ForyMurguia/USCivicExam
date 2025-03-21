import random
from datetime import datetime
from winreg import QueryValueEx


class Question(object):
    def __init__(self, text, answers, number_answers = 1, weight = 10000, age = 1):
        self.text = text
        self.answers = answers
        self.number_answers = number_answers
        self.weight = weight
        self.age = age

questions = [
    # AMERICAN GOVERNMENT
    # A: Principles of American Democracy
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

    # B: System of Government
    Question("Name one branch or part of the government", [
        "congress",
        "legislative",
        "president",
        "executive",
        "the courts",
        "judicial",
    ]),
    Question("What stops one branch of the government from becoming too powerful?", [
        "checks and balances",
        "separation of powers",
    ]),
    Question("Who is in charge of the executive branch?", [
        "the president",
    ]),
    Question("Who makes federal laws?", [
        "congress",
        "senate and house of representatives",
        "us legislature",
        "national legislature",
    ]),
    Question("What are the two parts of the U.S. Congress?", [
        "the senate",
        "house of representatives",
    ], number_answers=2),
    Question("How many U.S. Senators are there?", [
        "100",
        "one hundred",
    ]),
    Question("We elect a U.S. Senator for how many years?", [
        "six",
        "6",
    ]),
    Question("Who is one of your state's U.S. Senators now?", [
        "alex padilla",
        "adam schiff",
    ]),
    Question("The House of Representatives has how many voting members?", [
        "435",
        "four hundred thirty-five",
    ]),
    Question("We elect a U.S. Representative for how many years?", [
       "two",
        "2",
    ]),
    Question("Name your U.S. Representative", [
        "sam liccardo",
    ]),
    Question("Who does a U.S. Senator represent?", [
        "all people of the state",
    ]),
    Question("Why do some states have more Representatives that other states", [
        "because of the state's population",
        "because they have more people",
        "because some states have more people",
    ]),
    Question("We elect a President for how many years?", [
        "four",
        "4",
    ]),
    Question("In what month do we vote for President?", [
        "november",
    ]),
    Question("What is the name of the President of the United States now?", [
        "donald trump",
        "donald j. trump",
        "trump",
    ]),
    Question("What is the name of the Vice President of the Unites States now?", [
        "jd vance",
        "vance",
    ]),
    Question("If the President can no longer serve, who becomes President?", [
        "the vice president",
    ]),
    Question("If both the President and the Vice President can no longer serve, who becomes President?", [
        "the speaker of the house",
    ]),
    Question("Who is the Commander in Chief of the military?", [
        "the president",
    ]),
    Question("Who signs bills to become laws?", [
        "the president",
    ]),
    Question("Who vetoes bills?", [
        "the president",
    ]),
    Question("What does the President's Cabinet do?", [
        "advises the president",
    ]),
    Question("What are two Cabinet-level positions?", [
        "secretary of agriculture",
        "secretary of commerce",
        "secretary of defense",
        "secretary of education",
        "secretary of energy",
        "secretary of health and human services",
        "secretary of homeland security",
        "secretary of housing and urban development",
        "secretary of the interior",
        "secretary of labor",
        "secretary of state",
        "secretary of transportation",
        "secretary of the treasury",
        "secretary of veteran affairs",
        "attorney general",
        "vice president",
    ], number_answers=2),
    Question("What does the judicial branch do?", [
        "reviews laws",
        "explains laws",
        "resolves disputes",
        "resolves disagreements",
        "decides if a law goes against the constitution",
    ]),
    Question("What is the highest court in the United States", [
        "the supreme court",
    ]),
    Question("How many justices are on the Supreme Court?", [
        "nine",
        "9",
    ]),
    Question("Who is the Chief Justice of the United States now?", [
        "john roberts",
        "john g. roberts jr.",
    ]),
    Question("Under our Constitution, some powers belong to the federal government. What is one power of the federal government?", [
        "to print money",
        "to declare war",
        "to create an army",
        "to make treaties",
    ]),
    Question("Under our Constitution, some powers belong to the states. What is one power of the states?", [
        "provide schooling and education",
        "provide protection",
        "police",
        "provide safety",
        "fire departments",
        "give a driver's license",
        "approve zoning and land use",
    ]),
    Question("Who is the Governor of your state now?", [
        "gavin newsom",
        "newsom",
    ]),
    Question("What is the capital of your state?", [
        "sacramento",
    ]),
    Question("What are the two major political parties in the United States?", [
        "republican",
        "democratic",
    ], number_answers=2),
    Question("What is the political party of the President now?", [
        "republican",
    ]),
    Question("What is the name of the Speaker of the House of Representatives now?", [
        "mike johnson",
        "johnson",
        "james michael johnson",
    ]),

    # C: Rights and Responsibilities
    Question("There are four amendments to the Constitution about who can vote. Describe one of them.", [
        "any citizen can vote",
        "women and men can vote",
        "citizens 18 and older can vote",
        "you don't have to pay to vote",
        "a male citizen of any race can vote",
    ]),
    Question("What is one responsibility that is only for United States citizens.", [
        "serve on a jury",
        "vote in a federal election",
    ]),
    Question("Name one right only for United States citizens.", [
        "vote in a federal election",
        "run for federal office",
    ]),
    Question("What are two rights of everyone living in the United States?", [
        "freedom of expression",
        "freedom of speech",
        "freedom of assembly",
        "freedom to petition the government",
        "freedom of religion",
        "the right to bear arms",
    ], number_answers=2),
    Question("What do we show loyalty to when we say the Pledge of Allegiance?", [
        "the united states",
        "the flag",
    ]),
    Question("What is one promise you make when you become a United States citizen?", [
        "give up loyalty to other countries",
        "defend the constitution and laws of the united states",
        "obey the laws of the united states",
        "serve in the U.S. military",
        "serve the nation",
        "be loyal to the united states",
    ]),
    Question("How old do citizens have to be to vote for President?", [
        "eighteen and older",
        "18 and older",
    ]),
    Question("What are two ways that Americans can participate in their democracy?", [
        "vote",
        "join a political party",
        "help with a campaign",
        "join a civic group",
        "join a community group",
        "give an elected official your opinion on an issue",
        "call senators or representatives",
        "publicly support or oppose an issue or policy",
        "run for office",
        "write to a newspaper",
    ], number_answers=2),
    Question("When is the last day you can send in federal income tax forms?", [
        "april 15",
    ]),
    Question("When must all men register for the selective service?", [
        "at age eighteen",
        "at age 18",
        "between 18 and 26",
        "between eighteen and twenty-six",
        "between 18 and twenty-six",
        "between eighteen and 26",
    ]),

    # AMERICAN HISTORY
    # A: Colonial Period and Independence
    Question("What is one reason colonist came to America?", [
        "freedom",
        "political liberty",
        "religious freedom",
        "economic opportunity",
        "practice their religion",
        "escape persecution",
    ]),
    Question("Who lived in America before the Europeans arrived?", [
        "american indians",
        "native americans",
    ]),
    Question("What group of people was taken to America and sold as slaves?", [
        "africans",
        "people from africa",
    ]),
    Question("Why did the colonists fight the British?", [
        "because of high taxes",
        "because of taxation without representation",
        "because the british army stayed in their houses",
        "because they didn't have self-government",
    ]),
    Question("Who wrote the Declaration of Independence?", [
        "jefferson",
        "thomas jefferson",
    ]),
    Question("When was the Declaration of Independence adopted?", [
        "july 4, 1776",
    ]),
    Question("There were 13 original states. Name three.", [
        "new hampshire",
        "massachusetts",
        "rhode island",
        "connecticut",
        "new york",
        "new jersey",
        "pennsylvania",
        "delaware",
        "maryland",
        "virginia",
        "north carolina",
        "south carolina",
        "georgia",
    ], number_answers=3),
    Question("What happened at the Constitutional Convention?", [
        "the constitution was written",
        "the founding fathers wrote the constitution",
    ]),
    Question("When was the Constitution written?", [
        "1787",
    ]),
    Question("The Federalist Papers supported the passage of the U.S. Constitution. Name one of the writers.", [
        "james madison",
        "madison",
        "alexander hamilton",
        "hamilton",
        "john jay",
        "jay",
        "publius",
    ]),
    Question("What is one thing Benjamin Franklin is famous for?", [
        "u.s. diplomat",
        "oldest member of the constitutional convention",
        "first postmaster general of the united states",
        "writer of \"poor richard's almanac\"",
        "started the first free libraries",
    ]),
    Question("Who is the \"Father of Our Country\"?", [
        "george washington",
        "washington",
    ]),
    Question("Who was the first President?", [
        "george washington",
        "washington",
    ]),
]

random.seed(datetime.now().timestamp())
correct_answers = 0
CORRECT_WEIGHT = 1
WRONG_WEIGHT = 20
print("There are", len(questions), "questions")
for index, question in enumerate(questions):
    print(str(index + 1) + ".", question.text)
    for line in question.answers:
        print("  -", line)
        if (not line.islower()) and line.isalpha():
            print("-------- format incorrect")
            exit(1)
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
        current_answer = input().lower()
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
