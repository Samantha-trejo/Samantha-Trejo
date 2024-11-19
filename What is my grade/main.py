#Samantha Trejo, What is my grade?

#Function to determine letter grade based on percentage
def get_letter_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

#List to store class names and grades
grades = []

while True:
    #Ask for class name and grade percentage
    class_name = input("Enter the class name (or type 'done' to finish): ")
    if class_name.lower() == 'done':
        break
    grade_percentage = float(input(f"Enter the grade percentage for {class_name}: "))
    
    #Determine letter grade and store the result
    letter_grade = get_letter_grade(grade_percentage)
    grades.append((class_name, letter_grade))

#Print out all class names and letter grades
print("\nHere are your grades:")
for class_name, letter_grade in grades:
    print(f"{class_name}: {letter_grade}")
