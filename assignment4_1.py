def grade_cal(score1):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    elif score < 60:
        grade = "F"
    
    return grade
try:
    score = int(input("Enter your score:"))
    if score >= 0 and score <= 100:
        #grade_cal(score)
        print("Your grade is ",grade_cal(score))
    else:
        print("Enter a numeric input beteen 0 - 100")
except:
    print("Enter a numeric input beteen 0 - 100")


