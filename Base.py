# Evan's GPA Calculator
# Formula: (Grade point value * credits) / (total number of credits)

# Dictionary
user_dict = { # Change this dictionary to match unweighted 4.0 GPA scale
    "A": 4.0, # A is worth 4 points always
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
    "F": 0 # F is worth 0 points always    
}

# It is reccomended that you do not adjust values below this line
standard_dict = {
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

weight_dict = {
"AP": 1.0,
"HON": 0.5,
"REG": 0.0
}

# Total GPA Arrays
credit_values = []
point_values = []
weighted_point_values = []

# Retrives Grade Information
def get_grade():
    gpa_scale = int(input(f"Select (1) for standard scale or select (2): "))
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
                # Student input
                name = input("Class: ")
                credits = int(input(f"{name} credits: "))
                grade = input(f"{name} letter grade: ")
                grade_weight = input("Input (Reg), (Hon) or (AP): ")
                print(f"{grade_weight.upper()} {name} -> Credits: ({credits}) Letter Grade: ({grade.upper()})")
                
                # Credits and class difficulty calculations
                sem_credit_values.append(credits) # save credits in array
                get_grade_weight = float(weight_dict.get(grade_weight.upper())) # save class difficulty in var

                # Dictionary based calculations
                def course_value(dict): # Parent function
                    get_grade_point = float(dict.get(grade.upper()))
                    uw = credits * (get_grade_point) # Unweighted grade point calculation
                    w = credits * (get_grade_point + get_grade_weight) # Weighted grade point calculation
                    sem_point_values.append(uw)
                    sem_weighted_point_values.append(w)

                # Dictionary Based Calculations
                if gpa_scale == 1:
                    course_value(standard_dict) # Using standard_dict to calculate GPA
                elif gpa_scale == 2:
                    course_value(user_dict) # Using user_dict to calculate GPA

        class_grade()

        # Semester: Retrive totals from credit, grade/point value arrays (NOT WORKING)
        def GPA_calculator(credit_val, point_val, w_point_val):
            x = sum(credit_val)
            y = sum(point_val)
            z = sum(w_point_val)
            uw_gpa = y / x # unweighted calculation
            w_gpa = z / x # weighted calculation
            credit_values.append(x)
            point_values.append(y)
            weighted_point_values.append(z)
            print(f"\nSemester ({current_sem}): {uw_gpa}")
            print(f"Semester ({current_sem}): {w_gpa}\n")

        # credit_val = sem_credit_values, point_val = sem_point_values, w_point_val = sem_weighted_point_values
        GPA_calculator(credit_val = sem_credit_values, point_val = sem_point_values, w_point_val = sem_weighted_point_values)

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
