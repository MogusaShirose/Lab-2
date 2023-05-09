def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/height**2
    print("BMI = " + str(bmi))
    if bmi < 18.5:
        print("You are Under Weight")
        return num - 2
    elif bmi > 25.0:
        print("You are Overweight")
        return num
    else:
        print("You are Normal Weight")
        return num -1

print(calculate_bmi(weight=57, height=1.73))