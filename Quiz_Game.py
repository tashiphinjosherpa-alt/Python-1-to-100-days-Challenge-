questions = {
    "Capital of Nepal? ": "kathmandu",
    "2 + 2 = ? ": "4",
    "Python is language? ": "yes"
}

score = 0

for q, ans in questions.items():
    user = input(q).lower()

    if user == ans:
        score += 1

print("Final Score =", score)