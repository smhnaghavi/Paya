import math
import matplotlib.pyplot as plt

# Input
n, num_subjects = map(int, input("Enter number of students and subjects: ").split())
w = int(input("Enter weight of correct answer: "))

questions = [0] + list(map(int, input("Enter number of questions per subject: ").split()))
weights = [0] + list(map(int, input("Enter weight of each subject: ").split()))

# Initialize arrays
raw_scores = [[0 for _ in range(num_subjects + 1)] for _ in range(n + 1)]
averages = [0.0 for _ in range(num_subjects + 1)]
std_devs = [0.0 for _ in range(num_subjects + 1)]
scaled_scores = [[0 for _ in range(num_subjects + 1)] for _ in range(n + 1)]
final_score = [0.0 for _ in range(n + 1)]
ranking = []

# Person-based input: correct/wrong answers for each student
for student in range(1, n + 1):
    print(f"\nEnter correct and wrong answers for all {num_subjects} subjects of Student {student}:")
    for subject in range(1, num_subjects + 1):
        correct, wrong = map(int, input(f"  Subject {subject} (correct wrong): ").split())
        raw_scores[student][subject] = (correct * w - wrong) / (questions[subject] * w)
        averages[subject] += raw_scores[student][subject]

# Calculate average per subject
for subject in range(1, num_subjects + 1):
    averages[subject] /= n

# Calculate standard deviation per subject
for subject in range(1, num_subjects + 1):
    sum_sq = 0
    for student in range(1, n + 1):
        sum_sq += (raw_scores[student][subject] - averages[subject]) ** 2
    std_devs[subject] = math.sqrt(sum_sq / n)

# Calculate scaled score (taraz) for each student in each subject
for student in range(1, n + 1):
    for subject in range(1, num_subjects + 1):
        if std_devs[subject] != 0:
            scaled_scores[student][subject] = 1000 * (raw_scores[student][subject] - averages[subject]) / std_devs[subject] + 5000
        else:
            scaled_scores[student][subject] = 5000

# Calculate final weighted score
total_weight = sum(weights[1:])
for student in range(1, n + 1):
    for subject in range(1, num_subjects + 1):
        final_score[student] += scaled_scores[student][subject] * weights[subject]
    final_score[student] /= total_weight
    ranking.append((final_score[student], student))

# Sort students by final score
ranking.sort()

# Print sorted student order
print("\nStudent order based on final score:")
for _, student_id in ranking:
    print(student_id, end=' ')
print()

# Plot final scores
names = [f"Student {student_id}" for _, student_id in ranking]
scores = [score for score, _ in ranking]

plt.figure(figsize=(12, 6))
bars = plt.bar(names, scores, color='skyblue')
plt.xticks(rotation=45)
plt.ylabel("Final Score")
plt.title("Final Weighted Scores of Students")
plt.grid(axis='y', linestyle='--', alpha=0.7)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 30, f"{yval:.0f}", ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()
