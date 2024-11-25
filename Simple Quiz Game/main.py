#Samantha Trejo, Simple Quiz Game

def quiz():
    score = 0

    questions = [
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A) H2O", "B) O2", "C) CO2", "D) H2"],
            "answer": "A"
        },
        {
            "question": "What planet is known as the Red Planet?",
            "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
            "answer": "B"
        },
        {
            "question": "What is the powerhouse of the cell?",
            "options": ["A) Nucleus", "B) Ribosome", "C) Mitochondria", "D) Golgi apparatus"],
            "answer": "C"
        },
        {
            "question": "What gas do plants absorb from the atmosphere?",
            "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"],
            "answer": "B"
        },
        {
            "question": "What is the main organ of the circulatory system?",
            "options": ["A) Brain", "B) Lungs", "C) Heart", "D) Liver"],
            "answer": "C"
        }
    ]

    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['question']}")
        for option in q['options']:
            print(option)

        user_answer = input("Please select A, B, C, or D: ").upper()

        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong! The correct answer was:", q["answer"])
            #Give an easier question if the user gets it wrong
            if i < len(questions) - 1:
                print("Here's an easier question:")
                easier_question = questions[i + 1]
                print(f"\nEasier Question: {easier_question['question']}")
                for option in easier_question['options']:
                    print(option)

                user_answer = input("Please select A, B, C, or D: ").upper()
                if user_answer == easier_question["answer"]:
                    print("Correct!")
                    score += 1
                else:
                    print("Wrong again! The correct answer was:", easier_question["answer"])

    print(f"\nYour total score is: {score} out of {len(questions)}")

if __name__ == "__main__":
    quiz()
