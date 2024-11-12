#Samantha Trejo, Average Grade

#Initialize an empty list to store the grades
grades = []


#Get the number of classes from the user
num_classes = int(input("Enter the number of classes: "))


#Loop to get the grades for each class
for i in range(num_classes):
    grade = float(input(f"Enter the grade for class {i + 1}: "))
    grades.append(grade)


#Calculate the average grade
average_grade = sum(grades) / num_classes


#Output the average grade
print(f"Your average grade is: {average_grade:.2f}")