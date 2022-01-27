# Evan's GPA Calculator
# Formula: (Grade point value * credits) / (total number of credits)
# How to run in ***VSCODE LOCALLY***:
    # Step 1) Click "F5" on keyboard to open terminal
    # Step 2) Run as python file
    # Step 3) In the bottom bar input values as you are prompted in the terminal window
    # Step 4) To weight a class, enter (W) when promted with "GPA Type: Unweighted (U) or Weighted (W) "
    # Step 5) If you prefer to calculate your unweighted GPA, enter (U) for all classes

# Dictionary
grade_dict = {
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "D-": 0.7,
    "F": 0
}
grade_dict2 = {
    "A": 4.0,
    "A-": 3.67,
    "B+": 3.34,
    "B": 3.0,
    "B-": 2.67,
    "C+": 2.34,
    "C": 2.0,
    "C-": 1.67,
    "D+": 1.34,
    "D": 1.0,
    "D-": 0.67,
    "F": 0    
}
weight_dict = {
"AP": 1.0,
"HON": 0.5,
"REG": 0.0,
}

# Arrays
credit_values = []
point_values = []
weighted_point_values = []

# Retrives Information
def get_grade():
    gpa_scale = int(input("(0.67 & 0.34) or (0.7 & 0.3) (Enter (1) or (2): "))
    enter = 0
    sem_class = int(input("Total number of semesters taken: "))
    # Semester
    while sem_class > enter:
        enter += 1
        current_sem = enter + 1 # work

        # Semester Array
        sem_credit_values = []
        sem_point_values = []
        sem_weighted_point_values = []

        def class_grade(): # Gets each classes grade
            enter2 = 0
            num_class = int(input("Total classes this semester: "))

            # Get class info
            while num_class > enter2:
                enter2 += 1
                # Input
                name = input("Class: ")
                credits = int(input(f"{name} credits: "))
                grade = input(f"{name} letter grade: ")
                grade_weight = input("Input (Reg), (Hon) or (AP): ")
                print(f"{grade_weight.upper()} {name} -> Credits: ({credits}) Letter Grade: ({grade.upper()})")
                
                # Credit vaules and class difficulty
                sem_credit_values.append(credits) # save credits in array
                get_grade_weight = float(weight_dict.get(grade_weight.upper())) # save class difficulty in var

                # Dictionary based calculations
                def course_value(dict): # Parent function
                    get_grade_point = float(dict.get(grade.upper()))
                    uw = credits * (get_grade_point) # Unweighted grade point calculation
                    w = credits * (get_grade_point + get_grade_weight) # Weighted grade point calculation
                    sem_point_values.append(uw)
                    sem_weighted_point_values.append(w)
                    return

                # Dictionary dependency
                if gpa_scale == 1:
                    course_value(grade_dict2)
                elif gpa_scale == 2:
                    course_value(grade_dict)
                return
        class_grade()

        # Semester: Retrive totals from credit, grade/point value arrays (NOT WORKING)
        '''
        def GPA_calculator(credit_val, point_val, w_point_val):
        print(credit_val, point_val, w_point_val)
        x = sum(credit_val)
        y = sum(point_val)
        z = sum(point_val)
        uw_gpa = y / x # unweighted calculation
        w_gpa = z / x # weighted calculation
        print(f"This is test {uw_gpa}")
        print(f"This is test {w_gpa}")
        return

        # credit_val = sem_credit_values, point_val = sem_point_values, w_point_val = sem_weighted_point_values
        GPA_calculator(credit_val = sem_credit_values, point_val = sem_point_values, w_point_val = sem_weighted_point_values)
        '''

        # Semester: Calculations
        x = sum(sem_credit_values)
        y = sum(sem_point_values)
        z = sum(sem_weighted_point_values)
        uw_gpa = y / x # unweighted calculation
        w_gpa = z / x # weighted calculation

        # Semester: Append
        credit_values.append(x)
        point_values.append(y)
        weighted_point_values.append(z)
        
        # Semester: Print semester GPA
        print(f"Semester Unweighted: {round(uw_gpa, 2)}")
        print(f"Semester Weighted: {round(w_gpa, 2)}")

get_grade() # runs GPA calculator

# All: Retrive totals arrays
x = sum(credit_values)
y = sum(point_values)
z = sum(weighted_point_values)
uw_gpa = y / x # unweighted calculation
w_gpa = z / x # weighted calculation

# All: Print GPA
print(f"All Semesters Unweighted: {round(uw_gpa, 2)}")
print(f"All Semesters Weighted: {round(w_gpa, 2)}")
