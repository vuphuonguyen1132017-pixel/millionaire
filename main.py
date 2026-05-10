questions = [
    ["What is the largest mammal?", "Shark", "Elephant", "Blue Whale", "Dolphin", 3],
    ["What planet is closet to the Sun?", "Earth", "Venus", "Mercury", "Mars", 3],
    ["Which planet is known as the Red Planet?", "Jupiter", "Venus", "Mars","Mercury", 1],
    ["What is the capital of the United States?", "New York", "Los Angeles", "Washington D.C", "Chicago", 3],
    ["What is H2O?", "Oxygen", "Salt", "Water", "Hydrogen", 3],
    ["How many playes are on a basketball team on the court?", "5", "6", "7", "11", 1]
]

for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    # Check whether the answer is correct or not
    a = int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d"))
    if(question[5] == a):
        print("Correct Answer")
    else:
        print(f"Incorrect, the correct anwer was {question[5]}")
        print("Better luck nex time!")
        break