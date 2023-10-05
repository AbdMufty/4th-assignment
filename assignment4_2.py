def computepay(hours, rate):
    salary = 0
    if hours <= 40:
        salary = hours * rate
    elif hours > 40:
        overtime = hours - 40
        overtime_salary = overtime * rate * 1.5
        salary = (hours * rate + overtime_salary) - (overtime * rate)
    return salary

try:
    hours = int(input("Enter your work hours: "))
    rates = float(input("Enter payment rate: "))
    if hours >= 0 and rates >= 0:
        computepay(hours, rates)
        print("Your slary is $", computepay(hours, rates))
    else:
        print("Please enter valid numerinc input")
except:
    print("Please enter valid numerinc input")