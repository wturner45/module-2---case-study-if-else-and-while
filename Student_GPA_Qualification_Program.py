# Student GPA Qualification Program

while True:
    # Ask for the student's last name
    last_name = input("Enter student's last name (or ZZZ to quit): ")

    # Check if the user wants to quit
    if last_name.upper() == "ZZZ":
        print("Program ended.")
        break

    # Ask for the student's first name
    first_name = input("Enter student's first name: ")

    # Ask for the student's GPA
    gpa = float(input("Enter student's GPA: "))

    # Check Dean's List qualification
    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List!")

    # Check Honor Roll qualification
    if gpa >= 3.25:
        print(first_name, last_name, "has made the Honor Roll!")

    # Separate student records
    print()