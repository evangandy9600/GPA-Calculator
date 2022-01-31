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

weight_dict = {
"AP": 1.0,
"HON": 1.0,
"REG": 0.0
}

# Total GPA Arrays
credit_values = []
point_values = []
weighted_point_values = []

def GPA_calculator(credit_val, point_val, w_point_val, type_gpa):
    x = sum(credit_val)
    y = sum(point_val)
    z = sum(w_point_val)
    uw_gpa = y / x # unweighted calculation
    w_gpa = z / x # weighted calculation
    if type_gpa == "Semester":
        credit_values.append(x)
        point_values.append(y)
        weighted_point_values.append(z)
        print(f"\n{type_gpa} Unweighted: {uw_gpa}")
        print(f"{type_gpa} Weighted: {w_gpa}\n")
    elif type_gpa == "Final":
        print(f"Final GPA Unweighted: {round(uw_gpa, 2)}") # Print GPA
        print(f"Final GPA Weighted: {round(w_gpa, 2)}") # Print GPA

# Retrives Grade Information
def get_grade():
    enter = 0
    sem_class = int(input("Total semesters taken: "))

    while sem_class > enter: # Semester
        enter += 1
        current_sem = enter # keeps semester updates

        # Semester Array
        sem_credit_values = []
        sem_point_values = []
        sem_weighted_point_values = []

        def class_grade(): # Gets each classes grade
            enter2 = 0
            num_class = int(input(f"Total classes in semester ({current_sem}): "))

            # Get class info
            while num_class > enter2:
                enter2 += 1
                # Student input
                name = input(f"\nClass: ")
                grade_weight = input(f"\tInput (Reg), (Hon) or (AP): ")
                credits = int(input(f"\t{grade_weight.upper()} {name.capitalize()} credits: "))
                grade = input(f"\t{grade_weight.upper()} {name.capitalize()} letter grade: ")
                print(f"\t{grade_weight.upper()} {name.capitalize()} -> Credits: ({credits}) Letter Grade: ({grade.upper()})")
                
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


                course_value(user_dict) # Using user_dict to calculate GPA

        class_grade()

        # Semester: Retrive totals from credit, grade/point value arrays
        GPA_calculator(credit_val = sem_credit_values, point_val = sem_point_values, w_point_val = sem_weighted_point_values, type_gpa = "Semester")
get_grade() # runs GPA calculator
GPA_calculator(credit_val = credit_values, point_val = point_values, w_point_val = weighted_point_values, type_gpa = "Final")
