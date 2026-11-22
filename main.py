def classify_difficulty(question):
    question = question.lower()
    return "Easy"

print(classify_difficulty("Print hello world"))
def classify_difficulty(question):
    question = question.lower()

    easy_keywords = ["print", "variable", "input", "addition","add","sum", "even", "odd"]

    medium_keywords = ["loop", "function", "list", "dictionary", "sorting", "factorial"]

    hard_keywords = ["recursion", "algorithm", "inheritance", "machine learning", "dynamic programming"]
    easy_count = sum(word in question for word in easy_keywords)
    medium_count = sum(word in question for word in medium_keywords)
    hard_count = sum(word in question for word in hard_keywords)
    easy_count = sum(word in question for word in easy_keywords)
    medium_count = sum(word in question for word in medium_keywords)
    hard_count = sum(word in question for word in hard_keywords)
    if easy_count == 0 and medium_count == 0 and hard_count == 0:
        difficulty = "Medium"
        reason = "No matching keywords found."

    elif hard_count >= medium_count and hard_count >= easy_count:
        difficulty = "Hard"
        reason = "Advanced programming concepts detected."

    elif medium_count >= easy_count:
        difficulty = "Medium"
        reason = "Intermediate programming concepts detected."

    else:
        difficulty = "Easy"
        reason = "Basic programming concepts detected."

    return difficulty, reason
# Main Program

print("=" * 50)
print("PYTHON CODE DIFFICULTY CLASSIFIER")
print("=" * 50)
while True:
    question = input("\nEnter the Python problem (type exit to stop): ")

    if question.lower() == "exit":
        print("Thank you for using the classifier!")
        break
    difficulty, reason = classify_difficulty(question)

    print("\nCLASSIFICATION RESULT")
    print("Python Problem:", question)
    print("Difficulty:", difficulty)
    print("Reason:", reason)
