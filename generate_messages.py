"get and process input for a list of names"

names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades counts separated by commas: ").split(",")

MESSAGE = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
    submit before you can graduate. You're current grade is {} and can increase \
    to {} if you submit all assignments before the due date.\n\n"


for name, assignment, grade in zip(names, assignments, grades):
    print(MESSAGE.format(name, assignment, grade, int(grade) + int(assignment)*2))
