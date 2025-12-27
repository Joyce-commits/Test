import os

# List of slam book questions
questions = [
    "What is your name?",
    "What is your nickname?",
    "When is your birthday?",
    "What is your favorite color?",
    "What is your favorite food?",
    "What is your biggest fear?",
    "Who is your best friend?",
    "What is your dream job?",
    "One word that describes you:",
    "Any message for me?"
]

def get_user_entry():
    print("\n--- Welcome to the Slam Book! ---")
    answers = {}

    for question in questions:
        answer = input(question + " ")
        answers[question] = answer

    return answers

def save_to_file(entry, filename="slambook.txt"):
    with open(filename, "a", encoding='utf-8') as file:
        file.write("\n--- New Entry ---\n")
        for question, answer in entry.items():
            file.write(f"{question} {answer}\n")
        file.write("\n")

def main():
    while True:
        entry = get_user_entry()
        save_to_file(entry)

        cont = input("Do you want to add another entry? (yes/no): ").strip().lower()
        if cont != "yes":
            print("Thanks for using the Slam Book. Goodbye!")
            break

if __name__ == "__main__":
    main()