import csv

def get_grade(score):
    if score is None:
        return "N/A"
    elif 16 <= score <= 20:
        return "A"
    elif 12 <= score < 16:
        return "B"
    elif 8 <= score < 12:
        return "C"
    elif 0 <= score < 8:
        return "D"
    else:
        return "Invalid"

def clean_data(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        student_data = list(reader)

    for student in student_data:
        try:
            student["score"] = int(student["score"])
        except ValueError:
            student["score"] = None
        
        student["grade"] = get_grade(student["score"])

    return student_data

def generate_report(student_data):
    print("=== REPORT ===")
    for student in student_data:
        print(f"{student['name']} - Score: {student['score']} - Grade: {student['grade']}")

if __name__ == "__main__":
    data = clean_data("data/students.csv")
    generate_report(data)
    

# This code reads student data from a CSV file, cleans the data by handling invalid score values, assigns grades based on the scores, and generates a report. The `get_grade` function determines the grade based on the score, while the `clean_data` function processes the CSV file and handles any errors in the score values. Finally, the `generate_report` function prints out the cleaned data in a readable format.

"""This debugging taught you real engineering lessons:

Data format matters (CSV vs JSON)

Functions must return values

Code must actually execute

Output structure matters

This is real Data Engineering thinking.
"""