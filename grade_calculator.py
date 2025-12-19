# Week 2 Project: Student Grade Calculator
# Name: Purva

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

def grade_comment(grade):
    if grade == "A":
        return "Excellent performance"
    elif grade == "B":
        return "Very good job"
    elif grade == "C":
        return "Good, keep improving"
    elif grade == "D":
        return "Needs improvement"
    else:
        return "Failed, try harder"

# -------- INPUT VALIDATION --------

while True:
    try:
        total_students = int(input("Enter number of students: "))
        if total_students > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Enter a number.")

names = []
averages = []
grades = []
comments = []

subjects = ["Maths", "Science", "English"]

# -------- DATA COLLECTION --------

for i in range(total_students):
    print(f"\nStudent {i+1}")
    name = input("Enter student name: ")
    marks = []

    for subject in subjects:
        while True:
            try:
                mark = int(input(f"Enter marks for {subject} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter a number.")

    avg = sum(marks) / len(subjects)
    grade = calculate_grade(avg)
    comment = grade_comment(grade)

    names.append(name)
    averages.append(avg)
    grades.append(grade)
    comments.append(comment)

# -------- STATISTICS --------

class_avg = sum(averages) / total_students
highest = max(averages)
lowest = min(averages)

# -------- DISPLAY RESULTS --------

print("\n================ STUDENT RESULTS ================")
print(f"{'Name':<15}{'Average':<10}{'Grade':<8}{'Comment'}")
print("------------------------------------------------")

for i in range(total_students):
    print(f"{names[i]:<15}{averages[i]:<10.2f}{grades[i]:<8}{comments[i]}")

print("------------------------------------------------")
print(f"Class Average: {class_avg:.2f}")
print(f"Highest Score: {highest:.2f}")
print(f"Lowest Score : {lowest:.2f}")
print("================================================")

print("\nProgram completed successfully!")
